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
    reviews = request.reviews

    positive_terms = [
        "fragrance-free",
        "unscented",
        "lightweight",
        "comfortable",
        "gentle",
        "smooth",
        "soothing",
        "non-sticky",
        "weightless"
    ]

    negative_terms = [
        "strong scent",
        "fragrance",
        "sticky",
        "greasy",
        "heavy",
        "irritating",
        "burning",
        "stinging",
        "itchy"
    ]

    positive_mentions = 0
    negative_mentions = 0

    for review in reviews:
        review_lower = review.lower()

        for term in positive_terms:
            if term in review_lower:
                positive_mentions += 1

        for term in negative_terms:
            if term in review_lower:
                negative_mentions += 1

    total_mentions = positive_mentions + negative_mentions

    if total_mentions == 0:
        sensory_score = 50
    else:
        sensory_score = round(
            (positive_mentions / total_mentions) * 100
        )

    return {
        "review_count": len(reviews),
        "positive_mentions": positive_mentions,
        "negative_mentions": negative_mentions,
        "sensory_score": sensory_score
    }