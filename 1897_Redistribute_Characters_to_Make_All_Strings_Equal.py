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
        lengthTotal = 0
        for word in words:
            lengthTotal += len(word)

        averageLength = lengthTotal // len(words) # What if I get an odd value?
        # print(averageLength)

        shortWord = ''
        longWord = ''

        for word in words:
            if len(word) == averageLength - 1:
                shortWord = word
            elif len(word) == averageLength + 1:
                longWord = word

        shortWordHash = {}
        for letter in shortWord:
            if letter not in shortWordHash:
                shortWordHash[letter] = 1
            else:
                shortWordHash[letter] += 1

        longWordHash = {}
        for letter in longWord:
            if letter not in longWordHash:
                longWordHash[letter] = 1
            else:
                longWordHash[letter] += 1

        # print(shortWord)
        if len(shortWord) == len(longWord):
            return False
        # print(longWord)

        # longWordHashDupe = longWordHash
        # shortWordHashDupe = shortWordHash


        print('')

        for letter in longWordHash:
            # print(letter)
            if letter not in shortWordHash:
                shortWordHash[letter] = 1
                longWordHash[letter] -= 1
            elif longWordHash[letter] > shortWordHash[letter]:
                shortWordHash[letter] += 1
                longWordHash[letter] -= 1

        print('')

        if longWordHash == shortWordHash:
            return True
        else:
            return False





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
