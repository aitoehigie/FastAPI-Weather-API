import fastapi
from fastapi import FastAPI, Request, Response, Query, Path, Body
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, PlainTextResponse

templates = Jinja2Templates(directory="templates")

router = fastapi.APIRouter()

@router.get("/", include_in_schema=False)
async def index(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})


