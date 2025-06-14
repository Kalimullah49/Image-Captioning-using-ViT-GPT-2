from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi import status
import shutil
import os
from .model import generate_caption

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "caption": None})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, file: UploadFile = File(...)):
    if not file:
        return templates.TemplateResponse("index.html", {"request": request, "caption": "No file uploaded."})
    filename = file.filename
    file_location = os.path.join(UPLOAD_DIR, filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    caption = generate_caption(file_location)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "caption": caption,
            "filename": filename
        }
    )
