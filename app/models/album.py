from core.db import Base

from sqlalchemy import Column, String, Text


class Album(Base):
    title = Column(String(100), unique=True, nullable=False)
    discription = Column(Text, nullable=False)