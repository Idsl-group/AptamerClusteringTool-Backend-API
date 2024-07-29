from pydantic import BaseModel
from typing import Optional


class Dock(BaseModel):
    dock_score_mode: Optional[str] = 'coarse'
    