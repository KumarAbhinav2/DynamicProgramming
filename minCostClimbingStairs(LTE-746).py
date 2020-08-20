"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to
reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""

class Solution:

    def minCostClimbingStairs1(self, cost) -> int:
        # base cases
        # F(n) = C(n)+min(F(n-1)+F(n-2))
        c1, c2 = cost[0], cost[1]
        for i in range(2,len(cost)):
            c1, c2 = c2, cost[i] + min(c1,c2)
        return min(c1, c2)

    def minCostClimbingStairs2(self, cost) -> int:
        # base cases
        # F(n) = C(n)+min(F(n-1)+F(n-2))
        if not cost:
            return 0
        n = len(cost)
        dp = [0]*(n)
        dp[0] = cost[0]
        if n>=2:
            dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1], dp[-2])

    def minCostClimbingStairs3(self, cost) -> int:
        # base cases
        # F(n) = C(n)+min(F(n-1)+F(n-2))
        c1 = c2 = 0
        for c in reversed(cost):
            c1, c2 = c+min(c1,c2), c1
        return min(c1,c2)