import random

top_of_range= input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number greater than 0!")
        quit()
else:
    print("You did not type a number. Please type a number next time!")
    quit()
random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess= input("Guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("You did not type a number. Please type a number next time!")
        continue

    if user_guess == random_number:
        print("You guess it! Congrats!!!")
        break
    else:
        print('Damn, you got it wrong. Better luck next time...')
        if user_guess > random_number:
            print("The number you used is greater than the one you are trying to guess!")
        else:
            print("The number you used is below than the one you are trying to guess!")
print(f'The number was {random_number}.\nYou got it in {guesses} tries!')
