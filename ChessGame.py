from Chessnut import Game
from ChessBoard import *
import random
from Node import Node

#This program models a game of chess with the help of ChessNut, and integrates a GUI and intelligent chess agent
#Authors: Elias Strizower, Henry Kwan, Alex Godziela

################ GLOBAL VARIABLES ########################################

board = ChessBoard(8,8)
## chessgame = Game() # use this for a NEW GAME, use a fen generator for testing
chessgame = Game()

HumanNextMoves = {} #Dictionary that will hold 2 ply of the human player's next moves
AINextMoves = {} #Dictionary that will hold 2 ply of the AI's next moves
board.updateBoard(str(chessgame))

#This functions checks whether a player is in check, checkmate, or stalemate
def checkStatus():
    if chessgame.status == 1:
        print("CHECK")
    if chessgame.status == 2:
        print("CHECKMATE")
        print("GAME OVER")
    if chessgame.status ==3:
        print("STALEMATE")

#This function prints the player whose current turn it is
def printplayer():
    if chessgame.state[0] == 'w':
        return "White"
    else:
        return "Black"

#This function implements the minimax algorithm
def minimax(node, depth, maximizingPlayer):
    if depth == 0 or node.leaf == True:
        heuristicValue = findBestMove('b')  #best move for AI
        return heuristicValue

    #maximizingPlayer -AI
    if maximizingPlayer:
        bestValue = -1 * float('inf')
        for child in node.children:
            v = minimax(Node(child), depth-1, False)
            bestValue = max(bestValue,v)

    #minimizingPlayer- human
    else:
        bestValue = float('inf')
        for child in node.children:
            v = minimax(Node(child), depth-1, True)
            bestValue = min(bestValue,v)

    return bestValue


#this function is simply a heuristic to get the move with the highest point value
def findBestMove(player):
    possible_moves = chessgame.get_moves(player)

    #updates dictionary
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 200, ' ': 0}
    moves_dict = {} # {'e2e4': 0, 'f4f5': 3 ...}
    for move in possible_moves:
        space_moving_to = move[2:] # 'a6'
        piece = board.lookupPiece(space_moving_to) #string
        piece = piece.lower()
        pieceValue = piece_values[piece] #int
        moves_dict[move] = pieceValue  #dictionary['new_key'] = value

    #find key of max value in dictionary
    bestMove = 0 #returns ie. 'e2e4'
    goodMovesArray = []
    maxValue = 0
    for key in moves_dict:
        if moves_dict[key] > maxValue:
            goodMovesArray += [key]
            maxValue = moves_dict[key]
    return maxValue


'''Comments for how findBestMove works

# finds all possible moves at moment for AI
# returns an array of every move you can possible make at the moment
# each array element is of the form 'e2e4' where the first two characters are where you ar moving from
# and the second two characters are where you are moving to

# parse what is on each of the spaces in possible_moves (piece or no piece)
# possible_moves example = ['e2e4', 'f2f4', etc]
# check in second half of string if empty space or piece
# if empty space 0 points, if piece get piece value from above
# store move and point value for each move into moves_dict (dictionary)



############################### 1-PLY #####################################
##    evaluation = 0
##    evaluation = maxi(0)

######## everything below here in this function is basically the "evaluate()" function needed above....


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
'''

#This function generates a dictionary where the keys are the 1 ply moves, and the value at the key are the 2 ply moves that stem from the key move
def lookAhead(player):
    #create dictionary for 2-ply moves
    secondLayerMoves = {}

    currentFen = chessgame.get_fen()

    for move in chessgame.get_moves(player):
        #each current move is going to be a key for the above dictionary
        secondLayerMoves[move] = []
    for move in chessgame.get_moves(player):
        chessgame.apply_move(move)
        secondLayerMoves[move] += chessgame.get_moves(player)
        chessgame.set_fen(currentFen)
    return secondLayerMoves

#This function is a helper function that is used to change the player from 'b' to 'w' in the FEN. It is neccesary to lookahead 2 ply since ChessNut presents issues in doing so
def changeFenWB(lookAheadFen):
    for x in range(5,20):
        if lookAheadFen[-x] == 'b' and lookAheadFen[-x+1] == ' ' and lookAheadFen[-x-1] == ' ':
            lookAheadFen[-x] = 'w'
            break
    return lookAheadFen

#This function returns point value for specific move, used for white player only
def findMoveValue(move):
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 200, ' ': 0}
    space_moving_to = move[2:] # 'a6'
    piece = board.lookupPiece(space_moving_to) #string
    piece = piece.lower()
    pieceValue = piece_values[piece] #int
    return pieceValue

#This function finds a key (move) based on value (points)
def findMoveBasedonValue(bestValue, player):
    piece_values = {'p': 1, 'b': 3, 'n': 3, 'r': 5, 'q': 9, 'k': 200, ' ': 0}

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

#This function implements a minimax AI to play against
def MinimaxAgent():
        ourPossibleMoves = chessgame.get_moves('b')
        for move in ourPossibleMoves:
            originNode = Node(move)
            for key in HumanNextMoves:
                originNode.children = HumanNextMoves[key]
            originNode.setIsLeaf() #sets isLeaf equal to false or true depending on if node has children
            bestValue = minimax(originNode, 2, True)
            bestMove = findMoveBasedonValue(bestValue, 'b')
        move = bestMove
        return bestMove

#This function implements a 1 ply random move AI to play against
def RandomMoveAgent():
     ourPossibleMoves = chessgame.get_moves('b')
     move = random.choice(ourPossibleMoves)
     return move

#This function implements a 1 ply best move AI to play against
def BestMoveAgent():
     ourPossibleMoves = chessgame.get_moves('b')
     bestMoveValue = findBestMove('b')
     bestMove = findMoveBasedonValue(bestMoveValue,'b')
     return bestMove

#This function is called to determine the correct agent that the user selected to play against
def agentMove(agent):
    if agent == "1":
        return RandomMoveAgent()
    elif agent == "2":
        return BestMoveAgent()
    elif agent == "3":
        return MinimaxAgent()

#This function runs the sets up the game and runs it by assigning an ai, taking user input as moves, and displayin the GUI
def runGame():
    global HumanNextMoves
    global AINextMoves

    whiteValue = 0
    blackValue = 0

    turn_counter = 0
    print("\n\n\nWelcome to Chess AI")
    print('Player is white (capital letters on bottom of board), AI is black (lowercase letters on top of board\n')
    print('Instructions: \nEnter move as: \ncurrent position + next position \nExample: e2e4 -> piece moves from e2 to e4 \n\nWhen move requires pawn promotion enter move as: \ncurrent position + next position + piece pawn is promoted to \nExample: a7a8b -> piece moves from a7 to a8 and turns into bishop\n\n')

    #Determine what chess agent the player wants to play against
    agent = input("What chess agent do you want to play against?\n(1 = easy (1-Ply Random Move), 2 = medium (1-Ply Best Move), 3 = hard (2-Ply Minimax)\nEnter (1,2,or 3): ")
    if agent == "1" or agent == "2" or agent == "3":
        pass
    else:

        while True:
            agent = str(input("Error: Please Choose Agent [1 = easy (1 Ply Random Move) , 2 = medium (1 Ply Best Move), 3 = hard (2 Ply Minimax)]\n"))
            if agent == "1":
                break
            elif agent == "2":
                break
            elif agent == "3":
                break



    print('Turn ' + str(turn_counter) + '\n')
    print("White Score: " +  str(whiteValue))
    print("Black Score: " +  str(blackValue) + '\n')


    print(board)



    #print all the moves with print(chessgame.get_moves('b'))  player is (chessgame.state.player)
    # MAIN GAME LOOP
    #while not checkmate or stalemate
    while chessgame.status !=2 or chessgame.status != 3:
        #----------------------HUMAN MOVE-------------------------
        print(printplayer())
        move = input("move: ")

        #error handling for invalid move (ie. n2n3)
        ourPossibleMoves = chessgame.get_moves('w')   #What is this??
        if move in ourPossibleMoves:
            pass
        while move not in ourPossibleMoves:
            print("Valid Moves: ")
            print(ourPossibleMoves)
            move = input("Enter a valid move: ")


        #white player (user) makes move
        whiteValue += findMoveValue(move) #Keeps track of how many points the white (human) player has
        chessgame.apply_move(move) #Applies the move to the board
        board.updateBoard(str(chessgame)) #Updates the GUI



        #this handles setting humanNextMoves. ChessNut makes it very difficult to lookahead after you make your turn. This gets around that issue by saving the FEN, creating an artificial fen to get next moves, then resetting the original FEN
        currFen = chessgame.get_fen()
        lookAheadFen = chessgame.get_fen() #user's fen if user's move is made
        lookAheadFen = list(lookAheadFen)
        changeFenWB(lookAheadFen)
        lookAheadFen = "".join(lookAheadFen)  #recreates fen
        chessgame.set_fen(lookAheadFen)
        HumanNextMoves = lookAhead('w') #generates a dictionary with 2 ply of the next possible moves
        chessgame.set_fen(currFen)

        #----------------------AI MOVE-------------------------
        #after user makes move, AI needs to lookAhead
        #AI is the black player
        lookAhead('b') #generates a dictionary with 2 ply of the next possible moves
        AINextMoves = lookAhead('b')
        board.updateBoard(str(chessgame))
        turn_counter += 1
        print('\nTurn ' + str(turn_counter) + ' - white (player) moved\n')
        print("White Score: " +  str(whiteValue))
        print("Black Score: " +  str(blackValue) + '\n')
        print(board)
        checkStatus() #checks whether there is a check, checkmate, or stalemate, and prints the corresponding message
        print("AI is thinking...\n")


        move = agentMove(agent)  #AI move based on what agent was selected

        blackValue += findMoveValue(move)  #Keeps track of how many points the black (AI) player has
        chessgame.apply_move(move) #Applies the move to the board
        board.updateBoard(str(chessgame)) #Updates the GUI
        turn_counter += 1
        print('Turn ' + str(turn_counter) + ' - black (AI) made move ' + move + '\n')
        print("White Score: " +  str(whiteValue))
        print("Black Score: " +  str(blackValue) + '\n')
        print(board)



runGame()
