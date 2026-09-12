from fastapi import FastAPI, UploadFile, File
from parser import parse_document
from ner_model import CustomNER
from utils import extract_email, extract_phone
from skill_matcher import match_skills
from typing import List

app = FastAPI(title="AI Resume Parser API")
ner = CustomNER()

@app.post("/parse")
async def parse_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = parse_document(file.filename, content)
    entities = ner.extract_entities(text)
    email = extract_email(text)
    phone = extract_phone(text)
    
    return {
        "filename": file.filename,
        "email": email,
        "phone": phone,
        "skills": entities.get("skills", []),
        "entities": entities.get("extracted_entities", {})
    }

@app.post("/match")
async def match_resume_to_job(resume_skills: List[str], jd_skills: List[str]):
    return match_skills(resume_skills, jd_skills)
