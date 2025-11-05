from pydantic import BaseModel
from typing import Optional

class TelexRequest(BaseModel):
    input: Optional[dict] = {}
