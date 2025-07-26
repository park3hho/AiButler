from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World WWW I'm Your Fans"}
