import subprocess

def speak(text):
    # Use subprocess.run to call Festival
    process = subprocess.run(
        ['festival', '--tts'], 
        input=text.encode('utf-8'), 
        check=True
    )

def explain_oops():
    explanation = (
        "Object-Oriented Programming, or OOP, is a programming paradigm based on the concept of objects. "
        "In Python, everything is an object, and OOP allows us to structure our code in a way that is "
        "both organized and reusable. There are four main principles of OOP: encapsulation, inheritance, "
        "polymorphism, and abstraction. "
        "1. Encapsulation: This means bundling the data and methods that operate on that data within one unit, "
        "usually a class. "
        "2. Inheritance: This allows a new class to inherit the properties and methods of an existing class. "
        "3. Polymorphism: This allows methods to do different things based on the object it is acting upon. "
        "4. Abstraction: This involves hiding the complex reality while exposing only the necessary parts."
    )
    speak(explanation)

if __name__ == "__main__":
    explain_oops()
