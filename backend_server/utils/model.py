from pydantic import BaseModel, EmailStr


class Attendance(BaseModel):
    email: EmailStr
