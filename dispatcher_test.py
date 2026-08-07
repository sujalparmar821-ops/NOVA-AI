from BRAIN.dispatcher import dispatcher

while True:

    command = input("Command: ")

    if command == "exit":
        break

    if dispatcher.dispatch(command):
        print("Executed.")
    else:
        print("Unknown command.")