import fastapi
import os
import httpx
from dotenv import load_dotenv
load_dotenv()
from typing import Optional
from fastapi import Depends
router = fastapi.APIRouter()

from models.location import Location
    

@router.get("/api/weather/{city}")
async def weather(location: Location = Depends(),units: Optional[str] = 'metric'):
    API_KEY = os.environ.get('API_KEY')
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location.city},{location.country}&appid={API_KEY}&units={units}"
    
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        if resp.status_code != 200:
            return {"message": "Something Went Wrong! Try Another City with country"}
        data = resp.json()
        return data['main']
            
    
