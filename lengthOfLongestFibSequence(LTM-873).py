"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence,
find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements
(including none) from A, without changing the order of the remaining elements.
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)



Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
"""

import collections as c


class Solution:

    def lenLongestFibSubseq1(self, A) -> int:
        s = set(A)
        n = len(A)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                x, y = A[j], A[i]+A[j]
                length = 2
                while y in s:
                    x, y = y, x+y
                    length +=1
                count = max(count, length)
        return count if count >= 3 else 0

    def lenLongestFibSubseq2(self, A):
        index = {x: i for i, x in enumerate(A)}
        longest = c.defaultdict(lambda: 2)

        ans = 0
        for k, z in enumerate(A):
            for j in range(k):
                i = index.get(z - A[j], None)
                if i is not None and i < j:
                    cand = longest[j, k] = longest[i, j] + 1
                    ans = max(ans, cand)

        return ans if ans >= 3 else 0

obj = Solution()
obj.lenLongestFibSubseq2([1,3,7,11,12,14,18])