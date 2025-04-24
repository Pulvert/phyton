"""8-9. Messages: Make a list containing a series of short text messages. Pass the 
list to a function called show_messages(), which prints each text message."""

message_list = ["Vive la vida", "Protege a tu familia", "No seas envidioso"]

def print_messages(messages):
    for message in messages:
        print (message)


print_messages(message_list)


"""8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly."""

message_list = ["Vive la vida", "Protege a tu familia", "No seas envidioso"]
sent_messages = []


def move_messages(messages):
    while messages:
        mes = messages.pop()
        sent_messages.append(mes)


def print_messages():
    print(message_list)
    print(sent_messages)


move_messages(message_list)
print_messages()

"""8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function
send_messages() with a copy of the list of messages. After calling the function,
print both of your lists to show that the original list has retained its messages."""

message_list = ["Vive la vida", "Protege a tu familia", "No seas envidioso"]
sent_messages = []

def move_messages(messages):
    while messages:
        mes = messages.pop()
        sent_messages.append(mes)


def print_messages():
    print(message_list)
    print(sent_messages)


move_messages(message_list[:])
print_messages()