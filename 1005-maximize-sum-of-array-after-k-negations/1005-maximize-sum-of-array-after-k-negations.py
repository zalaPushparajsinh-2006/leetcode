class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1

        if k % 2 == 1:
            nums.sort()
            nums[0] *= -1

        return sum(nums)