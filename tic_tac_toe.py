# Tic Tac Toe
# Author: Adam Huffman
# Date: 5/16/18
# Description: Tic Tac Toe project from Udemy's Python Bootcamp.

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
    
def check_winner(board, token):
    '''
    Checks the board for a winner.
    Input: List of strings containing the board state, token indicating the player.
    Output: True if there is a winner, False if there is not.
    '''
    winner = False
    
    #Check the rows
    

#Infinite game loop.
while True:
    
    board = [' '] * 9 #Initialize the board in a clean state.
    winner = False #Nobody has won yet.
    player1_turn = True #For keeping track of the turn.
    turn_count = 0 #For keeping track of the turn count.
    
    #Until we have a winner.
    while not winner:
        
        #Draw the board
        draw_board(board)
        
        #Increment the turn count.
        turn_count += 1
        
        #Player 1 input.
        while player1_turn:
            selection = int(input('Player 1, enter a number: '))
            
            if selection not in range(len(board)) or board[selection] != ' ':
                print('\nThat is not a valid position!')
                continue
            else:
                board[selection] = 'X'
                player1_turn = False
        
        #Check for a draw
        if turn_count >= len(board):
            print('\nThe game is a draw!')
            winner = True
            break
        
        #Draw the board
        draw_board(board)
        
        #Increment the turn count.
        turn_count += 1
                
        #Player 2 input.        
        while not player1_turn:
            selection = int(input('Player 2, enter a number: '))
            
            if selection not in range(len(board)) or board[selection] != ' ':
                print('\nThat is not a valid position!')
                continue
            else:
                board[selection] = 'O'
                player1_turn = True
     
    #Ask if the user wants to play again.          
    if input('Play again? [Y][N]: ').lower() == 'n':
        break
    
#The game is over.
print('\nThanks for playing!')
            
