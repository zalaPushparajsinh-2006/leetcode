class Solution(object):
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]: return sorted(set(nums), reverse=True)[:k]