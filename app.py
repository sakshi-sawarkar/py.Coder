import streamlit as st
import os
from openai import OpenAI
client = OpenAI(
    api_key= st.secrets("KEY"),
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

st.title("Sakshi Bohot Roti Hai!!")

text = st.text_input("What do you want the code to do?")

if text:
    st.write(generate_text(text))

