import speech_recognition as sr

#Function to adjust sensitivity
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

#Function to convert speech to text
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
        return "timeout"
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "unrecognised"