# src/transliterator.py
# Core Logic using Pytesseract (FREE OCR) and Indic-Transliteration

import pytesseract
from PIL import Image
import io
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate 

# NOTE: Tesseract must be available on the system (handled by packages.txt in cloud).
# You may need to manually set the path here for local testing:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def detect_and_extract_text(image_bytes):
    """
    Uses Pytesseract to detect and extract text from an image, specifically enabling Indic language support.
    
    Args:
        image_bytes: Raw bytes of the uploaded image file.
    
    Returns:
        A dictionary with the combined extracted text.
    """
    try:
        # Load image from bytes using Pillow
        image = Image.open(io.BytesIO(image_bytes))
        
        # Perform OCR using Hindi ('hin') and English ('eng') language packs.
        # Streamlit Cloud's packages.txt ensures Tesseract is installed with these packs.
        full_text = pytesseract.image_to_string(image, lang='hin+eng')
        
        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "Tesseract (hin+eng)" # Status message
        }

    except pytesseract.TesseractNotFoundError:
        return {"full_text": None, "lang_code": "Tesseract not found (Cloud configuration error)."}
    except Exception as e:
        return {"full_text": None, "lang_code": f"Tesseract Execution Error: {e}"}


def transliterate_text(text, target_scheme):
    """
    Detects the source Indic script and transliterates the text to the target scheme.
    """
    try:
        source_scheme = detect.detect(text)
        
        if source_scheme == sanscript.HK or source_scheme == sanscript.IAST:
             return {
                 "result": text, 
                 "source_script": "Roman (Latin / English)", 
                 "error": None
             }
        
        transliterated_text = transliterate(
            data=text, 
            sch_map=SchemeMap(SCHEMES[source_scheme], SCHEMES[target_scheme])
        )
        
        return {
            "result": transliterated_text, 
            "source_script": str(source_scheme),
            "target_script": str(target_scheme),
            "error": None
        }
        
    except Exception as e:
        return {
            "result": None, 
            "source_script": None, 
            "target_script": None, 
            "error": f"Transliteration Error: {e}"
        }