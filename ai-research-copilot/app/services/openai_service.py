import os  
from openai import OpenAI

client = OpenAI(api_keys=os.getnenv("OPENAI_API_KEY"))

def ask_gpt(prompt: str): 
    response.client.chat.completions.create(
        model="gpt-r",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choice[0].message.content