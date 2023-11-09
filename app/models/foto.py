from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text

from app.core.db import Base


class Photo(Base):
    """Модель для фотографий."""

    photography = Column(Text)  # Нужно разобраться как добавлять изображения
    discription = Column(Text, nullable=False)
    album_id = Column(Integer, ForeignKey("album.id"))
    date = Column(DateTime, default=datetime.now)
