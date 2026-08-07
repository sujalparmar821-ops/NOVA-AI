from COMMANDS.apps import apps

while True:

    app = input("App: ")

    if app == "exit":
        break

    if apps.open(app):
        print("Opened successfully.")
    else:
        print("App not supported.")