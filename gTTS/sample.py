from gtts import gTTS
import os

text = "Hello, how are you?"
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

# Play the audio (optional)
os.system("start output.mp3")  # Use 'afplay' on macOS or 'xdg-open' on Linux
