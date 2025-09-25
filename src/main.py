from fastapi import FastAPI
import uvicorn
from api import router

app = FastAPI()
app.include_router(router)


# @app.get("/")
# def home():
#     return {"message": "Fuck"}


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
