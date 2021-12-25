from typing import Optional

from pydantic import BaseModel, EmailStr

class BaseSchema(BaseModel):
    id: Optional[int] = None