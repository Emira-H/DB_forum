from view.messageView import MessageView

action = MessageView()

if __name__ == '__main__':

    choice_user = ""

while choice_user != 'q':
    choice_user = input("Veuillez taper A pour afficher les messages stockés, M pour écrire un message ou Q pour quitter ").lower()
    if choice_user == 'm':
        action.input_message()
    if choice_user == "a":
        action.display_message()
    if choice_user == 'q':
        exit()
