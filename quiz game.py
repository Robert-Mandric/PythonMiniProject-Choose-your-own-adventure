print("Welcome to my Quiz Game")

playing = input("Are you ready for the Quiz Game? ")
if playing.lower() != 'yes':
    print('Closing game...')
    quit()
else:
    print('Okay, get ready!')
    score = 0

answer = input("How many hours does a day have? ")
if answer.lower() != '24':
    print('Wrong answer!')
else:
    print('Correct!')
    score += 1

answer = input("How many albums does Arctic Monkeys have? ")
if answer.lower() != '6':
    print('Wrong answer!')
else:
    print('Correct!')
    score += 1

answer = input("How many albums does Nothing but Thieves have? ")
if answer.lower() != '4':
    print('Wrong answer!')
else:
    print('Correct!')
    score += 1

answer = input("In what month does Summer Well take place? ")
if answer.lower() != 'august':
    print('Wrong answer!')
else:
    print('Correct!')
    score += 1

answer = input("Are you going to the festival? ")
if answer.lower() != 'yes':
    print('Wrong answer!')
else:
    print('Correct!')
    score += 1

print("You got " + str(score) + " questions right!")