from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate,PostResponse

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Test Post"},
    2: {"title": "Getting Started with FastAPI", "content": "FastAPI is a modern web framework for building APIs with Python."},
    3: {"title": "Python Tips", "content": "Use list comprehensions for cleaner and faster code."},
    4: {"title": "Async Programming", "content": "Async functions in Python allow non-blocking code execution."},
    5: {"title": "REST API Design", "content": "Good REST APIs are stateless, consistent, and well-documented."},
    6: {"title": "Database Integration", "content": "FastAPI works seamlessly with SQLAlchemy and async ORMs like Tortoise."},
    7: {"title": "Pydantic Models", "content": "Pydantic models in FastAPI provide automatic data validation and serialization."},
    8: {"title": "Authentication with JWT", "content": "Secure your FastAPI endpoints using OAuth2 and JWT tokens."},
    9: {"title": "Dependency Injection", "content": "FastAPI's dependency injection system makes it easy to share logic across routes."},
    10: {"title": "Deploying FastAPI", "content": "Deploy FastAPI apps using Docker and cloud platforms like AWS or Railway."},
}

#creating end points neccessary for the project

@app.get("/posts") # decorator to modify customized url-endpoint

def get_all_posts(limit:int = None):
    if limit:
        return list(text_posts.values())[:limit]
    
    return text_posts #created as dictionary since dealing with JSON format

@app.get("/posts{id}")

def get_post(id:int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404,detail="Post not found")
    return text_posts.get(id)

@app.post("/posts")

def create_post(post:PostCreate)->PostResponse:
    new_post = {"title":post.title,"content":post.content}
    text_posts[max(text_posts.keys())+1] = new_post
    return new_post