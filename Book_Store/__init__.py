from re import T
from flask import Flask                                        
######                                        
# Remove these line of code when you no longer require a dummy response                                        
import json                                        
import os                                        
DUMMY_RESPONSE_FILE = os.path.join('Book_Store','dummy_response.json')                                        
with open(DUMMY_RESPONSE_FILE, 'r') as fi:                                        
    DUMMY_RESPONSE_JSON = json.load(fi)                                        
######                             
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#Sqlalchamy - intitalizations
engine = create_engine('sqlite:////Users/phanigudepu/projects/BookStore/book_store.db', echo=True,future=True)
Base = declarative_base()
session_factory = sessionmaker(bind=engine, future = True)
#flask - inializations
app = Flask('__name__')
