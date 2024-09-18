import os
import sys
sys.path.append(os.getcwd())
sys.path.append('./')
from fastapi import APIRouter, HTTPException
from ..models.add_user import AddUserRequest, AddUserResponse
import logging
from ..config.yaml import read_yaml, write_yaml

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/addNewUser", response_model=AddUserResponse)
async def create_user(request: AddUserRequest):
    try:
        user_id = request.user_id
        username = request.username

        logger.info(f"Adding user {username} with id {user_id}")

        response = AddUserResponse(
            user_id=user_id,
            status=True,
            message="User added successfully"
        )
        pass

    except Exception as e:
        logger.error(f"Error adding user: {e}")
        raise HTTPException(status_code=802, detail=f"Error adding user: {e}")

