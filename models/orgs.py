from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Org(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
