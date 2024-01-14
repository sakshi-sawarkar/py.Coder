import os
from openai import OpenAI


client = OpenAI(
    api_key='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',
)

 
def generate_text(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant who helps people in writing code."},
            {"role": "user", "content": f"write a code for {prompt}"},
        ],
        model="gpt-3.5-turbo",
    )
    response = chat_completion.choices[0].message.content
    return response

output = generate_text("sum of two numbers in python")
print(output)