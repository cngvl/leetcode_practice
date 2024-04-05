# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Would this be considered to be a dynamic programming question?
# 'brute' force methoud would be to just loop through but then the issue comes with a variable number of digits being included
# Would this be considered to be more like a backtracking?¿


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        digToChar = { "2" : "abc",
                    "3" : "def",
                    "4" : "ghi",
                    "5" : "jkl",
                    "6" : "mno",
                    "7" : "pqrs",
                    "8" : "tuv",
                    "9" : "wxyz"}

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res

digits = "23"
# >>> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# digits = ""
# >>> []

# digits = "2"
# >>> ["a","b","c"]

sol = Solution()
sol.letterCombinations(digits)
