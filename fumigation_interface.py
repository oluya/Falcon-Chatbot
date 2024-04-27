import gradio as gr
from fumigation_db import FumigationDB
from datetime import datetime

def setup_fumigation_interface():
    db = FumigationDB()

    def add_appointment(customer_name, service_type, appointment_date, notes=''):
        try:
            # Here you might want to validate the date format or convert it to a datetime object
            # datetime.strptime(appointment_date, '%Y-%m-%d') could be used if the format is guaranteed
            db.add_appointment(customer_name, service_type, appointment_date, notes)
            return "Appointment successfully added!"
        except Exception as e:
            return f"Failed to add appointment: {str(e)}"

    def list_appointments():
        appointments = db.get_appointments()
        return '\n'.join([f"{row['customer_name']} - {row['service_type']} on {row['appointment_date']}" for row in appointments])

    with gr.Blocks() as app:
        with gr.Row():
            customer_name = gr.Textbox(label="Customer Name")
            service_type = gr.Textbox(label="Service Type")
            appointment_date = gr.Textbox(label="Appointment Date", placeholder="YYYY-MM-DD")  # Use this for date input
            notes = gr.Textarea(label="Additional Notes (optional)")  # Use this for multiline input
            submit_btn = gr.Button("Schedule Appointment")
        
        output = gr.Label()
        submit_btn.click(
            add_appointment,
            inputs=[customer_name, service_type, appointment_date, notes],
            outputs=output
        )

        list_appointments_btn = gr.Button("List Appointments")
        appointments_output = gr.Label()
        list_appointments_btn.click(
            list_appointments,
            inputs=[],
            outputs=appointments_output
        )

    return app