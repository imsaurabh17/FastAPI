from pydantic import BaseModel, Field, StrictInt
from typing import Optional

class Employee(BaseModel):
    id: int = Field(...,gt=0)
    name: str = Field(...,min_length=3,max_length=30)
    dep: str = Field(...,min_length=2,max_length=30)
    sal: Optional[StrictInt] = Field(default=None)