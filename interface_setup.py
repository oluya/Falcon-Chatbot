import gradio as gr
import bcrypt
from input_processing import process_input
from database_storage import DatabaseManager
from response_generation import generate_response


def setup_interface(txt_model, vis_model):
    # user_db = UserStorage("users.db")
    db_manager = DatabaseManager()

    def register_user(username, password, email):
        # password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        response =  db_manager.insert_user(username, email, password)
        return response

    def login_user(username, password):
        # This function would need a real implementation to check the hashed password
        # For demonstration, it's left simple
        pass

    with gr.Blocks(css=".gr-textbox { resize: none; }") as app:
        with gr.Row():
            image_box = gr.Image(type="filepath", label="Upload Image (JPEG, PNG supported)")
            chatbot = gr.Chatbot(scale=2, height=600)

        # The Text input code section.
        text_box = gr.Textbox(placeholder="Enter text and press enter, or upload an image", label="Enter Text (Max 500 characters)")
        submit_btn = gr.Button("Submit")

        
        def handle_submission(history, txt, img):
            output = process_input(history, txt, img)
            generate_response(history, txt, img, txt_model, vis_model)
            return history, "", None  # Clear text and image after submission

        submit_btn.click(
            handle_submission,
            inputs=[chatbot, text_box, image_box],
            outputs=[chatbot, text_box, image_box]
        )

    return app
