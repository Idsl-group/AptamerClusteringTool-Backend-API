import os
import sys
sys.path.append(os.getcwd())
sys.path.append('./')
from fastapi import APIRouter, HTTPException
from e2edna_api.app.models.update import Update
import logging
from e2edna_api.app.config.yaml import read_yaml, write_yaml

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/")
async def create_user(request: Update):
    logger.info(f"Received user: {request}")
    path = './'

    try:
        data = read_yaml(path)
        data['mode'] = request.dock_mode
        data['aptamer_seq'] = request.sequence
        data['ligand'] = request.ligand
        data['ligand_type'] = request.ligand_type
        data['ligand_seq'] = request.ligand_seq
        write_yaml(path, data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"File could not be read - {e}")

    return True
