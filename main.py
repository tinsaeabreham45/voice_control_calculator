import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def get_voice_input():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Input: " + text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand. Please try again.")
            return ""


def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error: Invalid expression"


def speak(text):
    engine.say(text)
    engine.runAndWait()


while True:
    speak("Please speak your calculation.")
    expression = get_voice_input()
    if expression.lower() == "exit":
        speak("Calculator is shutting down.")
        break
    result = calculate(expression)
    speak("The result is " + str(result))



