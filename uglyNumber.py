"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
"""
from duration import duration
import unittest

class Solution:

    def divide(self, a, b):
        while a % b == 0:
            a = a / b
        return a

    def isUgly(self, num):
        num = self.divide(num, 2)
        num = self.divide(num, 3)
        num = self.divide(num, 5)
        return 1 if num == 1 else 0

    @duration
    def intuitive(self, n):
        count = 1
        i  = 1
        while n > count:
            i +=1
            if self.isUgly(i):
                count +=1
        return i

    @duration
    def better(self, n):
        i2, i3, i5 = 0, 0, 0
        arr = [1] * n
        next_ugly = 1
        for i in range(1, n):
            next_ugly = min(2 * arr[i2], 3 * arr[i3], 5 * arr[i5])
            arr[i] = next_ugly
            if next_ugly == 2 * arr[i2]: i2 += 1
            if next_ugly == 3 * arr[i3]: i3 += 1
            if next_ugly == 5 * arr[i5]: i5 += 1
        return next_ugly


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = 15
        self.input2 = 150
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res, 24)
        res = self.obj.intuitive(self.input2)
        self.assertEqual(res, 5832)

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res, 24)
        res = self.obj.better(self.input2)
        self.assertEqual(res, 5832)


if __name__ == '__main__':
        unittest.main()




