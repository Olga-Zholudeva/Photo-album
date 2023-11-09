from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def test(request: Request):
    """Обрабочик запросов к стартовой странице."""
    data = {"page": "Home page"}
    return templates.TemplateResponse("home.html", {"request": request, "data": data})
