from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from app.schemas import CourseCategory, TopicCreate, TopicResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="ML/DS Pending Bucket API",
    description="API for managing Machine Learning and Data Science learning topics and resources.",
    version="0.1.0",
)


# Temporary in-memory data.
# This will be replaced by PostgreSQL when we reach the database section.
topics = {
    1: {
        "id": 1,
        "title": "Gradient Descent",
        "description": "Understand the intuition and mathematics behind gradient descent.",
        "module": 10,
        "category": CourseCategory.MACHINE_LEARNING,
        "hashtags": ["gradientdescent", "optimization"],
    },
    2: {
        "id": 2,
        "title": "Bayes Theorem",
        "description": "Revise conditional probability and Bayes theorem.",
        "module": 23,
        "category": CourseCategory.DATA_SCIENCE,
        "hashtags": ["probability", "bayes", "statistics"],
    },
}


@app.get("/topics", response_model=list[TopicResponse])
def get_all_topics(
    limit: int | None = None,
):
    if limit is not None:
        return list(topics.values())[:limit]

    return list(topics.values())


@app.get("/topics/{topic_id}", response_model=TopicResponse)
def get_topic(topic_id: int):
    if topic_id not in topics:
        raise HTTPException(
            status_code=404,
            detail="Topic not found",
        )

    return topics[topic_id]


@app.post("/topics", response_model=TopicResponse, status_code=201)
def create_topic(topic: TopicCreate):
    new_id = max(topics.keys(), default=0) + 1

    new_topic = {
        "id": new_id,
        **topic.model_dump(),
    }

    topics[new_id] = new_topic

    return new_topic