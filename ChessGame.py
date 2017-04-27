from Chessnut import Game
from ChessBoard import *
import time
import random
from Node import Node



################ GLOBAL VARIABLES ########################################

board = ChessBoard(8,8)
## chessgame = Game() # use this for a NEW GAME, use a fen generator for testing
chessgame = Game(fen='rnbqkbnr/p1pppppp/8/1p6/2P5/8/PP1PPPPP/RNBQKBNR w KQkq b6 0 2')

HumanNextMoves = {}
AINextMoves = {}

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


def minimax(node, depth, maximizingPlayer):

    if depth == 0 or node.isLeaf():
        heuristicValue = findBestMove()
        return heuristicValue

    #maximizingPlayer -AI
    if maximizingPlayer:
        bestValue = -1 * float('inf')
        for child in node.children:
            v = minimax(child, depth-1, False)
            bestValue = max(bestValue,v)
        return bestValue

    #minimizingPlayer- human
    else:
        bestValue = float('inf')
        for child in node.children:
            v = minimax(child, depth-1, True)
            bestValue = min(bestValue,v)
        return bestValue


#this function is simply a heuristic to get the move with the highest point value
#won't be used if we're using minimax
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
    return maxValue

    # print('the array of good moves is ' + str(goodMovesArray) + '\n')
    # if not goodMovesArray:
    #     pass
    # else:
    #     bestMove = random.choice(goodMovesArray)
    #
    # if str(bestMove) == '0':
    #     bestMove = random.choice(chessgame.get_moves())
    # print('the best move selected is ' + str(bestMove) + '\n')
    # return str(bestMove)



def lookAhead(player):
    #create dictionary for 2-ply moves
    secondLayerMoves = {}

    currentFen = chessgame.get_fen()

    for move in chessgame.get_moves(player):
        #each current move is going to be a key for the above dictionary
        secondLayerMoves[move] = []
    #print(secondLayerMoves)
    #print('--------------------------1----------------------------------')
    for move in chessgame.get_moves(player):
        chessgame.apply_move(move)
        opponent = player
        if player == 'b':
            opponent = 'w'
        else:
            opponent = 'b'
        secondLayerMoves[move] += chessgame.get_moves(opponent)
        chessgame.set_fen(currentFen)
    #print(secondLayerMoves)
    return secondLayerMoves


def findMoveBasedonValue(bestValue, player):
    possible_moves = chessgame.get_moves(player)
    moves_dict = {} # {'e2e4': 0, 'f4f5': 3 ...}
    #populates dictionary
    for move in possible_moves:
        space_moving_to = move[2:] # 'a6'
        piece = board.lookupPiece(space_moving_to) #string
        piece = piece.lower()
        pieceValue = piece_values[piece] #int
        moves_dict[move] = pieceValue  #dictionary['new_key'] = value
    for key in moves_dict.keys():
        if moves_dict[key] == bestValue:
            return key


def runGame():
    global HumanNextMoves
    global AINextMoves

    turn_counter = 0
    print("Welcome to Chess AI")
    print('player is white (capital letters on bototm of board), AI is black (lowercase letters on top of board\n')
    print('Turn ' + str(turn_counter) + '\n')
    print(board)

    #print all the moves with print(chessgame.get_moves('b'))  player is (chessgame.state.player)
    # MAIN GAME LOOP
    #while not checkmate or stalemate
    while chessgame.status !=2 or chessgame.status != 3:
        #----------------------HUMAN MOVE-------------------------
        print(printplayer())
        move = input("move: ")

        #error handling for invalid move (ie. n2n3)
        ourPossibleMoves = chessgame.get_moves('w')
        if move in ourPossibleMoves:
            pass
        while move not in ourPossibleMoves:
            move = input("Enter a valid move: ")

        #white player (user) makes move
        chessgame.apply_move(move)
        board.updateBoard(str(chessgame))

        #----------------------AI MOVE-------------------------
        #after user makes move, AI needs to lookAhead
        #AI is the black player
        lookAhead('b')

        print('--------------------2----------------------')
        currFen = chessgame.get_fen()
        print("current: ", currFen)
        #everything's working up until this point

        #this handles setting humanNextMoves
        # lookAheadFen = chessgame.get_fen() #user's fen if user's move is made
        # print("lookAhead: ", lookAheadFen)
        # lookAheadFen = list(lookAheadFen)
        # print(lookAheadFen)
        # lookAheadFen[-13] = 'w' #sets player from black to white
        # print(lookAheadFen)
        # lookAheadFen = "".join(lookAheadFen)  #recreates fen
        # print(lookAheadFen)
        # chessgame.set_fen(lookAheadFen)
        #
        # HumanNextMoves = lookAhead('w')
        # chessgame.set_fen(currFen)


        AINextMoves = lookAhead('b')
        board.updateBoard(str(chessgame))
        turn_counter += 1
        print('\nTurn ' + str(turn_counter) + ' - white (player) moved\n')
        print(board)

        checkStatus()

        print("Thinking...\n")
        #time.sleep(3)
        ############### SCREWS UP HERE ##################

        ourPossibleMoves = chessgame.get_moves('b')
        #call minimax HERE
        for move in ourPossibleMoves:
            originNode = Node(move)
            originNode.children = HumanNextMoves[move]
            #minimax(originMove, depthLevel, maximizingPlayer)
            bestValue = minimax(move, 2, True)
            bestMove = findMoveBasedonValue(bestValue, 'b')
        move = bestMove
        print(move)
        #######move = random.choice(chessgame.get_moves())
        ##print('got past findbestMove!')
        ##print(move) ##### move should look something like this 'd7d6'
        chessgame.apply_move(move)
        board.updateBoard(str(chessgame))
        turn_counter += 1
        print('Turn ' + str(turn_counter) + ' - black (AI) moved\n')
        print(board)

runGame()
