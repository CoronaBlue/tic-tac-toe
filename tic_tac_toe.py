# Tic Tac Toe
# Author: Adam Huffman
# Date: 5/16/18
# Description: Tic Tac Toe project from Udemy's Python Bootcamp.

import random

def draw_board(board):
    '''
    Prints the Tic Tac Toe game board.
    Input: List of strings containing the board state.
    Output: None
    '''
    print(' | |')
    print('{}|{}|{}'.format(board[6], board[7], board[8]))
    print('_|_|_')
    print(' | |')
    print('{}|{}|{}'.format(board[3], board[4], board[5]))
    print('_|_|_')
    print(' | | ')
    print('{}|{}|{}'.format(board[0], board[1], board[2]))
    print(' | | ')
    
def player_input():
    '''
    Assigns player markers.
    Input: None
    Output: Tuple containing assigned markers, in the form of (player1, player2).
    '''
    marker = ''
    
    #Repeat until a valid input is received.
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
        
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, position, marker):
    '''
    Places a marker on the board at the desired position.
    Input: List containing the game board, an integer of the desired position, and a string marker
    Output: Updated board.
    '''
    #Place the marker
    board[position] = marker
    
    return board
    
def win_check(board, marker):
    return ((board[0] == marker and board[1] == marker and board[2] == marker) or #Bottom
    (board[3] == marker and board[4] == marker and board[5] == marker) or #Middle
    (board[6] == marker and board[7] == marker and board[8] == marker) or #Top
    (board[0] == marker and board[3] == marker and board[6] == marker) or #Left
    (board[1] == marker and board[4] == marker and board[7] == marker) or #Center
    (board[2] == marker and board[5] == marker and board[8] == marker) or #Right
    (board[0] == marker and board[4] == marker and board[8] == marker) or #Diagonal
    (board[2] == marker and board[4] == marker and board[6] == marker)) #Antidiagonal
    
def choose_first():
    player1 = random.randint(1, 101)
    player2 = random.randint(1, 101)
    
    if player1 > player2:
        print('Player 1 will go first!')
    else:
        print('Player 2 will go first!')
        
def space_check(board, position):
    
    return (board[position] != 'X' and board[position] != 'O')
    
def board_full(board):
    return not ' ' in board
    
def move(board):
    position = 0
    
    while position not in range(1,10):
        
        position = input('Please choose a positional number, between 1 and 9: ')
        
        if space_check(board, postition):
            break
        else:
            position = 0
            print('That position is not available.')
        
    return position
    
def replay():
    answer = ''
    
    while answer != 'y' and answer != 'n':
        answer = input('Do you want to play again? [Y][N]').lower()
    
    return answer == 'y'

test_board = ['3'] * 9
        
player1_token, player2_token = player_input()

test_board = place_marker(test_board, 8, ' ')
#test_board = place_marker(test_board, 5, player1_token)
#test_board = place_marker(test_board, 2, player1_token)

print(board_full(test_board))

