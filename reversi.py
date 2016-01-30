#!/usr/bin/env python
#python2 program that simulates a game of reversi

p1, p2 = None, None #characters for each player

def draw_board(board):
	'''This function takes in an 8x8 array and prints it to stdout.'''
	#TODO: really should label each row and column so noone has to count every time

	row = 0
	for i in range(3*8+1):
		if i==0:
			print (' '+ ('_'*3) )*8
		elif i%3 == 1:
			print '|   '*8 + '|'
		elif i%3 == 2:
			print ('|'+' '+ str(board[row][0])+' ') + ('|'+' '+ str(board[row][1])+' ') + ('|'+' '+ str(board[row][2])+' ') + ('|'+' '+ str(board[row][3])+' ') + ('|'+' '+ str(board[row][4])+' ') + ('|'+' '+ str(board[row][5])+' ') + ('|'+' '+ str(board[row][6])+' ') + ('|'+' '+ str(board[row][7])+' ') + '|'
			row += 1
		elif i%3 == 0:
			print '|___'*8 + '|'

def instructions():
	'''This function prints the instructions for reversi.'''

	print '''\n\t-----------------Welcome to reversi!-----------------
	The goal of the game is to have more spaces filled
	by your symbol than spaces filled by your opponent's.
	For each turn a player places one piece (of their 
	symbol) on the board in a position where there is a 
	line (horizontal, vertical, or diagonal) of at least 
	one of the opponent's pieces with a piece of the 
	current player's symbol at the other end of the line. 
	Then, all of the pieces in this line are captured and 
	are changed to the player's symbol. This ends the turn.
	It's less complicated than it sounds, here's an example:\n'''
	#TODO: display a sample move, include numbering method

def find_lines(board, x, y):
	'''This function takes in an 8x8 list of a board and x,y the coordinates of the most recent move made on the board. 
	It returns a list of all of the lines which may be captured by this move.'''

	#TODO: pretty much everything
	if board[x][y] == p1:
		opp = p2
	else:
		opp = p1
'''	while x+i in range(8) and y+i in range(8):
	if board[x-1][y-1] == opp:
	if board[x-1][y] == opp:
	if board[x-1][y+1] == opp:
	if board[x][y+1] == opp:
	if board[x][y-1] == opp:
	if board[x+1][y-1] == opp:
	if board[x+1][y] == opp:
	if board[x+1][y+1] == opp:
'''

def flip(board, lines):
	'''This function takes in a list of lines to be flipped over and the board on which to flip them. It flips them in place and returns None.'''
	#TODO
	pass

def turn(player, board):
	'''This function plays a whole turn for a noncomputer player. It takes in the symbol used for the current player and the board being played on.'''

	#TODO uncomment section when function is callable
	#if no moves just return
	#if len(find_lines(board, x, y)) == 0:
	#	return
	while True:
		move = raw_input("What space would you like to move to?(# #)\n")
		try:
			y,x = move.split()
			x = int(x)
			y = int(y)
		except:
			print "Input not in correct form."
			continue
		if not x in range(8) or not y in range(8):
			print "Number not in range of board spaces."
			continue
		if not board[x][y] == ' ':
			print "Space already occupied."
		else:
			board[x][y] = player
			break
	lines = find_lines(board, x, y)
	flip(board, lines)

	draw_board(board)

def game():
	'''This function starts a new game, by initializing any necessary variables and calling each turn or computer move.'''
	pass


#test each function

instructions()

board = [[" "]*8 for i in range(8)]
draw_board(board)

turn("X", board)

#main 
play = None

while play not in ["yes", "no", 'y', 'n']:
	play = raw_input("Would you like to play reversi?(y/n)\n").lower()
while play[0] == 'y':
	game()
	play = raw_input("Would you like to play again?").lower() 
		#TODO add check loop

#initiate game
#X print instructions of some kind
#turn
#	choose move - input or AI
#		skip turn if no moves are available
#	flip pieces
#X	draw board (8x8)
#win conditions - when all spots are full, highest #
