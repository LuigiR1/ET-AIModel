from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import tempfile
from fastapi import UploadFile

async def extract_text_from_resume(resume: UploadFile) -> str:
    content = await resume.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{resume.filename.split('.')[-1]}") as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    if resume.filename.endswith(".pdf"):
        return extract_pdf_text(tmp_path)
    elif resume.filename.endswith(".docx"):
        return extract_text_from_docx(tmp_path)
    else:
        return "Unsupported file type."

def extract_text_from_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])
