from dataclasses import dataclass
import os
import redis
import json
from backend_server.utils.logger import logger
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("backend_server/.env")


@dataclass
class RedisClient:
    host: str = os.getenv("REDIS_URL")
    port: int = 6379
    db: int = 0
    redis_key: str = os.getenv("USER_KEY")

    def __init__(self):
        self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)

    def pushToRedis(self, data):
        self.redis_client.set(self.redis_key, json.dumps(data))

    def loadCache(self):
        redis_keys = self.redis_client.keys()
        key_in_bytes = str.encode(self.redis_key)
        if key_in_bytes in redis_keys:
            users = json.loads(self.redis_client.get(self.redis_key))
        else:
            users = {"user": {"date": "", "checkIN": "", "checkOUT": ""}}
            self.pushToRedis(data=users)
        return users

    def findUser(self, user):
        users = self.loadCache()
        users_list = list(users.keys())
        if user in users_list:
            logger.info(f"Find user : User <{user}> exists")
            return True, users
        else:
            logger.info(f"Find user : New user <{user}>")
            return False, users

    def findTodaysCheckINEntry(self, user):
        user_exists, users = self.findUser(user=user)
        if user_exists is False:
            logger.info("Create new user")
            users[user] = {
                "date": jsonable_encoder(datetime.now().date()),
                "checkIN": jsonable_encoder(datetime.now()),
                "checkOUT": "None",
            }
            self.pushToRedis(data=users)
            return 201
        else:
            logger.info("User exists")
            date = users[user]["date"]
            if date == str(datetime.now().date()):
                logger.info("User Checked In already")
                return 404
            else:
                logger.info("User Check In yet to be done")
                users[user]["checkIN"] = jsonable_encoder(datetime.now())
                self.pushToRedis(data=users)
                return 200

    def findTodaysCheckOUTEntry(self, user):
        user_exists, users = self.findUser(user=user)
        if user_exists is False:
            logger.info(f"CheckOUT for New User <{user}> NOT ALLOWED")
            return 404
        else:
            logger.info("User exists")
            date = users[user]["date"]
            checkout = users[user]["checkOUT"]
            if date == str(datetime.now().date()) and checkout == "None":
                logger.info("User Check Out yet to be done")
                users[user]["checkOUT"] = jsonable_encoder(datetime.now())
                self.pushToRedis(data=users)
                return 200
            else:
                logger.info("User Check Out done for today")
                return 400
