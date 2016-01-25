#!/usr/bin/env python
#python2 program that simulates a game of reversi

def draw_board(board):
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

#test each function
board = []
for i in range(8):
	board.append(range(8))

draw_board(board)

#main 

#initiate game
#print instructions of some kind
#turn
#	choose move - input or AI
#		skip turn if no moves are available
#	flip pieces
#X	draw board (8x8)
#win conditions - when all spots are full, highest #
