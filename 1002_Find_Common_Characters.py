# Constraints:
    # 1 <= words.length <= 100
    # 1 <= words[i].length <= 100
    # words[i] consists of lowercase English letters.

# Will need to iterate through each word and then map out each of those words?
    # Will have at most 100 words
# Not sure how to store the hashes for individal words?
    # Can make list of hashes

# How do I check if all the elements in the list have the same elements

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        allWords = []
        commonChars = []
        for word in words:
            wordHash = {}
            for letter in word:
                if letter in wordHash:
                    wordHash[letter] += 1
                else:
                    wordHash[letter] = 1

            allWords.append(wordHash)
            wordHash = {}


        print('x')

    def commonChars2(self,words: list[str]) -> list[str]:
            #output
        output = []
        intercept = {}
        #find the letters in the first word to  use as a starter
        for letter in words[0]:
            intercept[letter]  = intercept.get(letter, 0) + 1

        #begin from the second word and check their letter
        for index in range(1,len(words)):
            #create a new intercept that matches with the coming word
            newIntercept = {}
            for letter in words[index]:
                if letter in intercept:
                    if intercept[letter] > 0:
                        newIntercept[letter] = newIntercept.get(letter,0) + 1
                    intercept[letter] -= 1

            #replace the intercept with the new Intercept
            intercept = newIntercept

        #add all the letters as much as their apperance aka count
        for letter, count in intercept.items():
            for i in range(count):
                output.append(letter)

        #return the list version of the array
        return output


words = ["bella","label","roller"]
# >>> ["e","l","l"]

# words = ["cool","lock","cook"]
# >>> ["c","o"]

sol = Solution()
sol.commonChars2(words)

# class Solution:
#     def commonChars(self, words: list[str]) -> list[str]:
#         subsequentWords = {}
#         commonChars = []
#         for word in words[0]:
#             firstWord = {}
#             for letter in word:
#                 if letter in firstWord:
#                     firstWord[letter] += 1
#                 else:
#                     firstWord[letter] = 1

#         for word in words[1:]:
#             for letter in word:
#                 # if letter
#                 pass
