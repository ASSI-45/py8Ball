import random

def intro():
    print("Hello i am a ball ask me any question you desire.")
    print("It just has to be a yes or no question, cause i dont\ncare bout the you. :)") 
    print("Type quit to exit\n")

def question():
    inp = input("And you ask?\n")
    if inp == "quit":
        exit()

def answer():
    rndNum = random.randrange(4)
    match(rndNum):
        case 0:
            print("Yes.")
        case 1:
            print("No.")
        case 2:
            print("Maybe.")
        case 3:
            print("Who knows. I dont know, and dont care")

if __name__ == "__main__":
    intro()
    while(True):
        question()
        answer()
