import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def explain_variable():
    explanation = (
        "In Python, a variable is used to store data values. "
        "For example, you can create a variable named 'x' and assign it the value of 10 like this: "
        "x equals 10. You can then use 'x' in your calculations."
    )
    speak(explanation)

def explain_function():
    explanation = (
        "A function is a block of code that only runs when it is called. "
        "You can pass data, known as parameters, into a function. "
        "Here's an example: define a function named 'greet' that prints 'Hello, World!'."
    )
    speak(explanation)

def main():
    print("Select a programming concept to hear about:")
    print("1: Variables")
    print("2: Functions")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        explain_variable()
    elif choice == '2':
        explain_function()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
