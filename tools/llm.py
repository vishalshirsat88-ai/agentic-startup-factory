from dotenv import load_dotenv
import os

load_dotenv()

import os
from groq import Groq

LLM_PROVIDER = "groq"

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate(prompt):

    if LLM_PROVIDER == "groq":

        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama3-70b-8192"
        )

        return chat_completion.choices[0].message.content

    return "No LLM provider configured."