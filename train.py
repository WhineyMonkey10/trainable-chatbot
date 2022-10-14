import random
import colorama
from regex import F


user_Items = ["Common greeting", "Common goodbye", "Any random casual question (such as how are you)"]
Items = ["Common FORMAL greeting", "Common FORMAL goodbye", "Any random FORMAL casual question (such as how are you)"]

useritemtoTrain = random.choice(list(user_Items)) #randomly choose an item to train
itemtoTrain = random.choice(list(Items))
user_Items = []


# Defining values to be used in the program
userInput = []
botInput = []


def train(amount):
    for i in range(amount):
            print(f"{colorama.Fore.GREEN}You are training the{colorama.Fore.BLUE} USER {colorama.Fore.GREEN} responses. You will be given a question and you will have to answer it.{colorama.Fore.RESET}")
            print(f"{colorama.Fore.GREEN}The question is: {colorama.Fore.BLUE}{useritemtoTrain}{colorama.Fore.RESET}")
            userinput = input(f"{colorama.Fore.GREEN}Please enter an option (try not to repeat other options already set) {colorama.Fore.RESET}")
            print(f"{colorama.Fore.GREEN}Answer a response of the {colorama.Fore.BLUE}BOT {colorama.Fore.BLUE}to the previous question")
            userinput1 = input(f"{colorama.Fore.GREEN}Please enter an option (try not to repeat other options already set) {colorama.Fore.RESET}")          
            with open("trained_data.txt", "a") as file:
                file.write("\t")
                file.write(f"\"{userinput}\": \"{userinput1}\",")
                file.write("\n")

input("Press enter to start training ")
amount = int(input("How many questions would you like to train? "))
with open("trained_data.txt", "a") as file:
    file.write("{")
    file.write("\n")
train(amount)
with open("trained_data.txt", "a") as file:
    file.write("}")
print(f"{colorama.Fore.GREEN}Training complete!{colorama.Fore.BLUE} Please send the file 'trained_data.txt' to the developer to add it to the program{colorama.Fore.RESET}")







## Whineymonkey10 - Github - 2022