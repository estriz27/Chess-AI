# Chess AI, an intelligent chess agent that you can play against!
### By Henry Kwan, Elias Strizower, and Alex Godziela

What is Chess?


For those who may not be as familiar with the board game, Chess is a two-player perfect information game played on an 8x8 grid. Each player begins with 16 pieces: 8 pawns, 2 knights, 2 bishops, 2 rooks, 1 queen, and 1 king. These pieces are set up at opposite sides of the board and the goal is to place the opponent's king under checkmate, meaning that it is unable to get itself to a safe place where it is not being attacked. In certain cases, a game of chess will end in a draw, also known as a stalemate, where neither player is able to checkmate the opponent. With that being said, the goal of our Chess AI is to win games; it will only draw if necessary.

What is our project?


We built a Chess AI that is an artificially intelligent computer that optimizes its moves real time in order to win a chess game against a human player.

## Getting Started

Our project is located at [Henry's chess-AI GitLab Repo](https://gitlab.bucknell.edu/hbk001/chess-AI). It can be cloned using

```
git@gitlab.bucknell.edu:hbk001/chess-AI.git
```

### Instructions

Player - white (capital letters on bottom of board)
AI - black (lowercase letters on top of board)

* Open a terminal window
* Type into terminal
```
python3 ChessGame.py
```

* Choose the chess agent that you want to play against: Enter "1" for easy (1 Ply Random Move) "2" for medium (1 Ply Best Move) "3 for hard (2 Ply Minimax)
```
Example: What chess agent do you want to play against?(1 = easy (1 Ply Random Move) , 2 = medium (1 Ply Best Move), 3 = hard (2 Ply Minimax)
3
```

* Enter move as current position + next position
```
Example: e2e4 -> piece moves from e2 to e4
```

* When move requires pawn promotion (pawn reaches end of board), enter move as:
* current position + next position + piece pawn is promoted to
```
Example: a7a8b -> piece moves from a7 to a8 and turns into bishop
```

### Algorithm

Iteration 1
* AI makes random moves (this was a vital first step so that a player can play against the AI)


Iteration 2
* Implemented basic heuristics
* Each move is assigned a point value
* AI makes move with highest point value (Kind of like a Greedy Algorithm)


Iteration 3
* Minimax Algorithm - maximizes AI point value and minimizes opponent's point value based on AI's move
* 2-ply deep (Depth of 2)
* Looks 2 moves ahead to pick best move

## Built With

* Python
* Blood
* Sweat
* Tears

## Authors

* **Henry Kwan**
* **Elias Strizower**
* **Alex Godziela**


## License

Top Security Clearance Needed


## Acknowledgments

* Shoutout to [MIT](https://github.com/lamesjim/Chess-AI)
