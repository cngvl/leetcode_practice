# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

# Can use #zip function to loop through both strings at the same time but can also just do a position counter
    # how to account for remaining letters
    # might need to do a manual counter method
# Starting with word1
# Stack question

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # x = (zip(word1, word2))
        # print(tuple(x))
        s = ''
        counter = 0
        for x,y in zip(word1, word2):
            counter += 1
            s += x
            s += y

        if counter < len(word1):
            s += word1[counter:]

        if counter < len(word2):
            s += word2[counter:]

        return s

# word1 = "abc"
# word2 = "pqr"
# >>> "apbqcr"

word1 = "ab"
word2 = "pqrs"
# >>> "apbqrs"

# word1 = "abcd"
# word2 = "pq"
# >>> "apbqcd"

sol = Solution()
sol.mergeAlternately(word1, word2)
