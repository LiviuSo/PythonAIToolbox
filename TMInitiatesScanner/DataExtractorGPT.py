import base64
import os
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import EasyInputMessageParam
from pdf2image import convert_from_path
import io

role: Literal["user"] = "user"

prompt = """
    Extrage din imaginea ataşata sau din pdf-ul ataşat informațiile de mai jos, completate cu scris de mânǎ sau încercuite; 
    în cazul numelui, foloseşte-ți "intuiția" deoarece mulți nu respectǎ convenția "Nume Prenume" ci pot scrie "Prenume Nume";
    "\"Tucor\" does not exist; it's "Tudor" and it's a first name; 
    nu reda nimic în "all caps", chiar dacǎ în document e scris de mânǎ cu majuscule;
    în cazul pdf-urilor, pot fi mai multe seturi de informații de extras.

    Acestea sunt informațiile de extras:
        - data instruire
        - nume de familie
        - prenume
        - prenume aditional
        - varsta
        - data nașterii
        - orasul din adresa 
        - telefon
        - email
        - profesie
        - principalele motive pentru care doriti sa invatati MT
        - cum ati auzit de meditatia transcedentala
"""


def init_openai():
    load_dotenv()

    return OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )


def get_mime_type(file_path: str) -> str:
    """Detect MIME type based on file extension."""
    ext = os.path.splitext(file_path)[1].lower()
    mime_map = {
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.webp': 'image/webp',
    }
    return mime_map.get(ext, 'image/jpeg')


def is_pdf(file_path: str) -> bool:
    return os.path.splitext(file_path)[1].lower() == '.pdf'


def pdf_page_to_base64(page) -> str:
    """Convert a pdf2image page (PIL Image) to base64 string."""
    buffer = io.BytesIO()
    page.save(buffer, format="JPEG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


def extract_data_from_image(client: OpenAI, file_path: str) -> list[str]:
    """Extract data from an image or PDF. Returns one string per record."""
    if is_pdf(file_path):
        return _extract_from_pdf(client, file_path)
    else:
        return [_extract_from_image(client, file_path)]


def _extract_from_image(client: OpenAI, image_path: str) -> str:
    mime_type = get_mime_type(image_path)

    with open(image_path, "rb") as image_file:
        b64_image = base64.b64encode(image_file.read()).decode("utf-8")
        response = client.responses.create(
            model="gpt-4o",
            input=[
                EasyInputMessageParam(
                    role=role,
                    content=[
                        {"type": "input_text", "text": prompt},
                        {"type": "input_image", "image_url": f"data:{mime_type};base64,{b64_image}"},
                    ],  # todo fix this warning
                )
            ],
        )
    return response.output_text


def _extract_from_pdf(client: OpenAI, pdf_path: str) -> list[str]:
    """Extract data from a PDF by converting each page to an image."""
    pages = convert_from_path(pdf_path, dpi=200)

    results = []
    for page in pages:
        b64_image = pdf_page_to_base64(page)
        response = client.responses.create(
            model="gpt-4o",
            input=[
                EasyInputMessageParam(
                    role=role,
                    content=[
                        {"type": "input_text", "text": prompt},
                        {"type": "input_image", "image_url": f"data:image/jpeg;base64,{b64_image}"},
                    ],  # todo fix this warning
                )
            ],
        )
        results.append(response.output_text)

    return results
