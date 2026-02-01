from fastapi import FastAPI
from pa_reply.api.routes import router

app = FastAPI(title="Passive Aggressive Reply API")
app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Up and running",
        "docs": "/docs",
        "health": "/health",
        "generate": "/generate"
    }
