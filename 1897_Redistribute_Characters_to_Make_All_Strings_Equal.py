# Constraints:
    # 1 <= words.length <= 100
    # 1 <= words[i].length <= 100
    # words[i] consists of lowercase English letters.

# Need to count all the elements in words?
    # CANT track the most common string
    # Use the average length of string?

# I don't think I necessarily need to make the strings identical, just need to make their counts the same?

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        totalLetterHash = {}

        for word in words:
            for letter in word:
                if letter in totalLetterHash:
                    totalLetterHash[letter] += 1
                else:
                    totalLetterHash[letter] = 1

        for letter in totalLetterHash:
            if totalLetterHash[letter] % len(words) != 0:
                return False

        print('')

        return True






# words = ["abc","aabc","bc"]
# >>> true

# words = ["ab","a"]
# >>> false

# words = ["abc","aabc","bc","abc","abc","abc","abc"]
# >>> true

words = ["a","b"]
# >>> false

sol = Solution()
sol.makeEqual(words)
