## Whineymonkey10 - Github - 2022


# Data from: data.json

# Import libraries
import difflib
from difflib import get_close_matches
import json

# Load data

#data from data.json
data = json.load(open("data.json"))
# Define function



def start_chat():
    print("Hello, I'm a chatbot. Ask me a question about the English language.")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            break
        else:
            print("Bot: " + get_response(user_input))


def get_response(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    elif len(get_close_matches(user_input, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(user_input, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(user_input, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Run program
start_chat()