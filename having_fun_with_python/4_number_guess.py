'''
This app chose a number and
you try to guess it!
in the end, it gives you true answers and attempts count.
'''

import random


def welcome():
    print("Hi and welcome to the show!")
    print("I'll choose a random number and you'll try to guess it!")
    print("-----------------------------------------------------\n\n")
def generate_random_number():
    return random.randint(1, 10)


def get_a_guess():
    guess = int(input("what do you think my number is? "))
    return guess


def check_guess(computer_number, user_guess):
    if computer_number > user_guess:
        print("Mine is bigger!")
    elif computer_number < user_guess:
        print("Mine is smaller!")
    else:
        print("Ohhh! you won!")


IS_GUESS = False
GUESS = 0
ATTEMPTS = 0
computer_number = generate_random_number()


welcome()

while (not IS_GUESS):
    GUESS = get_a_guess()
    check_guess(computer_number, GUESS)
    ATTEMPTS += 1
    if computer_number == GUESS:
        IS_GUESS = True

print(f"You found {computer_number} in {ATTEMPTS} attempts!")
