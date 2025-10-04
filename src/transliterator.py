# src/transliterator.py
# Core Logic using EasyOCR (FREE OCR) and Indic-Transliteration

import easyocr
from indic_transliteration import sanscript, detect
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate 
from PIL import Image
import io

# Initialize EasyOCR Reader once (loads models into memory)
# We prioritize 'en' (English) for numbers/Latin text and 'hi' (Hindi/Devanagari) 
# as the common Indic script for street signs. Add more codes as needed (e.g., 'bn', 'ta').
# This is a robust, local, and free solution.
try:
    READER = easyocr.Reader(['en', 'hi']) 
except Exception as e:
    # Handle cases where EasyOCR setup fails (e.g., missing PyTorch components)
    READER = None
    print(f"WARNING: EasyOCR initialization failed. OCR functions will fail. Error: {e}")


def detect_and_extract_text(image_bytes):
    """
    Uses EasyOCR to detect and extract text from an image.
    
    Args:
        image_bytes: Raw bytes of the uploaded image file (from Streamlit).
    
    Returns:
        A dictionary with the combined extracted text and a status message.
    """
    if READER is None:
        return {"full_text": None, "lang_code": "OCR Engine Not Initialized (Setup Failure)"}

    try:
        # Load image from bytes using Pillow
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        
        # Perform OCR, setting detail=0 to return only the text strings
        results = READER.readtext(image, detail=0) 
        
        # Combine all detected text into a single string, separated by newlines
        full_text = "\n".join(results)
        
        return {
            "full_text": full_text.strip() if full_text else None,
            "lang_code": "EasyOCR (en, hi) Engine" # Status message
        }

    except Exception as e:
        return {"full_text": None, "lang_code": f"EasyOCR Execution Error: {e}"}


def transliterate_text(text, target_scheme):
    """
    Detects the source Indic script and transliterates the text to the target scheme.
    
    Args:
        text (str): The text string extracted by OCR.
        target_scheme (sanscript.Scheme): The user-selected target script.
    
    Returns:
        dict: Containing the transliterated result, source script name, and error status.
    """
    try:
        # 1. Detect the most likely source script
        source_scheme = detect.detect(text)
        
        # Guard clause: If the text is Latin/Roman, return it as is
        if source_scheme == sanscript.HK or source_scheme == sanscript.IAST:
             return {
                 "result": text, 
                 "source_script": "Roman (Latin / English)", 
                 "error": None
             }
        
        # 2. Perform the script-to-script conversion
        transliterated_text = transliterate(
            data=text, 
            # SchemeMap handles the conversion between two specific schemes
            sch_map=SchemeMap(SCHEMES[source_scheme], SCHEMES[target_scheme])
        )
        
        return {
            "result": transliterated_text, 
            "source_script": str(source_scheme),
            "target_script": str(target_scheme),
            "error": None
        }
        
    except Exception as e:
        # Catch errors from the transliteration process
        return {
            "result": None, 
            "source_script": None, 
            "target_script": None, 
            "error": f"Transliteration Error: {e}"
        }