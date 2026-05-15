def chatbot():

    print(" Simple Chatbot")
    print("Type 'bye' to close the chatbot.\n")

    while True:

        user_message = input("You: ").lower()

        if user_message == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user_message == "how are you":
            print("Bot: I am fine, thank you!")

        elif user_message == "what is your name":
            print("Bot: I am a Python chatbot.")

        elif user_message == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

 
chatbot()