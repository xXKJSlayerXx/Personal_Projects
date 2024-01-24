# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import random, randint

test_board = ['#', 'O', 'O', 'X', 'O', 'S', 'O', 'X', 'O', 'O']
#blank_board = ['#', '', '', '', '', '', '', '', '', '']




def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose your marker (X or O): ')
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return [player1, player2]


board = []


def display_board(board):
    # Use a breakpoint in the code line below to debug your script.
    print('               ' + board[7] + '| ' + board[8] + ' |' + board[9])
    print('               ' + board[4] + '| ' + board[5] + ' |' + board[6])
    print('               ' + board[1] + '| ' + board[2] + ' |' + board[3])  # Press Ctrl+F8 to toggle the breakpoint.


def place_marker(board, marker, position):
    # postion = ''
    # position_range = range(1,10)

    # while postion not in position_range:
    # postion = input('Choose your postion (1-9): ')

    board[position] = marker


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    first_player = randint(1,2)

    return first_player


def space_check(board, position):
    if len(board[position]) == 0:
        return True
    else:
        return False


def full_board_check(board):
    if len(board) == 10:
        return True
    else:
        return False


def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


def replay():
    play = ''
    while play != 'y' and play != 'n':
        play = input('Want to play again? (y/n): ')
        if play == 'y':
            return True
        elif play == 'n':
            return False
        else:
            pass

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

print('Welcome to Tic Tac Toe')
blank_board = ['$'] + [''] * 9
[player1_marker,player2_marker] = player_input()
first = choose_first()
print(f'Player {first} will go first')
play_game = input('Do you want to play? ')
if play_game.lower()[0] == 'y':
    game_on = True
else:
    game_on = False


while game_on == True:
    if first == 1:
        display_board(blank_board)
        position = player_choice(blank_board)
        place_marker(blank_board, player1_marker, position)

        if win_check(blank_board, player1_marker):
            display_board(blank_board)
            print('Congratulations! You have won the game!')
            game_on = False
        else:
            if full_board_check(blank_board):
                display_board(blank_board)
                print('The game is a draw!')
                break
            else:
                first = 2

    else:
        # Player2's turn.

        display_board(blank_board)
        position = player_choice(blank_board)
        place_marker(blank_board, player2_marker, position)

        if win_check(blank_board, player2_marker):
            display_board(blank_board)
            print('Player 2 has won!')
            game_on = False
        else:
            if full_board_check(blank_board):
                display_board(blank_board)
                print('The game is a draw!')
                break
            else:
                first = 1

















