# Constraints:
    # 1 <= strs.length <= 200
    # 0 <= strs[i].length <= 200
    # strs[i] consists of only lowercase English letters.

# Second attempt at this question but remember the general solution to solving the q
# Need to iterate through all the words in str at the same time
# First attempt used a stack method but there might be a way to solve without it to reduce mem need

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minLength = len(strs[0])
        returnString = ''
        for word in strs:
            minLength = min(minLength, len(word))

        # print(minLength)
        for letterPos in range(minLength):
            smallStack = []
            for word in strs:
                if word[letterPos] not in smallStack:
                    smallStack.append(word[letterPos])
            if len(smallStack) > 1:
                print(returnString)
            else:
                returnString += smallStack[0]

        print(returnString)

sol = Solution()
# strs = ["flower","flow","flight"]
# sol.longestCommonPrefix(strs)
# >>> "fl"

# strs = ["dog","racecar","car"]
# sol.longestCommonPrefix(strs)
# >>> ""

# Failed test case
strs = [""]
sol.longestCommonPrefix(strs)
# >>> ""

strs = ["a"]
sol.longestCommonPrefix(strs)
# >>> "a"

strs = ["a", "ab"]
sol.longestCommonPrefix(strs)
# >>> "a"

strs = ["cir","car"]
sol.longestCommonPrefix(strs)
# >>> "c"
