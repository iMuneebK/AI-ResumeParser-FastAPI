import PyPDF2
import docx
from io import BytesIO

def extract_text_from_pdf(file_bytes):
    reader = PyPDF2.PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_bytes):
    doc = docx.Document(BytesIO(file_bytes))
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def parse_document(filename, file_bytes):
    if filename.endswith('.pdf'):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith('.docx'):
        return extract_text_from_docx(file_bytes)
    return str(file_bytes)
