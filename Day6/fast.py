from fastapi import FastAPI # fastapi is package, FastAPI is a class
app = FastAPI() # instance of the class (object)

@app.get("/") # get request anotation (empty string)

def read_api(): # function
    return {'selcome' : 'shubham'}

