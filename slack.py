import streamlit as st
import requests
import json

def send_message_to_slack(message):
    webhook_url = "https://hooks.slack.com/services/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"
    payload = {"text": message}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        st.success("Mensaje enviado correctamente a Slack")
    else:
        st.error(f"Error al enviar el mensaje: {response.status_code}, {response.text}")

# Interfaz de usuario con Streamlit
st.title("Enviar mensaje a Slack")
message = st.text_area("Escribe tu mensaje", "Hola para todos")

if st.button("Enviar mensaje"):
    send_message_to_slack(message)
