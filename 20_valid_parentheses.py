class Solution:
    def isValid(self, s: str) -> bool:
        # print(s)
        stack = []
        for char in s:
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            elif char == '}' and len(stack) >= 1:
                if stack.pop(-1) != '{' : return False
            elif char == ']' and len(stack) >= 1:
                if stack.pop(-1) != '[' : return False
            elif char == ')' and len(stack) >= 1:
                if stack.pop(-1) != '(' : return False
            else:
                stack.append(char)


        return len(stack) == 0


# s = "()"
# >>> true

# s = "()[]{}"
# >>> true

# s = "(]"
# >>> false

# s = "([)]"
# >>> false

# s = "[()]"
# >>> true

s = "]"
# >>> false

sol = Solution()
print(sol.isValid(s))
