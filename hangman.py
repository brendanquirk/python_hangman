import time

#grab user input from terminal
name = input("What is your name?\n")

# print greeting to user using their name
print(f"Hello {name} time to play hangman!")

time.sleep(1)

print("Guess a letter!")
time.sleep(.5)

#hard coded word
word = 'secret'
#store user guesses (initially empty)
guesses = ''
#user gets 10 turns
turns = 10
