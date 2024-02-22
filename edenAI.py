import requests
import json

url = "https://api.edenai.run/v2/text/chat"
messages = []


def call_EDEN(message):
    if message:
        messages.append({"role": "user", "message": message})
        payload = {
            "response_as_dict": True,
            "attributes_as_list": False,
            "show_original_response": False,
            "temperature": 0.5,
            "max_tokens": 100,
            "previous_history": messages,
            "providers": "openai"
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzJkZTIyMjUtMmU4Zi00M2RlLTgxZTQtOGVhOTMyZjFhOTAzIiwidHlwZSI6ImFwaV90b2tlbiJ9.08apr4KdYl3PUuCA-M_A40_cwPlb7PP2oB3iCrpQbMA"
        }
        response = requests.post(url, json=payload, headers=headers)
        output = json.loads(response.text)
        reply = output["openai"]["generated_text"]
        messages.append({"role": "user", "message": reply})
        return reply

def chat():
    while True:
        prompt = input('Ingresa un prompt: ')
        if prompt == 'exit':
            break
        else:
            messages.append({"role": "user", "message": prompt})
            message = call_EDEN(prompt)
            messages.append({'role': 'user', 'message': message})
            print(message)

#chat()

print(call_EDEN('Hola'))