import uvicorn
from fastapi import FastAPI
from routers.load_data_router import *
from routers.check_data_router import * 

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)