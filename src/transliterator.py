# src/transliterator.py

from google.cloud import vision
# We need sanscript for defining target scripts later in app.py
from indic_transliteration.sanscript import sanscript 

# Initialize the Vision API client once
# This client automatically looks for the GOOGLE_APPLICATION_CREDENTIALS environment variable
client = vision.ImageAnnotatorClient() 

def detect_and_extract_text(image_bytes):
    """
    Calls Google Vision API to extract text (OCR) from an image.
    
    Args:
        image_bytes: Raw bytes of the uploaded image file.
    
    Returns:
        A dictionary with the extracted text and the detected language code.
    """
    image = vision.Image(content=image_bytes)
    
    # Use document_text_detection for dense text like street signs
    response = client.document_text_detection(image=image)
    
    # Check if any text was found
    if not response.text_annotations:
        return {"full_text": None, "lang_code": None}

    # The first annotation contains the entire extracted text
    full_text = response.text_annotations[0].description
    
    # Attempt to get the language code from the response context
    lang_code = None
    if response.context and response.context.language_hints:
        # The first hint is often the most confident language
        lang_code = response.context.language_hints[0]

    return {
        "full_text": full_text.strip(),
        "lang_code": lang_code
    }


# Placeholder for Phase B: Transliteration Logic (To be implemented later)
def transliterate_text(text, target_scheme):
    """Placeholder for the indic-transliteration conversion logic."""
    return {"result": None, "error": "NotImplemented"}