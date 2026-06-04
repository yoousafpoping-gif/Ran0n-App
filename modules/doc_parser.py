import easyocr
import fitz  # مكتبة pymupdf
import io
from PIL import Image

# إعداد الـ Reader (سيتم تحميل الموديلات أول مرة فقط)
reader = easyocr.Reader(['ar', 'en'])

def extract_text(pdf_file):
    text = ""
    # نستخدم ملف الـ PDF اللي جاي من الـ Upload
    pdf_bytes = pdf_file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    for page in doc:
        # استخراج النص العادي أولاً
        page_text = page.get_text()
        if page_text and page_text.strip():
            text += page_text + "\n"
        else:
            # لو الصفحة صورة، نستخدم EasyOCR
            pix = page.get_pixmap()
            img_bytes = pix.tobytes()
            # القراءة باستخدام EasyOCR
            results = reader.readtext(img_bytes, detail=0)
            text += "\n".join(results) + "\n"
            
    return text