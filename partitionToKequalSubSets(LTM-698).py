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

    def canPartitionKSubsets2(self, nums, k: int) -> bool:
        target, r = divmod(sum(nums), k)
        if r != 0:
            return False
        nums.sort(reverse=True)
        n = k
        s = 0
        while s < len(nums):
            if nums[s] < target:
                break
            elif nums[s] > target:
                return False
            else:
                n -= 1
            s += 1
        bins = [target] * n
        # remain = target * n
        def search(nums, s, bins, remain):
            if remain == 0:
                return True
            for i in range(len(bins)):
                if nums[s] <= bins[i]:
                    bins[i] -= nums[s]
                    if 0 < bins[i] < nums[-1]:
                        bins[i] += nums[s]
                        continue
                    if search(nums, s+1, bins, remain-nums[s]):
                        return True
                    bins[i] += nums[s]
            return False
        return search(nums, s, bins, target * n)


obj = Solution()
print(obj.canPartitionKSubsets2([4, 3, 2, 3, 5, 2, 1], 4))
#print(obj.canPartitionKSubsets([4,15,1,1,1,1,3,11,1,10], 3))