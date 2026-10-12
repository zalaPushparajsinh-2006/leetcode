class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        # If k == 0, every element qualifies
        if k == 0:
            return len(nums)
            
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)

        # Step 2: Find the threshold
        threshold = nums[n - k]

        # Step 3: Count all elements smaller than the threshold
        ans = 0
        for x in nums:
            if x < threshold:
                ans += 1

        return ans