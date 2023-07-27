# Constraints:
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print(ransomNote, magazine)


# ransomNote = "a"
# magazine = "b"
# >>> false

# ransomNote = "aa"
# magazine = "ab"
# >>> false

# ransomNote = "aa"
# magazine = "aab"
# >>> true
