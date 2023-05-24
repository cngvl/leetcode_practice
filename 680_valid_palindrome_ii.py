def validPalindrome(s):
    # forward_pointer = 0
    # reverse_pointer = -1
    splitS = [*s]
    revSplitS = list(reversed(splitS))

    if splitS == splitS[::-1]:
        return True


    for letter in range(len(splitS)):

        splitS_copy = splitS.copy()
        del splitS_copy[letter]

        splitS_copy_reversed = list(reversed(splitS_copy))
        if splitS_copy_reversed == splitS_copy:
            return True

    return False

# s = "aba"
# >>> true

# s = "abca"
# >>> true

# s = "abc"
# >>> false

# s = "aaaaab"
# >>> true

# s = "bebeb"
# true

s = "cbbcc"
# true

print(validPalindrome(s))

    # for letter in splitS:
    #     # print(letter)
    #     # remainingString =
    #     # splitS.remove(letter)
    #     remainingString = s.replace(letter, '', 1)
    #     revRemainingString = remainingString[::-1]
    #     if remainingString == revRemainingString:
    #         return True
    #     # print(revRemainingString)

# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:
#             if s[l] != s[r]:
#                 skipL, skipR = s[l + 1: r + 1], s[l:r]
#                 return (skipL == skipL[::-1] or skipR == skipR[::-1])
#             l, r = l + 1, r - 1
#         return True

# Josiah's solution:
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def is_pali_range(i, j):
#             return all(s[i + k] == s[j - k] for k in range(i, j))

#         for i in range(len(s) // 2):
#             if s[i] != s[~i]:
#                 j = len(s) - 1 - i
#                 return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
#         return True
