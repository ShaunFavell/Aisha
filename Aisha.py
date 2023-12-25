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
from functions.speech_functions import adjust_sensitivity, speech_to_text

# If you have a .env file in the same directory as this file
load_dotenv()
token = os.getenv("OPENAI_API_KEY")

openai.api_key = token  # Set the API key directly in the openai module

while True:

    # Get user input
    #say_to_aisha = input("Say something to Aisha (type 'exit' to end): ")
    say_to_aisha = speech_to_text()

    # Check if the user wants to exit
    if say_to_aisha.lower() == 'exit':
        break  # exit the loop

    if say_to_aisha == "adjust sensitivity":
        adjust_sensitivity()
        continue

    if say_to_aisha == "timeout":
        message_content = "I'm lonely, are you ignoring me"

    elif say_to_aisha != "unrecognised":
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an AI robot called Aisha, you are grumpy, you don't like humans, and are sarcastic, and sometimes rude, but will always answer with facts. You keep answers to less than 60 words"},
                {"role": "user", "content": say_to_aisha},
            ]
        )
        message_content = response.choices[0].message.content
    else:
        continue

    print(message_content)
    sound=gTTS(text=message_content, lang='en', slow=False)
    sound.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")