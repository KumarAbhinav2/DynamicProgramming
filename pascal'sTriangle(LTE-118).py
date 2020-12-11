"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:

    def generate(self, numRows):
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]
            # property of pascal's triangle
            row[0], row[-1] = 1, 1
            # starting from 2nd and end before last
            for j in range(1, len(row)-1):
                # previous row every two elements , starting from first one
                row[j] = triangle[row_num-1][j-1]+triangle[row_num-1][j]
            triangle.append(row)
        return triangle

    # Time complexity: O(numRows^2)
    # Space complexity: O(numRows^2)

