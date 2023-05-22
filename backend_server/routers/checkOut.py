from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from backend_server.utils.model import Attendance
from backend_server.utils.redis_client import RedisClient
from datetime import datetime

router = APIRouter()

redis_Client = RedisClient()

@router.post("/checkOut")
async def checkout(request: Attendance):
    try:
        response = redis_Client.findTodaysCheckOUTEntry(request.email)
        if response == 200:
            return JSONResponse(
                status_code=response,
                content={
                    "user": request.email,
                    "status": "check-out with MarkIt successful!",
                    "time": jsonable_encoder(datetime.now()),
                },
            )
        else:
            return JSONResponse(
                status_code=response,
                content={
                    "detail": 
                        "Either user already checked out today or checking out for unregistered user"
                }
            )
    except Exception:
        raise HTTPException(status_code=400, detail="check-out with MarkIt failed")