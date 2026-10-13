class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = max(nums)
        return k*(2*n+k-1)//2