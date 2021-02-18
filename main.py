import uvicorn
import fastapi
from views import home
from api import weather_api

api = fastapi.FastAPI()

def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)

if __name__ == "__main__":
    configure()
    uvicorn.run(api, host="127.0.0.1", port=8000,)

