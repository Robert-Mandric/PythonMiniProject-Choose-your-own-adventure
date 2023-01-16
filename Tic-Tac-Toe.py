"""Tic-Tac-Toe Board
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

1. user_input -> x/o in the 1-9 spots
2. if they enter anything else return them
3. check if the user_input already exist
4. add it to the board if correct
5. check if the user won/lost/draw: rows, columns, diagonals
6. toggle between users upon succesful moves
"""

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

user = True #When true means X, otherwise means O
turns = 0

def print_board(board):
    for row in board:
        for slot in row:
            print(f'{slot} ', end='')
        print()

#print_board(board)

def quit(user_input):
    if user_input == 'q':
        print('Thanks for playing!')
        return True
    else:
        return False

def check_input(user_input):
    #check if its a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    #check if its 1-9 nr
    if not bounds(user_input):
        return False
    return True

def isnum(user_input):
    if not user_input.isnumeric():
        print('This is not a valid number!')
        return False
    else:
        return True

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print('Number is out of bounds!')
        return False
    else:
        return True

def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print('This position is already taken!')
        return True
    else:
        return False

def coordonates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return(row, col)

def iswin(user, board):
    if check_row(user, board):
        return True
    if check_col(user, board):
        return True
    if check_diag(user, board):
        return True
    return False
    
def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col:
            return True
    return False

def check_diag(user, board):
    if board[0][0] == user and board[1][1] == user and board [2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board [2][0] ==user:
        return True
    else:
        return False


def add_to_board(coords, board, active_user):
  row = coords[0]
  col = coords[1]
  board[row][col] = active_user

def current_user(user):
    if user:
        return 'x'
    else:
        return 'o'


while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input('Enter a position from 1 to 9.\nPress "q" to Quit. ').lower()
    if quit(user_input):
        break
    if not check_input(user_input):
        print('Please try again.')
        continue
    user_input = int(user_input) - 1
    coords = coordonates(user_input)
    if istaken(coords, board):
        print("Please try again!")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f'{active_user.upper()} won! ')
        break

    turns += 1
    if turns == 9:
        print("It's a draw!")
    user = not user
