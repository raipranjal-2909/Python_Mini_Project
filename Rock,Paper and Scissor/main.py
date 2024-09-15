import random

users_wins = 0 
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_inputs = input("Type Rock,Paper,Scissors or Q to quit: ").lower()
    if user_inputs == "q":
        break

    if user_inputs not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")    

    if user_inputs == "rock" and computer_pick == "scissors":
        print("You Won!")
        users_wins+=1
    
    elif user_inputs == "paper" and computer_pick == "rock":
        print("You Won!")
        users_wins+=1

    elif user_inputs == "scissors" and computer_pick == "paper":
        print("You Won!")
        users_wins+=1
    
    elif user_inputs == computer_pick:
        print("Round Tied")

    else:
        print("You Lost!")
        computer_wins +=1

print(f"You Won", users_wins, "times.")
print(f"Computer Won", computer_wins, "times.")
print("Goodbye!")