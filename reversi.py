#!/usr/bin/env python
#python2 program that simulates a game of reversi

def draw_board():
	for i in range(3*8+1):
		if i==0:
			print (' '+ ('_'*3) )*8
		elif i%3 == 1:
			print '|   '*8 + '|'
		elif i%3 == 2:
			print ('|'+'   ')*8 + '|'#TODO include the board values
		elif i%3 == 0:
			print '|___'*8 + '|'

draw_board()

#initiate game
#print instructions of some kind
#turn
#	choose move - input or AI
#		skip turn if no moves are available
#	flip pieces
#	draw board (8x8)
#win conditions - when all spots are full, highest #
