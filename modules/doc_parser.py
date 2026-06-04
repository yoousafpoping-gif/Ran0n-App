import pytesseract
import sys
import fitz  # مكتبة pymupdf
import io
from PIL import Image

# إعداد ذكي لمسار Tesseract
if sys.platform.startswith('win'):
    # مسار الـ Tesseract على جهازك (ويندوز)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
else:
    # على سيرفر Streamlit (لينكس)، النظام بيعرفه أوتوماتيك
    pass

def extract_text(pdf_file):
    """دالة لاستخراج النص من الـ PDF مع دعم الـ OCR للصور"""
    text = ""
    # تحويل الملف المرفوع لمسار يمكن لـ fitz قراءته
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    for page in doc:
        # محاولة استخراج النص العادي
        page_text = page.get_text()
        if page_text.strip():
            text += page_text + "\n"
        else:
            # لو الصفحة صورة، نستخدم الـ OCR
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            text += pytesseract.image_to_string(img, lang='ara+eng') + "\n"
            
    return text