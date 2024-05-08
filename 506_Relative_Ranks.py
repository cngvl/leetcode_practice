# Constraints:
    # n == score.length
    # 1 <= n <= 104
    # 0 <= score[i] <= 106
    # All the values in score are unique.

# Easy solution would be to create a dupe score list that's sorted
# create a hash to map the values back to the placement val - works because the scores unique
# loop through the original score list and then append the appropriate statement back to returnlist
# The weirdbit is how to sort out the placements
    # Use of stack and then popping?

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        returnList = []
        placementHash = {}
        sortedScore = score[:]
        sortedScore.sort(reverse=True)

        for placement in range(len(score)):
            if placement == 0:
                placementHash[sortedScore[placement]] = 'Gold Medal'
            elif placement == 1:
                placementHash[sortedScore[placement]] = 'Silver Medal'
            elif placement == 2:
                placementHash[sortedScore[placement]] = 'Bronze Medal'
            else:
                placementHash[sortedScore[placement]] = f'{placement + 1}'

        for val in score:
            returnList.append(placementHash[val])

        print('x')
        return returnList

sol = Solution()
# score = [5,4,3,2,1]
# sol.findRelativeRanks(score)
# >>> ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

score = [10,3,8,9,4]
sol.findRelativeRanks(score)
# ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
