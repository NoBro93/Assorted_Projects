#tic tac toe game with AI to play against 
#maybe have options for 1 player or 2 player

#TODO:
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

def turn(player, board):
    while True:
        move = raw_input("Where would you like to move?")
        try:                            #in case a noninteger is input
            move = int(move)
        except:
            print "Please enter an integer"
            continue
        if move >= 1 and move <=9:      #make sure number is in range of board
            if board[move - 1] == ' ':      #if empty slot
                board[move - 1] = player    #set slot to that player
                break
            else:
                print "That slot is not available"
        else:
            print "Number not in range (1-9)"
    printBoard(board)

#INITIALIZATIONS
board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] #initialize board as empty
player = raw_input("Would you like to be X or O?")[0] #the [0] is in case they enter more than 1 character
if player == 'X':   #may ask second player if one exists
    computer = 'O'
else:
    computer = 'X'

#GAMEPLAY
printBoard([1,2,3,4,5,6,7,8,9]) #use to show the options for spaces
for i in range(9): #for now, play as if 2 players, later add a step to calculate the computer's move
    if i%2 == 0:
        turn(player, board)
    else:
        turn(computer, board)