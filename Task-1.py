import re
import random
from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"
def get_weather_info():
    return "It's sunny with a light breeze. Temperature: 25°C."

def education_topics():
    print("\nChatbot: Here are some popular educational topics you can explore:")
    print("1. Artificial Intelligence - AI involves creating machines that can perform tasks that usually require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.")
    print("2. Data Science - Data Science is a field that uses scientific methods, processes, algorithms, and systems to extract knowledge and insights from structured and unstructured data.")
    print("3. Python Programming - Python is a high-level, interpreted programming language known for its simplicity and readability, widely used in web development, data analysis, and machine learning.")
    print("4. Machine Learning Basics - Machine Learning is a branch of AI that allows systems to learn and improve from experience without being explicitly programmed. It involves algorithms that can identify patterns in data.")
    print("5. Web Development - Web Development is the process of building websites and web applications, which can range from simple static pages to complex dynamic applications.")

def get_motivational_quote():
    quotes = [
        "The best way to predict the future is to create it.",
        "You are never too old to set another goal or to dream a new dream.",
        "Believe you can and you're halfway there.",
        "Don’t watch the clock; do what it does. Keep going.",
        "The harder you work for something, the greater you’ll feel when you achieve it."
    ]
    return random.choice(quotes)

def common_conversation(user_input):
    if re.search(r"\bhow are you\b", user_input):
        responses = [
            "I'm doing great, thank you for asking! How about you?",
            "I'm just a chatbot, but I'm feeling fantastic! How can I assist you today?",
            "I'm doing well, thanks for asking! How can I help you today?"
        ]
        return random.choice(responses)

    elif re.search(r"\bwhat is your name\b", user_input):
        return "I am your friendly chatbot, here to assist you with anything you need!"

    elif re.search(r"\bhow old are you\b", user_input):
        return "As a chatbot, I don't have an age. But I am always learning new things!"

    elif re.search(r"\bwhat can you do\b", user_input):
        return ("I can help with the current time, date, weather, suggest educational topics, "
                "share motivational quotes, and much more. Just ask!")

    elif re.search(r"\bok\b", user_input):
        return "Okay! Let me know if you need anything else."

    elif re.search(r"\bbye\b|\bgoodbye\b", user_input):
        return "Goodbye! Have a wonderful day! Feel free to come back anytime."

    elif re.search(r"\bgood morning\b", user_input):
        return "Good morning! How can I assist you today?"

    elif re.search(r"\bgood afternoon\b", user_input):
        return "Good afternoon! How can I help you today?"

    return None  
print(f"Chatbot: {get_greeting()} Hi! How can I assist you today?")
print("Type 'exit' to end the conversation.")

while True:
    user_input = input("\nYou: ").lower()  
    
    if user_input == "exit":
        print("Chatbot: Goodbye! Have a wonderful day!")
        break

    elif re.search(r"\bhello\b|\bhi\b|\bhey\b", user_input):
        print("Chatbot: Hello! How can I help you today?")

    elif re.search(r"\btime\b", user_input):
        print(f"Chatbot: The current time is {get_current_time()}.")

    elif re.search(r"\bdate\b", user_input):
        print(f"Chatbot: Today's date is {get_current_date()}.")

    elif re.search(r"\bweather\b|\btemperature\b", user_input):
        print(f"Chatbot: {get_weather_info()}")

    elif re.search(r"\beducation\b|\bstudy\b|\btopics\b", user_input):
        education_topics()

    elif re.search(r"\bmotivation\b|\bquote\b", user_input):
        print(f"Chatbot: Here's a motivational quote for you: {get_motivational_quote()}")

    elif re.search(r"\bthank you\b|\bthanks\b", user_input):
        print("Chatbot: You're welcome! Let me know how else I can assist.")

    elif re.search(r"\bhelp\b", user_input):
        print("\nChatbot: Here are some commands you can use:")
        print("1. Ask for today's date – Type: 'What's the date?'")
        print("2. Ask about the current time – Type: 'What's the time?'")
        print("3. Ask about weather information – Type: 'Weather today?'")
        print("4. Learn about educational topics – Type: 'Tell me about education.'")
        print("5. Ask for a motivational quote – Type: 'Give me a motivation.'")
        print("6. Ask how the chatbot is doing – Type: 'How are you?'")
        print("7. Ask what the chatbot can do – Type: 'What can you do?'")
        print("8. Type 'exit' to end the chat.")

    elif common_conversation(user_input):
        print(f"Chatbot: {common_conversation(user_input)}")

    else:
        print("Chatbot: I'm not sure I understand that. Could you rephrase your question or type 'help' for assistance.")
