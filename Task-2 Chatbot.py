import datetime
import nltk
from nltk.chat.util import Chat, reflections

# Define intent patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'who are you?', ["I am a chatbot"]),
    (r'what is your name?', ["You can call me ChatBuddy.", "I'm just a ChatBuddy.", "My name is ChatBuddy"]),
    (r'how are you?', ["I'm doing well, thank you!", "I'm fine, thanks."]),
    (r'who am I\?', ["You are human"]),
    (r'what can you do?', ["I can provide information, answer your questions, and chat with you!"]),
    (r'help', ["Sure! What do you need help with?", "How can I assist you?"]),
    (r'how old are you?', ["I don't have an age. I'm just a computer program!"]),
    (r'what day is it today\?', [datetime.datetime.now().strftime("Today is %A")]),
    (r'What is today\'s date\?', [datetime.datetime.now().strftime("%d %B, %Y")]),
    (r'what time is it\?', [datetime.datetime.now().strftime("%H:%M:%S")]),  # Corrected closing parenthesis
    (r'what is the weather like today?', ["I'm sorry, I don't have access to real time weather information."]),
    (r'where are you from?', ["I exist in the digital realm, so I don't have a physical location."]),
    (r'what is the capital of India\?', ["Delhi"]),
    (r'will rcb win ipl this year\?', ["Ohhh!!! it's really tough question"]),
    (r'what is the meaning of life\?', ["The meaning of life is a philosophical question that people have debated for centuries!"]),
    (r'quit', ['Bye, take care.', 'Goodbye!'])
]

# Create a chatbot with defined patterns
chatbot = Chat(patterns, reflections)

# Define a function to chat with the user
def chat():
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        if not response:  # If response is empty (no pattern matched)
            print("ChatBuddy: I'm sorry, I didn't understand that.")
        else:
            print("ChatBuddy:", response)
        if user_input.lower() == 'quit':
            break

# Call the chatbot function
chat()
