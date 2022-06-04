from flask import Flask                                        
######                                        
# Remove these line of code when you no longer require a dummy response                                        
import json                                        
import os                                        
DUMMY_RESPONSE_FILE = os.path.join('Book_Store','dummy_response.json')                                        
with open(DUMMY_RESPONSE_FILE, 'r') as fi:                                        
    DUMMY_RESPONSE_JSON = json.load(fi)                                        
######                                        

app = Flask('__name__')
