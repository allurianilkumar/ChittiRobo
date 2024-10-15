import speech_recognition as sr
import subprocess


def speak(text):
    subprocess.run(['festival', '--tts'], input=text.encode('utf-8'))

def voice_to_text():
    # Create a recognizer instance
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something:")
        # Adjust for ambient noise and record audio
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Use Google Web Speech API to recognize the audio
        text = recognizer.recognize_google(audio)
        speak(text)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    voice_to_text()
