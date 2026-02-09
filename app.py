from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from model import generate_letter_body

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "letter": None}
    )

@app.post("/generate", response_class=HTMLResponse)
async def generate_letter(
    request: Request,
    from_name: str = Form(...),
    from_address: str = Form(...),
    to_name: str = Form(...),
    to_address: str = Form(...),
    reason: str = Form(...)
):
    letter_body = generate_letter_body(reason)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "letter": {
                "from_name": from_name,
                "from_address": from_address,
                "to_name": to_name,
                "to_address": to_address,
                "body": letter_body
            }
        }
    )
