import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Text to speak
while True:
    text = "I'm in a punchy mood!!"

    # Convert text to speech
    engine.say(text)

    # Wait for the speaking to finish
    engine.runAndWait()
    print("done")

    time.sleep(2)