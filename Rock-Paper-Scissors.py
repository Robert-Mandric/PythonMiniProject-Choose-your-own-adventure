import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("To play type Rock, Paper or Scissors. To quit press Q.").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Try writing again your option.")
        continue
    else:
        print(f'You chose {user_input}!')

    random_number = random.randint(0, 2)
    # 0 = Rock / 1 = Paper / 2 = Scissors
    computer_pick = options[random_number]
    print(f'Computer chose {computer_pick}.')

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a Draw!")
    else:
        print("You Lose!")
        computer_wins += 1
print(f'You won {user_wins} times.')
print(f'Computer won {computer_wins} times.')
print("Goodbye!")