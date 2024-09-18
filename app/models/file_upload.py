from pydantic import BaseModel
from typing import Optional, List
from fastapi import File, UploadFile


class FileUploadRequest(BaseModel):
    file: UploadFile = File(...)
    user_id: str = None


class FileUploadResponse(BaseModel):
    file_name: str
    location: int
    user_id: str = None
    status: bool = True
    message: str = "File uploaded successfully"


class ListFilesResponse(BaseModel):
    user_id: str = None
    files: List[str] = []
    status: bool = True
    message: str = "Files listed successfully"