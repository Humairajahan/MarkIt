from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from backend_server.utils.model import Attendance
from datetime import datetime

router = APIRouter()


@router.post("/checkIn")
async def checkin(request: Attendance):
    try:
        return JSONResponse(
            status_code=200,
            content={
                "user": request.email,
                "status": "check-in with MarkIt successful!",
                "time": jsonable_encoder(datetime.now()),
            },
        )
    except Exception:
        raise HTTPException(status_code=400, detail="check-in with MarkIt failed")
