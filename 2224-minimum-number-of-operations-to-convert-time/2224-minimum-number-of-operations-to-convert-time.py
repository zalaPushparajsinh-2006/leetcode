class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currTime = 60 * int(current[0] + current[1]) + int(current[3] + current[4])
        targetTime = 60 * int(correct[0] + correct[1]) + int(correct[3] + correct[4])

        diff = targetTime - currTime
        res = 0

        for minute in [60, 15, 5, 1]:
            res += diff // minute
            diff %= minute

        return res