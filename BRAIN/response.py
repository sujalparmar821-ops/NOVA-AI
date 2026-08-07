"""
BRAIN/response.py
-----------------
Common responses used by NOVA.
"""


class Response:

    def greeting(self):
        return "Yes? How can I help you?"

    def unknown_command(self):
        return "Sorry, I don't know how to do that yet."

    def goodbye(self):
        return "Goodbye. Have a great day!"


response = Response()