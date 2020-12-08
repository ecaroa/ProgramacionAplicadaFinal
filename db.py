from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


engine = create_engine('sqlite:///baseCarrera.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
