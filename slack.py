import requests
import json

#URL #https://hooks.slack.com/services/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
webhook_url = "https://hooks.slack.com/services/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"

def send_message():
    message = {
        "text": "Hola para todos"
    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(message))
    
    if response.status_code == 200:
        print("Mensaje enviado correctamente")
    else:
        print(f"Error al enviar el mensaje: {response.status_code}, {response.text}")

send_message()
