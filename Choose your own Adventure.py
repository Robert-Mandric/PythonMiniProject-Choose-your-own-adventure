name = input('Enter your name: ').capitalize()
print(f'Welcome {name}, to your brand new adventure! ')

q1 = input('Your car broke and you are at the end of a dirt road.\nWhich way do you wanna go?\n Left or Right? ').lower()

if q1 == 'left':
    q2 = input('You chose left and came across a river.\nYou can walk around it or swim to get across.\nWhich way do you wanna choose?\n Swim or Walk? ').lower()
    if q2 == 'swim':
        print('You jumped in and tried to swim but an alligator killed you.\n~~~You Lose!~~~')
    elif q2 == 'walk':
        print('You walked until you saw a bridge and walked across the river.')
    else:
        print('Not a valid option. You Lose!')

elif q1 == 'right':
    q3 = input('You come to a bridge.\nIt looks wobbly, do you wanna cross it or head back?\n Cross or Back? ').lower()
    if q3 == 'cross':
        print('The bridge crumbles, you fall and die.\n~~~You Lose!~~~')
    elif q3 == 'back':
        q4 = input('You went back and there is a stranger on the road.\nDo you talk to them?\n Talk or Ignore? ').lower()
        if q4 == 'talk':
            print('The strange repairs your car!\n~~~You Win!~~~')
        elif q4 == 'ignore':
            print('You ran out of choices...\n~~~You Lose!~~~')
        else:
            print('Not a valid option. You Lose!')
    else:
        print('Not a valid option. You Lose!')

else:
    print('Not a valid option. You Lose!')