from model.messageModel import MessageModel
from model.connection import Connection

class MessageView:
    def __init__(self):
        pass


    def input_message(self):
        author = input("Enter your name: ")
        content = input("Enter your message: ")
        model = messageModel()
        model.write_message(author,content)

    def display_message(self):
        model.get_message()
