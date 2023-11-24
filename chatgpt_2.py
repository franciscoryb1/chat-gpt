import openai

key = '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'

def chatgpt(api_key):
    openai.api_key = api_key
    chat_history = []
    total_tokens_usage = 0
    while True:
        prompt = input('Ingresa un prompt:')
        if prompt == 'exit':
            break
        else:
            chat_history.append({'role': 'user', 'content': prompt})

            completion = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=chat_history,
                temperature=0.8,
                max_tokens=10
            )
            print(completion)
            usage = completion.usage["total_tokens"]
            mensaje = completion.choices[0]['message']['content']
            chat_history.append({'role': 'assistant', 'content': mensaje})
            #print(mensaje)
            #print('total tokens:', usage)
            return mensaje, usage

ch = chatgpt(key)
mensaje = ch[0]
usage = ch[1]
print(f'mensaje: {mensaje}')
print(f'uso: {usage}')