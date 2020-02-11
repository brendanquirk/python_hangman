import time
import random

#word array to select from
words_array = ['time']
# , 'money', 'code', 'dragon', 'winning', 'avocado', 'waverider'
#hard coded word
word = random.choice(words_array)
#store user guesses (initially empty)
wrong_guesses = []
#store correct letters in array
correct_word = []
#user gets 10 turns
turns = 10

#grab user input from terminal
name = input("What is your name?\n")

# print greeting to user using their name
print(f"Hello {name} time to play hangman!")

time.sleep(1)
print(f"The word has {len(word)} letters!")
time.sleep(1)



### while loops that runs when user still has turns ###
# if len(word) is len(str.join('', correct_word)):
#     print(f"You win! The word was {word}")
# else:
while len(word) > len(str.join('', correct_word)) and turns > 0:
    guess = input("Guess a letter!\n")
    time.sleep(.5)
    if guess in wrong_guesses or guess in correct_word:
        print(f"you have already guessed {guess}, try again")
    elif guess in word:
        print(f"{guess} is in the word!")
        # wrong_guesses.append(guess)
        correct_word.append(guess)
        print(f"All wrong guesses so far {wrong_guesses}")
        print(f"All correct guesses so far: {correct_word}")
        # print(f"Correct word:{len(str.join('', correct_word))}")
        print(f"Word Length: {len(word)}")
    elif guess not in word:
        turns -= 1
        print(f"{guess} is not in the word! Try again! You have {turns} wrong guesses left!")
        wrong_guesses.append(guess)
        print(f"All wrong guesses so far: {wrong_guesses}")
        print(f"All correct guesses so far: {correct_word}")
    else:
        print(f"You win! The word was {word}!")




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
