
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://health:health@db:5432/clinical")
Session=sessionmaker(bind=engine)
