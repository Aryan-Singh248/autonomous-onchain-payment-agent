from fastapi import FastAPI
from app.api.routes import router as payments_router

app = FastAPI(title="Autonomous On-Chain Payment Agent")

@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(payments_router, prefix="/payments")
