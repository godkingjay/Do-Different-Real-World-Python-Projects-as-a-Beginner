import pyttsx3

# create an object
engine = pyttsx3.init()

for voice in engine.getProperty("voices"):
    print(voice)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def Speak(Audio):
    engine.say(Audio)
    engine.runAndWait()

text = input("Enter your text: ")
Speak(text)