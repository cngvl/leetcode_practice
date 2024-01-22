# Constraints:
    # 2 <= s.length <= 1000
    # s.length is even.
    # s consists of uppercase and lowercase letters.

# Will need to standardise input
# Make a vowel hash
# Do one loop for counting each half
# and then need a comparison loop

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # vowelHash = {}
        vowelList = ["a","e","i","o","u"]
        firstHash = {
            "vowel": 0,
            "constant": 0
        }

        secondHash = {
            "vowel": 0,
            "constant": 0
        }

        s = s.lower()
        firstHalf = s[0:len(s)//2]
        secondHalf = s[len(s)//2:]

        for letter in firstHalf:
            if letter in vowelList:
                firstHash["vowel"] += 1
            else:
                firstHash["constant"] += 1

        for letter in secondHalf:
            if letter in vowelList:
                secondHash["vowel"] += 1
            else:
                secondHash["constant"] += 1


        return firstHash == secondHash

# s = "book"
# >>> true

s = "textbook"
# >>> false

sol = Solution()
sol.halvesAreAlike(s)
