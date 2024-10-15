import pyttsx3

engine = pyttsx3.init()
text = "Hello, how are you?Choose the one that fits your needs best! If you have any specific questions or need further examples, feel free to ask!"
engine.say(text)
engine.runAndWait()
