from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from mangum import Mangum

app = FastAPI()

API_KEY = "mysecretkey123"

class Message(BaseModel):
    session_id: str
    message: str

@app.post("/honeypot")
def honeypot(data: Message, x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

    return {
        "scam_detected": False,
        "status": "ok",
        "reply": "Hello, can you explain more?",
        "session_id": data.session_id
    }
handler = Mangum(app, lifespan="off")
# Vercel handler

