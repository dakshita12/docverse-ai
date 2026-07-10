from fastapi import FastAPI

app = FastAPI(
    title="DocVerse AI API",
    description="Backend API for the AI-powered study workspace.",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to DocVerse AI"}

@app.get("/login")
def login():
    return {"message": "Login Page"}