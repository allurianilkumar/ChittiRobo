import subprocess

def speak(text):
    subprocess.run(['festival', '--tts'], input=text.encode('utf-8'))

def explain_class():
    explanation = (
        "A class is a blueprint for creating objects. "
        "It defines attributes and methods that the created objects will have. "
        "For example, a Dog class might have a name attribute and a bark method."
    )
    speak(explanation)

def explain_method():
    explanation = (
        "Methods are functions defined inside a class that operate on instances of that class. "
        "They can access the object's attributes and perform actions. "
        "For instance, the bark method in the Dog class returns a string."
    )
    speak(explanation)

if __name__ == "__main__":
    explain_class()
    explain_method()
