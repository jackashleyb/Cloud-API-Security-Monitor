from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Cloud API Security Monitor is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

