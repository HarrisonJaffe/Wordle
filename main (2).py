import random
import sys
from termcolor import colored
import nltk

nltk.download('words')
from nltk.corpus import words


def print_wordle():
  print("Wordle!")


#creating function
#def Read_Random_Word():
  #with open("Words.txt") as f:
    #words = f.read().splitlines()
    #return random.choice(words)

nltk.data.path.append('/work/words')
words_list = words.words()
words_five = [word for word in words_list if len(word) == 5]
print_wordle()

play_again = ""
while play_again != "q":
  word = random.choice(words_five)
  #word = Read_Random_Word()
  for attempt in range(1, 7):
    guess = input().lower()

    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

    for i in range(min(len(guess), 5)):
      if guess[i] == word[i]:
        print(colored(guess[i], 'green'), end=" ")
        #break
      elif guess[i] in word:
        print(colored(guess[i], 'yellow'), end=" ")
        #break
      else:
        print(colored(guess[i], 'red'), end=" ")
        #break
    print("\n")

    if guess == word:
      print(f"Good Job, it took you {attempt} guesses")

    elif attempt == 6:
      print('\n')
      print(f"The wordle is {word}")
      break
play_again = input(
  "Want to play again? Type enter key to play again, and q to exit.")
