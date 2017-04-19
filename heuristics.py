import ChessGame
import operator

piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 0}

def findBestMove(board, chessgame):
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

    moves_dict = {} #{'e2e4': 0, 'f4f5': 3 ...}
    for move in possible_moves:
        space_moving_to = move[2:]
        piece = board.lookupPiece() #string
        pieceValue = piece_values[piece] #int
        moves_dict[move] = pieceValue  #dictionary['new_key'] = value

    keyOfAMaxValue = max(moves_dict.iteritems(), key=operator.itemgetter(1))[0] #returns ie. 'e2e4'

    return keyOfAMaxValue
