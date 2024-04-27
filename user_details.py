import gradio as gr
import bcrypt
from database_storage import DatabaseManager

def userauth_interface():
    db_manager = DatabaseManager()

    def register_user(username, password, email):
        response = db_manager.insert_user(username, email, password)
        return response

    def login_user(username, password):
        if db_manager.validate_user(username, password):
            return "Login successful", "default"  # Second parameter is the CSS class for success
        else:
            return "Invalid username or password", "error"  # CSS class for error

    with gr.Blocks(css=".gr-textbox { resize: none; }") as app:
        with gr.Row():
            username_input = gr.Textbox(label="Username", placeholder="Enter your username")
            password_input = gr.Textbox(label="Password", placeholder="Enter your password", type="password")
            email_input = gr.Textbox(label="Email", placeholder="Enter your email", type="email")
            submit_register_btn = gr.Button("Register")
            registration_feedback = gr.Label()

        with gr.Row():
            login_username_input = gr.Textbox(label="Username", placeholder="Enter your username")
            login_password_input = gr.Textbox(label="Password", placeholder="Enter your password", type="password")
            login_btn = gr.Button("Login")
            login_feedback = gr.Label()

        submit_register_btn.click(
            register_user,
            inputs=[username_input, password_input, email_input],
            outputs=[registration_feedback]
        )

        login_btn.click(
            login_user,
            inputs=[login_username_input, login_password_input],
            outputs=[login_feedback]
        )

    return app
