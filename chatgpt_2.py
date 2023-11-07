import openai

openai.api_key = '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'

completion = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": "hi"}],
    max_tokens=100,
    stream=True
)

for part in completion:
    print(part.choices[0]['delta']['content'])