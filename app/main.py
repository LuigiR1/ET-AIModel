from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.middleware.resume_parser import extract_text_from_resume
from app.middleware.keyword_matcher import match_keywords

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def process_form(request: Request, prompt: str = Form(...), resume: UploadFile = File(...)):
    # Extract text from the uploaded resume
    resume_text = await extract_text_from_resume(resume)

    # Check for keyword matches from the prompt
    result = match_keywords(prompt, resume_text)

    return templates.TemplateResponse("form.html", {"request": request, "response": result})
