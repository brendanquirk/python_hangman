import time
import random

#word array to select from
words_array = ['time', 'money', 'code', 'dragon', 'winning', 'avocado', 'waverider']
#hard coded word
word = random.choice(words_array)
#store user guesses (initially empty)
guesses = []
#user gets 10 turns
turns = 10

#grab user input from terminal
name = input("What is your name?\n")

# print greeting to user using their name
print(f"Hello {name} time to play hangman!")

time.sleep(1)
print(f"The word has {len(word)} letters!")
time.sleep(1)

### Grab guess from user ###
# def user_guess():
#     guess = input("Guess a letter!\n")
#     time.sleep(.5)
#
#     guesses.append(guess)
#
#     print(f"You have guessed {guesses}")


### while loops that runs when user still has turns ###
while turns > 0:
    # user_guess()
    guess = input("Guess a letter!\n")
    time.sleep(.5)

    if guess in guesses:
        print(f"you have already guessed {guess}, try again")
    else:
        guesses.append(guess)
        print(f"You guessed {guess}. All guesses so far {guesses}")



### if guess isnt in guesses add to guesses ###


### if it is have them guess again ###

### If guess isnt in word increment a failed variable ###


# while turns > 0:
#     print(word)
#     turns -= 1
#     failed = 0
#
#     for char in word:
#         if char in guesses:
#             print(char),
#         else:
#             print("_")
#             failed += 1
#

#################### GRAVEYARD ####################

# def get_word():
#     word = random.choice(words_array)
#
# get_word()


# while turns > 0:
#     # user_guess()
#     for item in guesses:
#         if item in guesses:
#             print(f"this is the item {item}")
#
#             print(f"You have already guessed {item}, guess again")
#             user_guess()
#         else:
#             print(f"this is the item {item}")
#             # guesses.append(item)
