from app import app

print("asgi.gy", __name__)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5432)
