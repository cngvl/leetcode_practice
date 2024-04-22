# Constraints:
    # 1 <= s.length <= 5 * 104
    # t.length == s.length
    # s and t consist of any valid ascii character.

# Second attempt at this question
# Don't exactly recall the solution from first attempt but question seems not too bad
# Create a hashMap for both input strings and then compare the two after
    # The vals should be the same for both hashMaps but not sure how to compare
    # What if the order for the keyvals are different?

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}
        comparisonHash = {}

        for char in s:
            if char not in sHash:
                sHash[char] = 1
            else:
                sHash[char] += 1
        print(sHash)

        for char in t:
            if char not in tHash:
                tHash[char] = 1
            else:
                tHash[char] += 1
        print(tHash)

        if len(sHash) != len(tHash):
            # return False
            print('False')

        for sChar, tChar in zip(s, t):
            if sChar not in comparisonHash:
                comparisonHash[sChar] = tChar
            else:
                if comparisonHash[sChar] != tChar: print('False in comparisonCheck')

        for sChar, tChar in zip(sHash, tHash):
            # print(sChar, tChar)
            if sHash[sChar] != tHash[tChar]:
                print('False')

        # print('x')
        print('True')

    def isIsomorphicNeetCode(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}
        for c1, c2 in zip(s,t):
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1

        return True


sol = Solution()

# s = "egg"
# t = "add"
# sol.isIsomorphic(s, t)
# >>> true

# s = "foo"
# t = "bar"
# sol.isIsomorphic(s, t)
# >>> false

# s = "paper"
# t = "title"
# sol.isIsomorphic(s, t)
# >>> true

# Failed test case - Counter solution isn't enough, each char needs to be a 1 to 1 switch.
# Should I map each letter to its counterpart?
s = "bbbaaaba"
t = "aaabbbba"
sol.isIsomorphic(s, t)
