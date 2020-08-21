class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem: return False
        nums.sort(reverse=True)
        dp, n = [0] * k, len(nums)

        def rec(i):
            if i == n:
                return len(set(dp)) == 1.  # Ideally the final array contains [target, target, target]
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target and rec(i + 1):  # recursion till we traverse whole array (nums)
                    return True
                dp[j] -= nums[i]  # returning to old state
                if not dp[j]: break
            return False

        return nums[0] <= target and rec(0)


obj = Solution()
#print(obj.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
print(obj.canPartitionKSubsets([4,15,1,1,1,1,3,11,1,10], 3))