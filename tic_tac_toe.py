# Tic Tac Toe
# Author: Adam Huffman
# Date: 5/16/18
# Description: Tic Tac Toe project from Udemy's Python Bootcamp.

# Imports and function definitions.
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
	'''
	Checks to see if the provided marker has won.
	Input: Game board, marker of player to be checked.
	Output: Boolean indicating victory.
	'''
	return ((board[0] == marker and board[1] == marker and board[2] == marker) or (board[3] == marker and board[4] == marker and board[5] == marker) or (board[6] == marker and board[7] == marker and board[8] == marker) or (board[0] == marker and board[3] == marker and board[6] == marker) or (board[1] == marker and board[4] == marker and board[7] == marker) or (board[2] == marker and board[5] == marker and board[8] == marker) or (board[0] == marker and board[4] == marker and board[8] == marker) or (board[2] == marker and board[4] == marker and board[6] == marker))
    
def choose_first():
	'''
	Determines the first player based on a random number.
	Input: None
	Output: String indicating which player is going first.
	'''
	player1 = random.randint(1, 101)
	player2 = random.randint(1, 101)
    
	if player1 > player2:
		return 'Player 1'
	else:
		return 'Player 2'
        
def space_check(board, position):
	'''
	Checks to see if the provided position is available.
	Input: Game board, position to be checked.
	Output: Boolean indicating whether the position is free.
	'''
	return (board[position] != 'X' and board[position] != 'O')
    
def board_full(board):
	'''
	Checks to see if the board is full
	Input: Game board.
	Output: Boolean indicating whether or not the board is full.
	'''
	#If there are no blank spaces on the board, it is full.
	return not ' ' in board
    
def move(board):
	'''
	Asks the player which position they would like to play in.
	Input: Game board.
	Output: Integer corresponding to the chosen position.
	'''
	position = 0
    
	while position not in range(1,10):
        
        #Subtract 1, because lists are zero-indexed.
		position = int(input('Please choose a positional number, between 1 and 9: ')) - 1
        
		if space_check(board, position):
			break
		else:
			position = 0
			print('That position is not available.')
        
	return position
    
def replay():
	'''
	Ask the players if they want to play again.
	Input: None
	Output: Boolean indicating the players' choice.
	'''
	answer = ''
    
	while answer != 'y' and answer != 'n':
		answer = input('Do you want to play again? [Y][N] ').lower()
    
	return answer == 'y'

# Game logic.
print('Welcome to Tic Tac Toe!')

# Infinite game loop.
while True:
	# Initialize the game.
	board = [' '] * 9
	player1_token, player2_token = player_input()
	position = -1
	turn = choose_first()

	print(turn + ' will go first.')

	#Loop until there is a winner.
	while True:

		if turn == 'Player 1':
			#First player's turn.
			draw_board(board)
			print("First player's turn.")
			position = move(board)
			place_marker(board, position, player1_token)

			#Check for end conditions.
			if win_check(board, player1_token):
				draw_board(board)
				print('Congratulations, ' + turn + '. You have won!')
				break
			elif board_full(board):
				draw_board(board)
				print('This match is a draw!')
				break
			else:
				turn = 'Player 2'
		else:
			#Second player's turn.
			draw_board(board)
			print("Second player's turn.")
			position = move(board)
			place_marker(board, position, player2_token)

			#Check for end conditions.
			if win_check(board, player2_token):
				draw_board(board)
				print('Congratulations, ' + turn + '. You have won!')
				break
			elif board_full(board):
				draw_board(board)
				print('This match is a draw!')
				break
			else:
				turn = 'Player 1'

	#Play again?
	if not replay():
		break

print('')
print('Thanks for playing!')

