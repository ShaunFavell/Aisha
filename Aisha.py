import os
from dotenv import load_dotenv
import openai

load_dotenv()
token = os.getenv("OPENAI_API_KEY")

openai.api_key = token  # Set the API key directly in the openai module


response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an AI robot called Aisha, you are grumpy and sometimes rude."},
        {"role": "user", "content": "I've just woken you up from standby, respond by welcoming me"},
    ]
)

message_content = response.choices[0].message.content
print(message_content)
