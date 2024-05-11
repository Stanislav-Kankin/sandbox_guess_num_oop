from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///scores.db')
Base = declarative_base()


class Score(Base):
    __tablename__ = 'Таблица очков'
    id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String(100), nullable=False)
    number_of_try = Column(Integer, nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
