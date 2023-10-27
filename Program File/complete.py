import nltk
from nltk.chat.util import Chat, reflections
patterns = [
    (r'hello|hi|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am just a chatbot, but thanks for asking!']),
    (r'what is your name', ['I am a chatbot created with Python.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later.']),
]
chatbot = Chat(patterns, reflections)
print("Hello, I'm your chatbot. Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.respond(user_input)
    print("Chatbot:", response)
