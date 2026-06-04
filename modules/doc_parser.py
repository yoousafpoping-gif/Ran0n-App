import fitz
import pytesseract
from PIL import Image
import io

# مسار الـ OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            text = page.get_text()
            if len(text.strip()) < 100:
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                text = pytesseract.image_to_string(img, lang='ara+eng')
            full_text += text + "\n"
        return full_text
    except Exception as e:
        return f"خطأ: لم نتمكن من قراءة الملف. التفاصيل: {e}"