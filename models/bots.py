from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base


class Bot(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    owner = relationship("User", back_populates="bots")
