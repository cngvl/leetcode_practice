# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

# Would this be considered to be a dynamic programming question?
# 'brute' force methoud would be to just loop through but then the issue comes with a variable number of digits being included
# Would this be considered to be more like a backtracking?¿


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pass


digits = "23"
# >>> ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# digits = ""
# >>> []

# digits = "2"
# >>> ["a","b","c"]

sol = Solution()
sol.letterCombinations(digits)
