#!/usr/bin/env python
#python2 program that simulates a game of reversi

#TODO: count number of games
        #count and display scores per turn
        #create validity function to test all available spaces to see which are valid to move to

p1, p2 = None, None #characters for each player

def draw_board(board):
        '''This function takes in an 8x8 array and prints it to stdout.'''
        print "    0   1   2   3   4   5   6   7"
        row = 0
        for i in range(3*8+1):
                if i==0:
                        print '  ' + (' '+ ('_'*3) )*8
                elif i%3 == 1:
                        print '  ' + '|   '*8 + '|'
                elif i%3 == 2:
                        print str(row) + ' ' + ('|'+' '+ str(board[row][0])+' ') + ('|'+' '+ str(board[row][1])+' ') + ('|'+' '+ str(board[row][2])+' ') + ('|'+' '+ str(board[row][3])+' ') + ('|'+' '+ str(board[row][4])+' ') + ('|'+' '+ str(board[row][5])+' ') + ('|'+' '+ str(board[row][6])+' ') + ('|'+' '+ str(board[row][7])+' ') + '|'
                        row += 1
                elif i%3 == 0:
                        print '  ' + '|___'*8 + '|'

def instructions():
        '''This function prints the instructions for reversi.'''

        print '''\n   ------------------Welcome to reversi!------------------
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
        #TODO: display a sample move

def find_lines(board, x, y):
        '''This function takes in an 8x8 list of a board and x,y the coordinates of the most recent move made on the board. 
        It returns a list of all of the pieces which may be captured by this move.'''

        #TODO: pretty much everything
        lines = [] #list of tiles to return (that should be captured)
        if board[x][y] == p1:
                opp = p2
                p = p1
        else:
                opp = p1
                p = p2
        for i, j in [ [-1,-1], [-1,0], [-1, 1], [0,-1], [0,1], [1, -1], [1, 0], [1,1] ]:
                line = [] #stores a list of tiles that match opponent in one direction
                while x+i in range(8) and y+j in range(8):
                        while board[x+i][y+j] == opp:
                                line.append([x+i,y+j])
                                #continue in that direction
                                if i>0:
                                        i += 1
                                elif i<0:
                                        i -= 1
                                if j>0:
                                        j += 1
                                elif j<0:
                                        j -= 1
                        if board[x+i][y+j] == p:
                                lines.extend(line)
                        break
                        
        return lines
                                
def flip(board, lines):
        '''This function takes in a list of pieces to be captured and the board on which they are. It captures them in place and returns None.'''
        if board[lines[0][0]][lines[0][1]] == p1:
                to = p2
        else:
                to = p1
        for x,y in lines:
                board[x][y] = to
        return None

def turn(player, board):
        '''This function plays a whole turn for a noncomputer player. It takes in the symbol used for the current player and the board being played on.'''

        #TODO: if no moves just return - have to do all options for find, valid function
        while True:
                move = raw_input("What space would you like to move to, player " + player + "?(# #)\n")
                try:
                        y,x = move.split() #x and y are actually reversed internally
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
                else:   #add a condition here for whether valid
                        board[x][y] = player
                        break
        lines = find_lines(board, x, y)
        if lines != []:
                flip(board, lines)
        draw_board(board)

def game():
        '''This function starts a new game, by initializing any necessary variables and calling each turn or computer move.'''

        global p1, p2
        p1 = raw_input("What symbol would you like to play as?\n")[0] #in case multiple characters entered
        if p1 != 'X':
                p2 = 'X'
        else:
                p2 = 'O'
        board = [[" "]*8 for i in range(8)] #sets up empty board
        #TODO: use validity function to test for end, for now, until full
        for i in range(32):
                turn(p1, board)
                turn(p2, board)
        
#main 
play = None

while play not in ["yes", "no", 'y', 'n']:
        play = raw_input("Would you like to play reversi?(y/n)\n").lower()
while play[0] == 'y':
        game()
        play = raw_input("Would you like to play again?").lower() 
                #TODO add check loop

#X initiate game
#X print instructions of some kind
#turn
#       choose move - input or AI
#               skip turn if no moves are available
#X       flip pieces
#X      draw board (8x8)
#win conditions - when all spots are full, highest #


