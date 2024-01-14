# Constraints:
    # 1 <= s.length <= 105
    # s consists of only lowercase English letters.


# First thought is to use some stack?
    # can also use append pop method
        # might be sketchy if there's more than 2 instances of the letter
# Might also be able to use a hashMap
    # First loop through all the letters and add the number of occurances as a keyval pair
    # return the first key with a val of 1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        seenDict = {}
        for char in s:
            if char not in seenDict:
                seenDict[char] = 1
            else:
                seenDict[char] += 1

        print(seenDict)

        for key in seenDict:
            if seenDict[key] == 1:
                print(f"returning {s.index(key)} for the letter {key}")
                return s.index(key)

        print("returning -1 ")
        return -1

# s = "leetcode"
# >>>  0

# s = "loveleetcode"
# >>>  2

s = "aabb"
# >>> -1



sol = Solution()
sol.firstUniqChar(s)
