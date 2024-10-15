import TTS

def text_to_speech(text):
    # Initialize the TTS
    tts = TTS.TTS()

    # Generate speech
    tts.tts_to_file(text=text, file_path="output.wav")

if __name__ == "__main__":
    text = "Hello, this is a text to speech example using the TTS library."
    text_to_speech(text)
