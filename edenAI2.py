import json
import requests

url = "https://api.edenai.run/v2/text/chat"
chat_history = []

def chat():
    url = "https://api.edenai.run/v2/text/chat"
    chat_history = []
    while True:
        prompt = input('Ingresa un prompt: ')
        if prompt == 'exit':
            break
        else:
            chat_history.append({"role": "user", "message": prompt})
            payload = {
                "response_as_dict": True,
                "attributes_as_list": False,
                "show_original_response": False,
                "temperature": 0.5,
                "max_tokens": 100,
                "previous_history": chat_history,
                "providers": "openai"
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzJkZTIyMjUtMmU4Zi00M2RlLTgxZTQtOGVhOTMyZjFhOTAzIiwidHlwZSI6ImFwaV90b2tlbiJ9.08apr4KdYl3PUuCA-M_A40_cwPlb7PP2oB3iCrpQbMA"
            }

            response = requests.post(url, json=payload, headers=headers)
            output = json.loads(response.text)
            mensaje = output["openai"]["generated_text"]
            chat_history.append({'role': 'assistant', 'message': mensaje})
            print(mensaje)

chat()