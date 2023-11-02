from sqlalchemy import Column, Text, Integer, ForeignKey, DateTime

from core.db import Base
from datetime import datetime


class Foto (Base):
    file = Column()
    discription = Column(Text, nullable=False)
    album_id = Column(Integer, ForeignKey("album.id"))
    date = Column(DateTime, default=datetime.now)