import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, 
 paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user>=3 or user<0:
  print("You type an invalid number, You lose!")
else:
  print("user_choice:")
  print(game_images[user])
  computer_choice=random.randint(0,2)
  print("computer_choice:")
  print(game_images[computer_choice])
  if user ==0 and computer_choice==2:
    print("You Win!")
  elif user==2 and computer_choice==0:
    print("You Lose")
  elif computer_choice > user:
    print("You Lose")
  elif user>computer_choice:
    print("You Win!")
  elif computer_choice == user:
    print("It's a draw")
