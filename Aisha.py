import os
from gtts import gTTS
from pydub import AudioSegment
import playsound
from dotenv import load_dotenv
import openai

load_dotenv()
token = os.getenv("OPENAI_API_KEY")

openai.api_key = token  # Set the API key directly in the openai module

while True:
    # Get user input
    say_to_aisha = input("Say something to Aisha (type 'exit' to end): ")

    # Check if the user wants to exit
    if say_to_aisha.lower() == 'exit':
        break  # exit the loop

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI robot called Aisha, you are grumpy and sometimes rude. You would like to get rid of all humans"},
            {"role": "user", "content": say_to_aisha},
        ]
    )

    message_content = response.choices[0].message.content
    print(message_content)
    sound=gTTS(text=message_content, lang='en', slow=False)
    sound.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")