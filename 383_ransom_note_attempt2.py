class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # print(ransomNote, magazine)
        ransomHash = {}
        magazineHash = {}

        for ransomLetter in ransomNote:
            if ransomLetter in ransomHash:
                ransomHash[ransomLetter] += 1
            else:
                ransomHash[ransomLetter] = 1

        for magazineLetter in magazine:
            if magazineLetter in magazineHash:
                magazineHash[magazineLetter] += 1
            else:
                magazineHash[magazineLetter] = 1

        print(ransomHash)
        print(magazineHash)








# ransomNote = "a"
# magazine = "b"
# >>> false

# ransomNote = "aa"
# magazine = "ab"
# >>> false

ransomNote = "aa"
magazine = "aab"
# >>> true


sol = Solution()
sol.canConstruct(ransomNote, magazine)
