from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate,PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan) #automatically runs and creates database when the app is started



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