from sqlalchemy import Column, Text, Integer, ForeignKey

from core.db import Base


class Foto (Base):
    file = Column()
    discription = Column(Text, nullable=False)
    album_id = Column(Integer, ForeignKey="album.id")