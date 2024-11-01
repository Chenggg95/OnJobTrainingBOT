import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


if load_dotenv('.env'):
   # for local development
   OPENAI_KEY = os.getenv('OPENAI_API_KEY')
else:
   OPENAI_KEY = st.secrets['OPENAI_API_KEY']

# Pass the API Key to the OpenAI Client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                base_url="https://litellm.govtext.gov.sg/",
                default_headers={"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0"}
                )



# Note that this function directly take in "messages" as the parameter.
def get_completion_by_messages(messages, model="gpt-4o-prd-gcc2-lb", temperature=0, top_p=1, max_tokens=1024):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


