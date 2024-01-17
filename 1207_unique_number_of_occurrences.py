# Constraints:
    # 1 <= arr.length <= 1000
    # -1000 <= arr[i] <= 1000

# Seems like a stack + hash map solution
    # create a hashmap counting the number of each number's occurrence
    # loop through the hashmap and adding ONLY the keys to the stack?
    # if any dupe values can return false - might be another method to check for dupe vals?

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        countHash = {}
        checkingCounter = {}
        for num in arr:
            if num not in countHash:
                countHash[num] = 1
            else:
                countHash[num] += 1

        print(countHash)

        for key in countHash:
            if countHash[key] not in checkingCounter:
                checkingCounter[countHash[key]] = 1
            else:
                return False

        return True

    def uniqueOccurrences2(self, arr: list[int]) -> bool:
        countHash = {}
        checkingCounter = []
        for num in arr:
            if num not in countHash:
                countHash[num] = 1
            else:
                countHash[num] += 1

        for key in countHash:
            if countHash[key] not in checkingCounter:
                checkingCounter.append(countHash[key])

        return len(countHash) == len(checkingCounter)

# arr = [1,2,2,1,1,3]
# >>> true

# arr = [1,2]
# >>> false

arr = [-3,0,1,-3,1,1,1,-3,10,0]
# >>> true

sol = Solution()
print(sol.uniqueOccurrences(arr))
