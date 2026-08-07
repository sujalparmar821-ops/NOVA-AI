from BRAIN.wake_word import wake_word
from BRAIN.response import response

while True:
    text = input("You: ")

    if wake_word.detected(text):
        print("Wake Word Detected!")
        print(response.greeting())
    else:
        print("Waiting for wake word...")