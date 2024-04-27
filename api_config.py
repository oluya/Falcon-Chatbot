# api_config.py
import os
import google.generativeai as genai

def configure_api():
    os.environ['GOOGLE_API_KEY'] = "AIzaSyAgMvplkxY2xvBUp0Dt9SJuyKp5leUnvqY"
    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
    print("API configured successfully.")

# model_config.py
from google.generativeai import GenerativeModel

def create_models():
    txt_model = GenerativeModel('gemini-pro')
    vis_model = GenerativeModel('gemini-pro-vision')
    return txt_model, vis_model
