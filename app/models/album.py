from sqlalchemy import Column, DateTime, String, Text

from app.core.db import Base


class Album(Base):
    """Модель для создания альбомов."""

    title = Column(String(100), unique=True, nullable=False)
    discription = Column(Text, nullable=False)
    date_update = Column(DateTime)
