from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="SFGLAM Sensory Analysis API",
    description="Backend API for analyzing beauty product reviews.",
    version="1.0.0"
)


class ReviewRequest(BaseModel):
    reviews: list[str]


@app.get("/")
def root():
    return {
        "message": "SFGLAM AI backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/analyze")
def analyze_reviews(request: ReviewRequest):
    return {
        "review_count": len(request.reviews),
        "message": "Reviews received successfully"
    }