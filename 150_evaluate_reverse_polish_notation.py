# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

# Initial issue is that the items within the list are all strings and aren't operators or ints
    # Might make a hashmap for this?
# After this step I should be able to do the logic of just taking the [-1] and [-2] indexed items from the stack and doing the math operations on them
#


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        numberStack = []

        operationHash = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),
        }

        for item in tokens:
            if item == "/" or item == "+" or item == "-" or item == "*":
                operationValue = operationHash[item](numberStack[-2], numberStack[-1])
                numberStack[-2] = (operationHash[item](numberStack[-2], numberStack[-1]))
                numberStack.pop()
            else:
                numberStack.append(int(item))

        return int(numberStack[0])




# tokens = ["2","1","+","3","*"]
# >>> 9

# tokens = ["4","13","5","/","+"]
# >>> 6

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# >>> 22

sol = Solution()
print(sol.evalRPN(tokens))
