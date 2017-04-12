from Chessnut import Game
from ChessBoard import *


    
chessgame = Game()
board = ChessBoard(8,8)
board.updateBoard(str(chessgame))
print(board)

#print(chessgame)  # 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'

#print(chessgame.get_moves())
"""
['a2a3', 'a2a4', 'b2b3', 'b2b4', 'c2c3', 'c2c4', 'd2d3', 'd2d4', 'e2e3', 
 'e2e4', 'f2f3', 'f2f4', 'g2g3', 'g2g4', 'h2h3', 'h2h4', 'b1c3', 'b1a3', 
 'g1h3', 'g1f3']
"""

chessgame.apply_move('e2e4')  # succeeds!
board.updateBoard(str(chessgame))
print(board)
#print(chessgame)  # 'rnbqkbnr/ pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1'

chessgame.apply_move('b7b6')  # fails! (raises InvalidMove exception)

board.updateBoard(str(chessgame))
print(board)
