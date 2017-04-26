from Chessnut import Game
from ChessBoard import *
import time
import random

# class Game_Engine():
#     def __init__(self, board_state):
#         self.game = Game(board_state)
#         self.computer = AI(self.game, 3)
#
#     def prompt_user(self):
#         #TO COMPLETE
#         pass
#
# class AI():
#     def __init__(self, game, max_depth=3, leaf_nodes=[], num_nodes=0):
#         self.game = game
#         self.max_depth = max_depth
#         self.leaf_nodes = leaf_nodes #TO COMPLETE
#         self.num_nodes = num_nodes
#         #add more about caches here


################ GLOBAL VARIABLES ########################################

board = ChessBoard(8,8)
## chessgame = Game() # use this for a NEW GAME, use a fen generator for testing
chessgame = Game(fen='rnbqkbnr/p1pppppp/8/1p6/2P5/8/PP1PPPPP/RNBQKBNR w KQkq b6 0 2')


##chessgame = Game(fen='rnbqkbnr/p1pppppp/8/1p6/2P5/8/PP1PPPPP/RNBQKBNR w KQkq b6 0 2')
##board = ChessBoard(8,8)
board.updateBoard(str(chessgame))




"""
--iniitial moves--
['a2a3', 'a2a4', 'b2b3', 'b2b4', 'c2c3', 'c2c4', 'd2d3', 'd2d4', 'e2e3',
 'e2e4', 'f2f3', 'f2f4', 'g2g3', 'g2g4', 'h2h3', 'h2h4', 'b1c3', 'b1a3',
 'g1h3', 'g1f3']
"""

def checkStatus():
    if chessgame.status == 1:
        print("CHECK")
    if chessgame.status == 2:
        print("CHECKMATE")
    if chessgame.status ==3:
        print("STALEMATE")

def printplayer():
    if chessgame.state[0] == 'w':
        return "White"
    else:
        return "Black"

################################### start pseudo code (won't work) #########

##def maxi(depth):
##    if depth == 0:
##        return evaluate()
##    maxi = float('inf')
##    for ( all moves):
##        score = mini( depth - 1 )
##        if( score > maxi):
##            maxi = score
##    return maxi
##
##def mini(depth):
##    if depth == 0:
##        return -evaluate()
##    mini = float('inf')
##    for ( all moves):
##        score = maxi( depth - 1 )
##        if( score < mini ):
##            mini = score
##    return mini;
##
##def evaluate():
##    global board
##    #updates dictionary
##    moves_dict = {} # {'e2e4': 0, 'f4f5': 3 ...}
##    for move in possible_moves:
##        space_moving_to = move[2:] # 'a6'
##        piece = board.lookupPiece(space_moving_to) #string
##        piece = piece.lower()
##        pieceValue = piece_values[piece] #int
##        moves_dict[move] = pieceValue  #dictionary['new_key'] = value
##    print('the move dictionary (key is space and value is piece value of space) is: ' + str(moves_dict) + '\n')
##
##    #find key of max value in dictionary
##    bestMove = 0 #returns ie. 'e2e4'
##    goodMovesArray = []
##    for key in moves_dict:
##        maxValue = 0
##        if moves_dict[key] > maxValue:
##            goodMovesArray += [key]
##            maxValue = moves_dict[key]
##    print('the array of good moves is ' + str(goodMovesArray) + '\n')
##    if not goodMovesArray:
##        pass
##    else:
##        bestMove = random.choice(goodMovesArray)
##
##    if str(bestMove) == '0':
##        bestMove = random.choice(chessgame.get_moves())
##    print('the best move selected is ' + str(bestMove) + '\n')
##    return str(bestMove)
##
##def bestMoveLocation():

################################## end pseudo code (won't work) #############


def findBestMove():

    global board
    global chessgame

    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 200, ' ': 0}

    # finds all possible moves at moment for playerColor (black or white)
    # returns an array of every move you can possible make at the moment
    # each array element is of the form 'e2e4' where the first two characters are where you ar moving from
    # and the second two characters are where you are moving to

    possible_moves = chessgame.get_moves('b')

    # parse what is on each of the spaces in possible_moves (piece or no piece)
    # possible_moves example = ['e2e4', 'f2f4', etc]
    # check in second half of string if empty space or piece
    # if empty space 0 points, if piece get piece value from above
    # store move and point value for each move into moves_dict (dictionary)

    '''
    http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    import operator
  	stats = {'a':1000, 'b':3000, 'c': 100}
  	max(stats.iteritems(), key=operator.itemgetter(1))[0]
    '''

    ############################### 1-PLY #####################################
##    evaluation = 0
##    evaluation = maxi(0)

    ######## everything below here in this function is basically the "evaluate()" function needed above....

    #updates dictionary
    moves_dict = {} # {'e2e4': 0, 'f4f5': 3 ...}
    for move in possible_moves:
        space_moving_to = move[2:] # 'a6'
        piece = board.lookupPiece(space_moving_to) #string
        piece = piece.lower()
        pieceValue = piece_values[piece] #int
        moves_dict[move] = pieceValue  #dictionary['new_key'] = value
    print('the move dictionary (key is space and value is piece value of space) is: ' + str(moves_dict) + '\n')

    #find key of max value in dictionary
    bestMove = 0 #returns ie. 'e2e4'
    goodMovesArray = []
    for key in moves_dict:
        maxValue = 0
        if moves_dict[key] > maxValue:
            goodMovesArray += [key]
            maxValue = moves_dict[key]
    print('the array of good moves is ' + str(goodMovesArray) + '\n')
    if not goodMovesArray:
        pass
    else:
        bestMove = random.choice(goodMovesArray)

    if str(bestMove) == '0':
        bestMove = random.choice(chessgame.get_moves())
    print('the best move selected is ' + str(bestMove) + '\n')
    return str(bestMove)


def lookahead(player):
    secondLayerMoves = {}
    currentFen = chessgame.get_fen()
    for move in chessgame.get_moves(player):
        secondLayerMoves[move] = []

    for move in chessgame.get_moves(player):
        chessgame.apply_move(move)
        print(board)
        secondLayerMoves[move] += chessgame.get_moves(player)
        chessgame.set_fen(currentFen)
    
    return secondLayerMoves
        
        
        



def runGame():
    turn_counter = 0
    print("Welcome to Chess AI")
    print('player is white (capital letters on bototm of board), AI is black (lowercase letters on top of board\n')
    print('Turn ' + str(turn_counter) + '\n')
    print(board)

    #print all the moves with print(chessgame.get_moves('b'))  player is (chessgame.state.player)
    # MAIN GAME LOOP
    while chessgame.status !=2 or chessgame.status != 3:

        print(printplayer())
        move = input("move: ")
        #error handling for invalid move (ie. n2n3)
        ourPossibleMoves = chessgame.get_moves('w')
        if move in ourPossibleMoves:
            pass
        while move not in ourPossibleMoves:
            move = input("Enter a valid move: ")
            
        chessgame.apply_move(move)
        board.updateBoard(str(chessgame))
        turn_counter += 1
        print('\nTurn ' + str(turn_counter) + ' - white (player) moved\n')
        print(board)

        checkStatus()

        print("Thinking...\n")
        #time.sleep(3)
        ############### SCREWS UP HERE ##################
        move = findBestMove()
        #######move = random.choice(chessgame.get_moves())
        ##print('got past findbestMove!')
        ##print(move) ##### move should look something like this 'd7d6'
        chessgame.apply_move(move)
        board.updateBoard(str(chessgame))
        turn_counter += 1
        print('Turn ' + str(turn_counter) + ' - black (AI) moved\n')
        print(board)


