from distutils.log import debug
from Book_Store import app                                      
from Book_Store import engine
from Book_Store import Base
from Book_Store import models
from Book_Store import webapp 
from Book_Store.load_data import LoadCSVData

# DB related
Base.metadata.create_all(engine)
LoadCSVData().load_data_from_csv()
# Flask related
app.run(host='0.0.0.0', port=1201,debug=True)
