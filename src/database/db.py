from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.conf.config import config


engine = create_async_engine(config.DB_URL)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)