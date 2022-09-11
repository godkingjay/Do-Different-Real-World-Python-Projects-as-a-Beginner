import pyttsx3

# create an object
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

text = input("Enter your text: ")
Speak(text)

# SAMPLE TEXT:
# “Imagine jumping out of a skydiving plane and discovering your parachute doesn’t work. What memories would flash before you? Now imagine the parachute opened. How differently would you act when you landed?” (ypo.org)