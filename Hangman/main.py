import os
import random

from hangman_words import word_list
end_of_game = False
chosen_word = random.choice(word_list)

lives = 6

from hangman_art import logo
print(logo)

print(f'Pssst, the solution is {chosen_word}')

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter:").lower()

  os.system('cls')

  if guess in display:
    print(f"You've already guessed {guess}")

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    print(f"you guessed {guess},word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("you lose")

  print(f"{' '.join(display)}")

  print(display)

  if "_" not in display:
    end_of_game = True
    print("You Win")
    
  from hangman_art import stages
  print(stages[lives])
  
print(f'Pssst, the solution is {chosen_word}')
