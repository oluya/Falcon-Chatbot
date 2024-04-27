def validate_text(text):
    if not text.strip():
        return "Text input cannot be empty."
    if len(text) > 500:
        return "Text input is too long. Please limit to 500 characters."
    return None
