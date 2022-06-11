import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type :\n1 - rock\n2 - paper\n3 - scissor\nq - quit the game\n - ").lower()
    
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "q":
        print("Please enter valid input")
        continue
    elif user_input == "q":
        break

    user_input = int(user_input)
    user_picked = options[user_input-1]
    print("You picked :", user_picked)

    random_number = random.randint(0,2)
    computer_picked = options[random_number]
    print("computer picked :", computer_picked)

    if user_picked == "rock" and computer_picked == "scissor":
        print("You won!!!")
        user_wins +=1

    elif user_picked == "paper" and computer_picked == "rock":
        print("You won!!!")
        user_wins +=1

    elif user_picked == "scissor" and computer_picked == "paper":
        print("You won!!!")
        user_wins +=1

    elif user_picked == computer_picked:
        print("Both picked", user_picked,", Lets try again")
        
    else:
        print("You lost!")
        computer_wins +=1

    print("You won :", user_wins, "and computer won :", computer_wins)

print("Goodbye!")


