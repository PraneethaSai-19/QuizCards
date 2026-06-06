#1.import create engine which is used to create connection with db
from sqlalchemy import create_engine
#3.import session maker to create object and talk to db
from sqlalchemy.orm import sessionmaker
#5. import declarative_base to create a base class for all the tables
from sqlalchemy.ext.declarative import declarative_base


#2.create an obj "engine" for create_engine(with db_url as a parameter)
db_url = "mysql+pymysql://root:Mo%40141202@localhost/quizcards"
engine = create_engine(db_url)

#4. create an object sessionlocal and create a session with db to communicate 
SessionLocal = sessionmaker(
    autocommit = False, #autocommit to control data changes permantantly into db
    autoflush=False,#autoflush to control data changes temporarily into db_buffer
    bind=engine
)

#6. use declarative base to create a base class for tables 
""" why base class is needed??
Because SQLAlchemy needs a way to:

recognize which classes are database tables
collect metadata about all tables
create tables automatically
map Python objects ↔ database rows
"""
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()