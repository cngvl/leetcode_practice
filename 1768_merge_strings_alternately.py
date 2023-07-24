# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(word1, word2)





word1 = "abc"
word2 = "pqr"
# >>> "apbqcr"

# word1 = "ab"
# word2 = "pqrs"
# >>> "apbqrs"

# word1 = "abcd"
# word2 = "pq"
# >>> "apbqcd"

sol = Solution()
sol.mergeAlternately(word1, word2)
