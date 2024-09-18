import os
import sys
from http.client import responses

sys.path.append(os.getcwd())
sys.path.append('./')
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from ..models.file_upload import FileUploadRequest, FileUploadResponse, ListFilesResponse
import logging
import subprocess

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/uploadFile/", response_model=FileUploadResponse)
async def create_item(request: FileUploadRequest):
    try:
        file = request.file
        user_id = request.user_id
        logger.info(f"Request received at backend for user: {user_id}")
        logger.info(f"File received at backend: {file.filename}")

        if not os.path.exists(os.path.join(os.getcwd(), f"data/{user_id}")):
            os.makedirs(os.path.join(os.getcwd(), f"data/{user_id}"))
            logger.info(f"Directory created for first time user: {user_id}")

        file_path = os.path.join(os.getcwd(), f"data/{user_id}/{file.filename}")
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        logger.info(f"File saved at: {file_path}")

        response = FileUploadResponse(
            file_name=file.filename,
            file_size=os.path.getsize(file_path),
            user_id=user_id,
            str_message="File uploaded successfully",
            status=True
        )

    except Exception as e:
        logger.error(f"Error in receiving file: {str(e)}")
        raise HTTPException(status_code=800, detail=f"File Upload failed: {str(e)}")

    return response


@router.get("/listFiles/", response_model=ListFilesResponse)
async def list_files(user_id: str):
    try:
        logger.info(f"Request received at backend for user: {user_id}")

        if not os.path.exists(os.path.join(os.getcwd(), f"data/{user_id}")):
            logger.info(f"Directory not found for user: {user_id}")
            raise HTTPException(status_code=801, detail=f"Directory not found for user: {user_id}")

        files = os.listdir(os.path.join(os.getcwd(), f"data/{user_id}"))
        logger.info(f"Files found for user: {user_id} are: {files}")

        response = ListFilesResponse(
            user_id=user_id,
            files=files,
            str_message="Files listed successfully",
            status=True
        )

    except Exception as e:
        logger.error(f"Error in listing files: {str(e)}")
        raise HTTPException(status_code=850, detail=f"Error in listing files: {str(e)}")

    return response
