# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        print(tokens)

tokens = ["2","1","+","3","*"]
# >>> 9

# tokens = ["4","13","5","/","+"]
# >>> 6

# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# >>> 22

sol = Solution()
sol.evalRPN(tokens)
