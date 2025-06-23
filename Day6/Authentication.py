from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "mysecureapikey123"

@app.get("/secure-data")
def read_secure_data(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": "This is secured data"}