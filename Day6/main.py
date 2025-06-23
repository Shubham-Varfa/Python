from fastapi import FastAPI # from package import Class

app = FastAPI() 
# app [creating a FastAPI web application instance]
# FastAPI() [creates your app]

@app.get("/") #registers an endpoint that listens for GET requests to /hello.
def say_hello():
    return {"message": "Hello, FastAPI!"}
