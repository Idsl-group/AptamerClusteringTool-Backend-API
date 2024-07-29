import os
import sys
sys.path.append(os.getcwd())
sys.path.append('./')
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from E2EDNA_API.app.models.dock import Dock
import logging
import subprocess

router = APIRouter()
logger = logging.getLogger(__name__)


def run_command():
    command = ["python3", "main.py", "-yaml", "simu_config.yaml", "-ow"]
    result = subprocess.run(command, capture_output=True, text=True)

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    if result.returncode != 0:
        raise Exception(f"Command failed with return code {result.returncode}")


@router.get("/dock")
async def create_item(request: Dock):
    logger.info(f"Received item: {request}")
    run_command()
    return JSONResponse(content={'Executed': True})  # Change to Score
