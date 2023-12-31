import fastapi
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
templates = Jinja2Templates('templates')
router = fastapi.APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})