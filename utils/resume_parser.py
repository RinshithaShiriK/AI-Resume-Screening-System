from pdfminer.high_level import extract_text as pdf_extract_text

def extract_text(file_path):

    text = pdf_extract_text(file_path)

    return text