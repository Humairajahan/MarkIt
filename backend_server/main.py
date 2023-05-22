from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend_server.routers import checkIn, checkOut

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(checkIn.router)
app.include_router(checkOut.router)