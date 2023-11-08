from config import settings
from sqlalchemy import Column, Imagq, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(PreBase)

engine = create_async_engine(
    url=settings.database_url,
    echo=True,
)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)
