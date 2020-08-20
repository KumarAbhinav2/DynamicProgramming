"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
"""


class Solution:

    d= {}
    def tribonacci1(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        if n not in self.d.keys():
            self.d[n] = self.tribonacci1(n-1)+self.tribonacci1(n-2)+self.tribonacci1(n-3)
        return self.d[n]

    def tribonacci2(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for i in range(n):
            a, b, c = b, c, a+b+c
        return a

