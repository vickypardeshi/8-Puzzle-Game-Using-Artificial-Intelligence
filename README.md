# 9Tiles-Puzzle-Game-in-Artificial-Intelligence


Run:
	python3 9TilesPuzzle.py


How to implement 9TilePuzzle program in AI:

Initial State = randomally created matrix ( ['1','2','3','4','5','6','7','8','-'] ) 
Goal State = ['1','2','3','4','5','6','7','8','-']

1)Generate 3*3 matrix GUI
2)Randomally swap all numbers(0-8) in matrix
3)Start game for solving puzzle
4)Create heuristic function to calculate Manhattan distance
Heuristic Function : The sum of distance of tiles from their goal position
5)Create all possible state space in each state of moving a tile
6)Take minimum heuristic function (min Manhattan distance) state & solve
7)Follow step 4 to 6 till we reach to goal state
