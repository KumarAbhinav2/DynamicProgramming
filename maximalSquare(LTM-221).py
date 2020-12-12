"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's
and return its area.
Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
"""
class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1: return 0
        r = len(matrix)
        c = len(matrix[0])
        # dp matrix holding extra rws and cols for 0th row/col values updation
        dp = [[0]*(c+1) for _ in range(r+1)]
        # max value of a cell
        max_side = 0
        for row in range(r):
            for col in range(c):
                if matrix[row][col]=='1':
                    # checking for the combo, combo results to square if all four(top, diagonal and left)
                    # are 1 and that gives us 1 more sided square than original thats why 1 added at the end
                    # if not combo , will fall back to single side square because of added 1
                    dp[row+1][col+1] = min(dp[row][col], dp[row][col+1], dp[row+1][col])+1
                    # updating the max cell value, that will be the side of the max square
                    max_side = max(max_side, dp[row+1][col+1])
        return max_side*max_side

    # Time Complexity: O(rc). Single pass - row x col (r=row; c=col)
    # Space complexity : O(rc). Additional space for dp grid (don't need to worry about additional 1 row and col).