from sqlalchemy import create_engine , Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#databse URL
DATABASES_URL= "postgresql://postgres:12345%4054321@localhost:5432/Usermanagment"


#database engine 
engine=create_engine(DATABASES_URL)

#Session for Database
sessionLocal = sessionmaker(autoflush=False, bind=engine)

#base for model
Base=declarative_base()


