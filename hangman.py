import time
import random

#word array to select from
words_array = ['time', 'money', 'code', 'dragon', 'winning', 'avocado', 'waverider']
#hard coded word
word = random.choice(words_array)
#store user guesses (initially empty)
guesses = ''
#user gets 10 turns
turns = 10

#grab user input from terminal
name = input("What is your name?\n")

# print greeting to user using their name
print(f"Hello {name} time to play hangman!")

time.sleep(1)

print("Guess a letter!")
time.sleep(.5)




while turns > 0:
    print(word)
    turns -= 1
    failed = 0

    for char in word:
        if char in guesses:
            print(char),
        else:
            print("_")
            failed += 1


#################### GRAVEYARD ####################

# def get_word():
#     word = random.choice(words_array)
#
# get_word()
