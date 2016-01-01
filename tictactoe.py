#tic tac toe game with AI to play against 
#maybe have options for 1 player or 2 player

#TODO:
#board - array from 0 to 8 left to right, then down
#players - either 2 players or 1 + computer
#how to take a turn - ask for a move, check if valid, store move
#AI - decide which move is best - see xkcd?, maybe have easy/hard modes
#how to check for wins - long way?

def printBoard(board):
    print
    for i in range(9):
        if i%3 == 0 or i == 8:
            print "   |   |"
        elif i%3 == 1:
            print '', board[i-1],'|', board[i], '|', board[i+1]
        elif i<8:
            print "___|___|___"
    print
printBoard([1,2,3,4,5,6,7,8,9])

#MAIN
board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] #initialize board as empty
printBoard(board)