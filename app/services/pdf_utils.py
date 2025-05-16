from io import BytesIO
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

def extract_text_from_pdf(file_bytes) -> str:
    pdf_stream = BytesIO(file_bytes)    # Wrap bytes into a file-like object
    pdf = PdfReader(pdf_stream)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""
    return text

def chunk_text(text: str):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(text)

