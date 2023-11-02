from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


router = APIRouter()


templates = Jinja2Templates(directory='templates')

@router.get(
        '/',
        response_class=HTMLResponse
)
async def home(
    request: Request
):
    data = {
        "page": "I am developer"
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})


@router.get('/test', response_class=HTMLResponse)
async def test(
    request: Request
):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("test.html", {"request": request, "data": data})