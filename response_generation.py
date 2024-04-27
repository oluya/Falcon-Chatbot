from PIL import Image
def generate_response(history, text, img, txt_model, vis_model, default_prompt="You are FALCON AI, falcon pest control chatbot. Answer only as a Pest Expert, decline anything outside this domain."):
    try:
        if img:
            img = Image.open(img)
            response = vis_model.generate_content([text, img])
            history.append((None, response.text))
        else:
            response = txt_model.generate_content([text])
            history.append((None, response.text))
        print("Response generated successfully.")
        return history
    except Exception as e:
        error_msg = f"Error processing your input: {str(e)}"
        print(error_msg)
        return [(error_msg, None)]
