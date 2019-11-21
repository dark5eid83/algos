# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. 
# A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. 
# The given board represents the state of the game following the player's move. 
# Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# 1. If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
# 2. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
# 3. After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# 4. If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.

# Perform the above rules until the board becomes stable, then return the current board.



class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[list[int]]
        :rtype: List[List[int]]
        """

        R, C = len(board), len(board[0])
        changed = True

        while changed:
            changed = False

            for r in range(R):
                for c in range(C-2):
                    if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]) != 0:
                        board[r][c] = board[r][c+1] = board[r][c+2] = -abs(board[r][c])
                        changed = True

            for r in range(R-2):
                for c in range(C):
                    if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]) != 0:
                        board[r][c] = board[r+1][c] = board[r+2][c] = -abs(board[r][c])
                        changed = True

            for c in range(C):
                i = R-1
                for r in reversed(range(R)):
                    if board[r][c] > 0:
                        board[i][c] = board[r][c]
                        i -= 1
                for r in reversed(range(i+1)):
                    board[r][c] = 0

        return board
