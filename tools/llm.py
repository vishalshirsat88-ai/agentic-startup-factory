from dotenv import load_dotenv
import os
import time
from groq import Groq

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

# Initialize Groq client
client = Groq(api_key=api_key)


def generate(prompt):
    for attempt in range(3):
        try:
            chat_completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
            )

            return chat_completion.choices[0].message.content

        except Exception as e:
            if "rate_limit" in str(e):
                print("⏳ Rate limit hit, retrying in 7 sec...")
                time.sleep(7)
            else:
                print("❌ LLM ERROR:", e)
                raise e
