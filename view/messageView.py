from model.messageModel import MessageModel

class MessageView:
    def __init__(self):
        vm = MessageModel()


    def input_message(self):
        self.author = input("Enter your name: ")
        self.content = input("Enter your message: ")
        self.write_message(self.author, self.content)
    
