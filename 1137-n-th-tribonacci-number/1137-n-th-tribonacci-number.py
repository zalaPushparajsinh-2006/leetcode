class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.solve( dp, n)
    def solve(self, dp, index):
        if index <= 1:
            return index
        if index == 2:
            return 1
        if dp[index] != -1:
            return dp[index]
        dp[index] = self.solve(dp, index-1) + self.solve(dp, index-2) + self.solve(dp, index-3)
        return dp[index]