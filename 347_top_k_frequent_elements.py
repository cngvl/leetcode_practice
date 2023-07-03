# Constraints:
    # 1 <= nums.length <= 10^5
    # -10^4 <= nums[i] <= 10^4
    # k is in the range [1, the number of unique elements in the array].
    # It is guaranteed that the answer is unique.
    # Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# My notes
    # The hint of returning the answer in any order implies that there doesn't need to be any sorting?
    # I still think I should sort out the array though but I'm not sure if it has any point in simplifying the process
    # I can run some sort of HashMap with the value and frequency as key value pairs

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # print(list, k)
        # print(sorted(nums))
        # print(nums.sort)
        # nums.sort
        numberHash = {}
        for num in nums:
            if num not in numberHash:
                numberHash[num] = 1
            else:
                numberHash[num] += 1

        sortedNumberHash = sorted(numberHash.items(), key=lambda x:x[1], reverse = True)
        # print(sortedNumberHash)

        returnArray = []
        i = 0
        while len(returnArray) < k:
            returnArray.append(sortedNumberHash[i][0])
            i += 1

        return returnArray




nums = [1,1,1,2,2,3]
k = 2
# >>> [1,2]

# nums = [1]
# k = 1
# >>> [1]

# nums = [1,2,2,2,2,2,2,3,3]
# k = 2
# >>> [2,3]

s = Solution()
print(s.topKFrequent(nums, k))
