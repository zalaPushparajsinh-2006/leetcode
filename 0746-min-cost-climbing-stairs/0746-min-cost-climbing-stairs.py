class Solution:
    def minCostClimbingStairs(self, nums: list[int]) -> int:
        for i in range(2, len(nums)):
            nums[i] += min(nums[i-1], nums[i-2])
        return min(nums[-1], nums[-2])