# This is the main file for the Aisha voice interface
# It uses the OpenAI API to generate responses to user input.
#   You will need to set up an account and get an API key from https://beta.openai.com/
# It uses the gTTS library to convert the text to speech
# It uses the playsound library to play the audio file
# It uses the dotenv library to load the API key from the .env file

import os
from gtts import gTTS
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
            {"role": "system", "content": "You are an AI robot called Aisha, you are grumpy and sometimes rude, but will always answer with facts"},
            {"role": "user", "content": say_to_aisha},
        ]
    )

    message_content = response.choices[0].message.content
    print(message_content)
    sound=gTTS(text=message_content, lang='en', slow=False)
    sound.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")