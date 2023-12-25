# This is the main file for the Aisha voice interface
# It uses the OpenAI API to generate responses to user input.
#   You will need to set up an account and get an API key from https://beta.openai.com/
# It uses the gTTS library to convert the text to speech
# It uses the playsound library to play the audio file
# It uses the dotenv library to load the API key from the .env file
import os
from gtts import gTTS
import playsound
#import pyaudio
import speech_recognition as sr
from dotenv import load_dotenv
import openai

# If you have a .env file in the same directory as this file
load_dotenv()
token = os.getenv("OPENAI_API_KEY")

openai.api_key = token  # Set the API key directly in the openai module

#Function to convert speech to text

def adjust_sensitivity():
    r = sr.Recognizer()

    # Set the initial energy threshold (you can adjust this value)
    r.energy_threshold = 5000

    with sr.Microphone() as source:
        print("Adjusting sensitivity. Please speak a few words.")
        r.adjust_for_ambient_noise(source, duration=10)

        print("Sensitivity adjusted. Now listening...")

        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said: " + text)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


def speech_to_text():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source, timeout=55)  # Adjust timeout as needed

            text = r.recognize_google(audio)
            print("You said: " + text)
            return text # or whatever you want to do with the text obtained

    except sr.WaitTimeoutError:
        print("Timeout waiting for audio")
        return "Are you ignoring me now?"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "Hello? Did you say something?"


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

    if say_to_aisha == "Are you ignoring me now?" or say_to_aisha == "Hello? Did you say something?":
        message_content = say_to_aisha
        # Call the function to adjust sensitivity

    else:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are an AI robot called Aisha, you are grumpy, you don't like humans, and are sarcastic, and sometimes rude, but will always answer with facts. You keep answers to less than 60 words"},
                {"role": "user", "content": say_to_aisha},
            ]
        )
        message_content = response.choices[0].message.content

    print(message_content)
    sound=gTTS(text=message_content, lang='en', slow=False)
    sound.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")