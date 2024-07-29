from pydantic import BaseModel
from typing import Optional


class Update(BaseModel):
    sequence: Optional[str] = None
    dock_mode: Optional[str] = 'coarse dock'
    ligand: Optional[str] = None
    ligand_type: Optional[str] = None
    ligand_seq: Optional[str] = None
