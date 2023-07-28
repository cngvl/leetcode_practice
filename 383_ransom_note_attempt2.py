class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomDict = {}
        magazineDict = {}

        for ransomLetter in ransomNote:
            if ransomLetter in ransomDict:
                ransomDict[ransomLetter] += 1
            else:
                ransomDict[ransomLetter] = 1

        for magazineLetter in magazine:
            if magazineLetter in magazineDict:
                magazineDict[magazineLetter] += 1
            else:
                magazineDict[magazineLetter] = 1

        for letter in ransomDict:
            if letter in magazineDict:
                magazineDict[letter] = magazineDict[letter] - ransomDict[letter]
            else:
                return False

        for letter in magazineDict:
            if magazineDict[letter] < 0:
                return False

        return True

# ransomNote = "a"
# magazine = "b"
# >>> false

ransomNote = "aa"
magazine = "ab"
# >>> false

# ransomNote = "aa"
# magazine = "aab"
# >>> true

sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
