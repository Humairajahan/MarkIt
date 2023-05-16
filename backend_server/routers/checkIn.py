from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from backend_server.utils.model import Attendance
from backend_server.utils.redis_client import RedisClient
from datetime import datetime

router = APIRouter()

redis_Client = RedisClient()


@router.post("/checkIn")
async def checkin(request: Attendance):
    try:
        response = redis_Client.findTodaysCheckINEntry(request.email)
        if response == 404:
            raise HTTPException(status_code=response, detail="Error with Redis!")
        else:
            return JSONResponse(
                status_code=response,
                content={
                    "user": request.email,
                    "status": "check-in with MarkIt successful!",
                    "time": jsonable_encoder(datetime.now()),
                },
            )
    except Exception:
        raise HTTPException(status_code=400, detail="check-in with MarkIt failed")
