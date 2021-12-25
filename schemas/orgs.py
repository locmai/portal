from typing import Optional
from schemas.base import BaseSchema


# Shared properties
class OrgSchema(BaseSchema):
    full_name: Optional[str] = None
    is_active: bool = False

# Properties to receive via API on creation
class OrgCreate(OrgSchema):
    full_name: str
    is_active: bool

# Properties to receive via API on update
class OrgUpdate(OrgSchema):
    full_name: Optional[str]
    is_active: Optional[bool]

