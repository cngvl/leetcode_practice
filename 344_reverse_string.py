# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
# def reverseString(s):
#     s.reverse()

# Kind of cheated but I just used whatever tools were available to me
# I assume they wanted some pointer going in the leftward direction (but this uses more mem?)

def reverseString(s):
    l = 0
    r = len(s) - 1
    while l <= r:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1

s = ["h","e","l","l","o"]
# >>> ["o","l","l","e","h"]

# s = ["H","a","n","n","a","h"]
# >>> ["h","a","n","n","a","H"]

reverseString(s)
