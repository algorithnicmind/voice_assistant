# interaction.py
from groq import Groq
from backend.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(prompt):
    try:
        chat_completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": prompt}]
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print(f"❌ Error while querying Groq: {e}")
        return "Sorry, I couldn't get a response from Groq."
