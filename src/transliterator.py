# src/transliterator.py
# Core Logic for OCR and Transliteration

from google.cloud import vision
from indic_transliteration import sanscript 
# NOTE: We will import 'detect' and 'transliterate' in Phase C

# Initialize the Vision API client once
client = vision.ImageAnnotatorClient() 

def detect_and_extract_text(image_bytes):
    """
    Calls Google Vision API to extract text (OCR) from an image.
    """
    image = vision.Image(content=image_bytes)
    
    # Use document_text_detection for dense text like street signs
    response = client.document_text_detection(image=image)
    
    if not response.text_annotations:
        return {"full_text": None, "lang_code": None}

    full_text = response.text_annotations[0].description
    
    lang_code = None
    if response.context and response.context.language_hints:
        lang_code = response.context.language_hints[0]

    return {
        "full_text": full_text.strip(),
        "lang_code": lang_code
    }


def transliterate_text(text, target_scheme):
    """
    Placeholder for the indic-transliteration conversion logic (Phase C).
    """
    return {"result": None, "error": "NotImplemented"}