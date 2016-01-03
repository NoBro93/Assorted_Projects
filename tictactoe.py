#tic tac toe game with AI to play against 
#maybe have options for 1 player or 2 player

#TODO:
#AI - decide which move is best - see xkcd?, maybe have easy/hard modes

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
    
def clearBoard(): #sets up a board of all empty spaces
    return[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
def turn(player, board):
    while True:
        move = raw_input("Where would you like to move, player " + player + '?') #TODO: fix for computer player
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

def win(board):
    winner = ''
    for i in range(3):
        n = 3*(i+1) - 1 #used for row calculations, makes (0,1,2) into (3, 6, 9)
        if board[i] != ' ':
            if board[i] == board[i+3] and board[i+3] == board[i+6]: #checks column wins
                winner = board[i]
        elif board[n] != ' ':
            if board[n] == board[n - 1] and board[n - 1] == board[n - 2]: #checks rows for wins
                winner = board[n]
    if board[4] != ' ': 
        if board[0] == board[4] and board[4] == board[8]: #left diagonal
            winner = board[4]
        elif board[2] != ' ' and board[2] == board[4] and board[4] == board[6]: #right diagonal 
            winner = board[4]
    return winner

    
#INITIALIZATIONS
print "Welcome to Tic Tac Toe!"
board = clearBoard() #initialize board as empty
player = raw_input("Would you like to be X or O?")[0] #the [0] is in case they enter more than 1 character
if player == 'X':   #TODO: may ask second player if one exists
    computer = 'O'
else:
    computer = 'X'

#GAMEPLAY
print "Use the numbers on this chart to specify which space you would like to move to"
printBoard([1,2,3,4,5,6,7,8,9]) #use to show the options for spaces
for i in range(9): #TODO: for now, play as if 2 players, later add a step to calculate the computer's move
    if i%2 == 0:
        turn(player, board)
    else:
        turn(computer, board)
    winner = win(board) #TODO: to keep stats, check winner against players, maybe in win function
    if winner != '':
        print "Player " + winner + " wins!" #fix wording for computer player
        break