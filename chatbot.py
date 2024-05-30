import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi!"]),
    (r"how are you?", ["I'm good, thank you!", "I'm doing well, thanks for asking."]),
    (r"what's your name?", ["I'm a chatbot created by Zaman.", "You can call me RoboChat."]),
    (r"(.*) your name(.*)", ["I'm a chatbot created by OpenAI.", "You can call me robochat."]),
    # Add more patternswhats your and responses as needed
]

# Create chatbot
chatbot = Chat(patterns, reflections)



print("Hi! I'm Robochat. How can I help you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    if response:
        print("Robochat:", response)
    else:
        print("Robochat: I'm sorry, I didn't understand that. Please ask me something else.")