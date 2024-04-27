import gradio as gr
from api_config import configure_api
import google.generativeai as genai
from interface_setup import setup_interface
from user_details import userauth_interface
from fumigation_interface import setup_fumigation_interface

def main():
    configure_api()
    txt_model = genai.GenerativeModel('gemini-pro')
    vis_model = genai.GenerativeModel('gemini-pro-vision')

    with gr.Blocks() as app:
        with gr.Tab("Main Interface"):
            setup_interface(txt_model, vis_model)
        # with gr.Tab("User Authentication"):
        #     userauth_interface()(app)
        # with gr.Tab("Fumigation Services"):
        #     setup_fumigation_interface()(app)

    app.launch()

if __name__ == "__main__":
    main()
