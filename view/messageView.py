from model.messageModel import MessageModel

class MessageView:
    def __init__(self):
        self.vm = MessageModel()


    def input_message(self):
        author = input("Enter your name: ")
        content = input("Enter your message: ")
        self.vm.write_message(author,content)

    def display_message(self):
        view = self.vm.get_message()
        for element in view:
            print(f"Voici le message de {element['author']} datant du {element[2]}: {element[1]}")
