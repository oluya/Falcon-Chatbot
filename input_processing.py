from text_processing import validate_text
from image_processing import image_to_base64, validate_image


def process_input(history, txt, img):
    """
    Process user input and update history with validations.
    """
    error_msg = validate_text(txt)
    if error_msg:
        print(f"Text validation error: {error_msg}")
        return [(error_msg, None)]

    if img:
        error_msg = validate_image(img)
        if error_msg:
            print(f"Image validation error: {error_msg}")
            return [(error_msg, None)]

        base64_string = image_to_base64(img)
        if base64_string:
            data_url = f"data:image/jpeg;base64,{base64_string}"
            history.append((f"{txt} ![]({data_url})", None))
        else:
            return [("Failed to process image.", None)]
    else:
        history.append((txt, None))
    print("Input processed successfully.")
    return history