from VOICE.listen import listener

while True:
    text = listener.listen()

    if text:
        print("Returned:", text)

    if text == "exit":
        break