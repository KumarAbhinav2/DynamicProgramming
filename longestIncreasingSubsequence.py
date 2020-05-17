"""
Find a subsequence in given array in which the subsequence's elements are in sorted order, lowest to highest, and in
which the subsequence is as long as possible.

Input = [3, 10, 2, 1, 20]
Output = [3, 10, 20]

Input = [50, 3, 10, 7, 40, 80]
Output = [3, 10, 40, 80]

"""
from duration import duration
import unittest
class Solution:

    @duration
    def intuitive(self, arr):
        res = [1]*len(arr)
        i, j = 1, 0
        subSeqIndices = [i for i in range(len(arr))]
        while i < len(arr) and j < len(arr):
            if arr[j] < arr[i]:
                if res[j] + 1 > res[i]:
                    res[i] = res[j] + 1
                    subSeqIndices[i] = j
            j +=1
            if j == i:
                j, i = 0, i+1
        max_value = max(subSeqIndices)
        max_index = subSeqIndices.index(max_value)
        next_index = max_index
        subSeq = []
        while True:
            subSeq.append(arr[next_index])
            old_index = next_index
            next_index = subSeqIndices[next_index]
            if next_index == old_index:
                break
        return max(res), subSeq

    @duration
    def better(self, arr):
        n = len(arr)
        T = [1 for _ in range(n)]
        solution_indices = [i for i in range(n)]

        for index_i in range(1, n):
            for index_j in range(0, index_i):
                if (arr[index_i] > arr[index_j]) and (T[index_i] < T[index_j] + 1):
                    T[index_i] = T[index_j] + 1
                    solution_indices[index_i] = index_j
        max_value = max(T)
        max_index = T.index(max_value)
        next_index = max_index
        subSeq = []
        while True:
            subSeq.append(arr[next_index])
            old_index = next_index
            next_index = solution_indices[next_index]
            if next_index == old_index:
                break

        return T[max_index], subSeq


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.input1 = [3, 10, 2, 1, 20]
        self.input2 = [50, 3, 10, 7, 40, 80]
        self.obj = Solution()

    def test_intuitive(self):
        res = self.obj.intuitive(self.input1)
        self.assertEqual(res[1], [3, 10, 20])
        res = self.obj.intuitive(self.input2)
        self.assertEqual(res[1], [3, 10, 40, 80])

    def test_better(self):
        res = self.obj.better(self.input1)
        self.assertEqual(res[1], [3, 10, 20])
        res = self.obj.better(self.input2)
        self.assertEqual(res[1], [3, 10, 40, 80])


if __name__ == '__main__':
        unittest.main()
