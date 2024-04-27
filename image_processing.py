from PIL import Image
import base64

cache = {}  # Cache for storing base64 encoded images

def image_to_base64(image_path):
    if image_path in cache:
        return cache[image_path]
    try:
        with open(image_path, 'rb') as img:
            encoded_string = base64.b64encode(img.read()).decode('utf-8')
        cache[image_path] = encoded_string
        return encoded_string
    except Exception as e:
        print(f"Error encoding image: {str(e)}")
        return None

def validate_image(image_path):
    try:
        with Image.open(image_path) as img:
            img.verify()
        print("Image validated successfully.")
        return None
    except Exception as e:
        print(f"Invalid image file: {str(e)}")
        return f"Invalid image file: {str(e)}"
