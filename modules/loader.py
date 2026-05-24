from pypdf import PdfReader
import re


def load_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        content = page.extract_text()

        if content:
            text += content + " "

    # clean excessive whitespace/newlines
    text = re.sub(r'\s+', ' ', text)

    return text.strip()