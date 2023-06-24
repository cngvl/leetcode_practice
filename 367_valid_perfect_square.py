# Constraints:
# You must not use any built-in library function, such as sqrt.
# 1 <= num <= 231 - 1

# Hard coded values seem like a mad stupid idea but not sure how else to tackle the question.
# This is a binary serch question but I still have no clue how to go about this
# I could do some while loop with a counter that has a square but that seems like a jank method to solve it

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        counter = 0
        while counter ** 2 <= num:
            print(counter ** 2)
            if counter ** 2 == num:
                return True
            counter += 1
        return False


# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         for i in range(1, num+1):
#             if i * i == num:
#                 return True
#             if i * i > num:
#                 return False

# num = 16
# >>> true

num = 14
# >>> false


s = Solution()
s.isPerfectSquare(num)
