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

chessgame = Game()
board = ChessBoard(8,8)
board.updateBoard(str(chessgame))

print("Welcome to Chess AI")
print(board)

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


def findBestMove(board, chessgame):
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 0, ' ': 0}
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
    #updates dictionary
    moves_dict = {} #{'e2e4': 0, 'f4f5': 3 ...}
    for move in possible_moves:
        #print(move) # 'b8a6'
        space_moving_to = move[2:] # 'a6'
        #print('this is space_moving_to: ' + space_moving_to)
        piece = board.lookupPiece(space_moving_to) #string
        piece = piece.lower()
        #print('piece: ', str(piece))
        pieceValue = piece_values[piece] #int
        moves_dict[move] = pieceValue  #dictionary['new_key'] = value

    #find key of max value in dictionary
    maxKey = 0 #returns ie. 'e2e4'
    for key in moves_dict:
        maxValue = 0
        if moves_dict[key] > maxValue:
            maxKey = key
            maxValue = moves_dict[key]
    print('keyOfAMaxValue: ' + str(maxKey))
    if str(maxKey) == '0':
        #print('DOES IT GET HERE?')
        maxKey = random.choice(chessgame.get_moves())
    return str(maxKey)



#print all the moves with print(chessgame.get_moves('b'))  player is (chessgame.state.player)
while chessgame.status !=2 or chessgame.status != 3:

    print(printplayer())
    move = input("move: ")
    #error handling for invalid move (ie. n2n3)
    column = move[2]
    row = move[3]
    if column > 'g' or row > '8':
        move = input("Enter a valid move: ")
    chessgame.apply_move(move)
    board.updateBoard(str(chessgame))
    print(board)

    checkStatus()

    print("Thinking...")
    #time.sleep(3)
    ############### SCREWS UP HERE ##################
    move = findBestMove(board, chessgame)
    #######move = random.choice(chessgame.get_moves())
    #print('got past findbestMove!')
    print(move) ##### move should look something like this 'd7d6'
    chessgame.apply_move(move)
    board.updateBoard(str(chessgame))
    print(board)
