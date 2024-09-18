from pydantic import BaseModel
from typing import Optional


class AddUserRequest(BaseModel):
    username: str
    user_id: str = None


class AddUserResponse(BaseModel):
    user_id: str
    status: bool = True
    message: str = "User added successfully"

