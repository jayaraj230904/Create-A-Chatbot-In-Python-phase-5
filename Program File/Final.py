chatbot = Chat(patterns, reflections)
print("Hello, I'm your chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
