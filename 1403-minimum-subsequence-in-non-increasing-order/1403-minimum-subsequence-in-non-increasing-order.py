class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        total = sum(nums)
        curr = 0
        ans = []
        for num in nums:
            curr += num
            ans.append(num)
            if curr > total - curr:
                return ans