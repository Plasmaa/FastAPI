from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "Hello World", "content": "My first blog post!"},
    2: {"title": "FastAPI Tips", "content": "Use Pydantic for validation."},
    3: {"title": "Python 3.12", "content": "New features are awesome."},
    4: {"title": "Coffee Break", "content": "Time for an espresso."},
    5: {"title": "Debugging", "content": "print() is all you need."},
    6: {"title": "REST APIs", "content": "Keep your endpoints clean."},
    7: {"title": "Weekend Plans", "content": "Coding and hiking."},
    8: {"title": "Book Review", "content": "Clean Code is a classic."},
    9: {"title": "Async IO", "content": "Concurrency made simple."},
    10: {"title": "Deployment", "content": "Dockerize everything."}
}

# query paramerters - they filter data in the response based on the value passed in the url 
@app.get("/posts")
def get_all_posts(limit: int = None, text_length: int = None): 
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]


# posting using pydantic schemas - we don't use path like /posts/{id}, instead we use the body to pass the data
# why don't we directly use path while posting? because it creates ambiguity with the dynamic ids & we use body to pass the data
@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post