from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from api import weather_api
from home import home
app = FastAPI()

def configure():
    configure_router()
    
def configure_router():
    app.mount("/static",StaticFiles(directory="static"),name="static")
    app.include_router(weather_api.router)
    app.include_router(home.router)


if __name__ == "__main__":
    configure()
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    configure()