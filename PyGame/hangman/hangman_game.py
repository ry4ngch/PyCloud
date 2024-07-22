stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


import random
import os

clear = lambda: os.system('clear')
print(clear())
print(logo)
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
pr_list = ["_"]*len(chosen_word)
lives = 6

while "_" in pr_list:
   if lives > 0:
       guess = input("Guess a letter: ").lower()
       if not guess in pr_list:
           if guess in chosen_word:
               for pos, letter in enumerate(chosen_word):
                   if letter == guess:
                       pr_list[pos] = guess
           else:
               print("You lose a life")
               lives -= 1
       else:
           print(f"You already guess the character {guess}")
       clear()
       print(stages[lives])
       print(pr_list)
   else:
       print("You lose")
       print(stages[0])
       break
