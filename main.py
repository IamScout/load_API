import uvicorn
from fastapi import FastAPI
from routers.load_data_router import router as load_data_router
from routers.check_data_router import router as check_data_router
from routers.etc_routers import router as etc_routers
from routers.delete_data_router import router as delete_data_router 

def create_app():
    app = FastAPI()
    app.include_router(load_data_router)
    app.include_router(check_data_router)
    app.include_router(etc_routers)
    app.include_router(delete_data_router)
    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)