from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL= "postgresql://postgres:hogYMLhMQQJjUpUrUlAzGcTcqwcEcQNd@shuttle.proxy.rlwy.net:26469/railway"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
session=SessionLocal(bind=engine)