import openai
import os
import platform

openai.api_key = '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'

#def cls():
#    os.system('cls' if os.name=='nt' else 'clear')

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


chat_history = []
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
            max_tokens=100
        )
        mensaje = completion.choices[0]['message']['content']
        chat_history.append({'role': 'assistant', 'content': mensaje})
        print(mensaje)

#chat_history = []
#while True:
#    prompt = input('Ingresa un prompt:')
#    if prompt == 'exit':
#        break
#    else:
#        chat_history.append({'role': 'user', 'content': prompt})
#
#        completion = openai.ChatCompletion.create(
#            model='gpt-3.5-turbo',
#            messages=chat_history,
#            temperature=0.8,
#            max_tokens=100,
#            stream=True
#        )
#
#        collected_messages = []
#
#        for chunk in completion:
#            chunk_message = chunk['choices'][0]['delta']
#            collected_messages.append(chunk_message)
#            full_reply_content = ''.join(m.get('content', '') for m in collected_messages)
#            print(full_reply_content)
#            os.system('cls')
#            #clear()
#            #print("\033[H\033[J", end="")
#
#        chat_history.append({'role': 'assistant', 'content': full_reply_content})
#        print(full_reply_content)

