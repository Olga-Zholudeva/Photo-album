from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from config import settings
from sqlalchemy import Column, Integer

class PreBase():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    
    id = Column(Integer, primary_key=True)

Base = declarative_base(PreBase)

engine = create_async_engine(
    url=settings.database_url,
    echo=True,  # При установлении этого параметра в консоль будут выводится все зарпосы, которые делает sqlalchemy к нашей БД
    # pool_size=5, # Количество соединений
    # max_overflow=10 # Количество доплнительных подключений, на случай если все доступные подключения уже заняты
)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)

