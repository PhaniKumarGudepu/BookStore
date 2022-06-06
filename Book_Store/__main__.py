from . import app                                      
from . import engine
from . import Base
from . import models
from . import webapp 



Base.metadata.create_all(engine)
app.run(host='0.0.0.0', port=1201)
