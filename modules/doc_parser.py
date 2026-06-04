import easyocr
import fitz
import io
from PIL import Image

# إعداد الـ Reader للغة العربية والإنجليزية (بيحمل الموديل مرة واحدة)
reader = easyocr.Reader(['ar', 'en'])

def extract_text(pdf_file):
    text = ""
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    for page in doc:
        page_text = page.get_text()
        if page_text.strip():
            text += page_text + "\n"
        else:
            # استخدام EasyOCR بدل Tesseract
            pix = page.get_pixmap()
            img_bytes = pix.tobytes()
            results = reader.readtext(img_bytes, detail=0)
            text += "\n".join(results) + "\n"
            
    return text