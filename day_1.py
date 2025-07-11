from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greetings():
    return {"message": "Hello,world!"}

@app.get("/introduction")
def intro():
    return {"mesasge":"I am Saurabh Dubey and I am an AI Developer. I am currently learning FastAPI and I am excited to build APIs with it."}

@app.get("/about")
def about():
    return {"message": "FastAPI seems easy and cool to learn. I am excited to learn more about it and build APIs with it."}

@app.get("/more")
def more():
    return {"message": "It's my first day of learning FastAPI and I am enjoying it so far. I hope to build some amazing APIs with it."}