from BRAIN.parser import parser

while True:
    text = input("You: ")

    if text == "exit":
        break

    print(parser.parse(text))