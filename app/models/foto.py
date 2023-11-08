from datetime import datetime

from core.db import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text


class Photo(Base):
    photography = Column()  # Нужно разобраться как добавлять изображения
    discription = Column(Text, nullable=False)
    album_id = Column(Integer, ForeignKey("album.id"))
    date = Column(DateTime, default=datetime.now)
