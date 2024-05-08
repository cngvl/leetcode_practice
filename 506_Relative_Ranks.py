# Constraints:
    # n == score.length
    # 1 <= n <= 104
    # 0 <= score[i] <= 106
    # All the values in score are unique.

class Solution:
   def findRelativeRanks(self, score: list[int]) -> list[str]:
        pass

sol = Solution()
score = [5,4,3,2,1]
sol.findRelativeRanks(score)
# >>> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

score = [10,3,8,9,4]
sol.findRelativeRanks(score)
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
