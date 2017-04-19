from Chessnut import Game
from ChessBoard import *
import time
import random


class Game_Engine():
    def __init__(self, board_state):
        self.game = Game(board_state)
        self.computer = AI(self.game, 3)

    def prompt_user(self):
        #TO COMPLETE
        pass

class AI():
    def __init__(self, game, max_depth=3, leaf_nodes=[], num_nodes=0):
        self.game = game
        self.max_depth = max_depth
        self.leaf_nodes = leaf_nodes #TO COMPLETE
        self.num_nodes = num_nodes
        #add more about caches here

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


<<<<<<< HEAD
#print all the moves with print(chessgame.get_moves('b'))  player is (chessgame.state.player)
#while chessgame.status !=2 or chessgame.status != 3:
#
#    print(printplayer())
#    move = input("move: ")
#    chessgame.apply_move(move) 
#    board.updateBoard(str(chessgame))
#    print(board)
#
#    checkStatus()
#
#
#    print("Thinking...")
#    time.sleep(3)
#    move = random.choice(chessgame.get_moves())
#    chessgame.apply_move(move)
#    board.updateBoard(str(chessgame))
#    print(board)

    
    

=======
    print(printplayer())
    move = input("move: ")
    chessgame.apply_move(move)
    board.updateBoard(str(chessgame))
    print(board)

    checkStatus()


    print("Thinking...")
    time.sleep(3)
    move = random.choice(chessgame.get_moves())
    chessgame.apply_move(move)
    board.updateBoard(str(chessgame))
    print(board)
>>>>>>> 6244c8f4d06e05cd742b56361106d17dbd94dccc
