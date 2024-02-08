# Constraints:
    # 1 <= s.length <= 3 * 105
    # s consist of printable ASCII characters.

# Some form of a two pointer technique at the start and end of the string
# Need to keep iterating inwards until both pointers are at a vowel

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        leftPointer, rightPointer = 0, len(s) - 1
        tempLetter = ''
        listS = [char for char in s]

        while leftPointer < rightPointer:
            if listS[leftPointer] not in vowels:
                leftPointer += 1

            if listS[rightPointer] not in vowels:
                rightPointer -= 1

            leftPointerCheck = listS[leftPointer]
            rightPointerCheck = listS[rightPointer]
            ifCheck = (listS[leftPointer] in vowels and listS[rightPointer] in vowels)

            if listS[leftPointer] in vowels and listS[rightPointer] in vowels:
                tempLetter = listS[leftPointer]
                listS[leftPointer] = listS[rightPointer]
                listS[rightPointer] = tempLetter
                leftPointer += 1
                rightPointer -= 1

        listS = ''.join(listS)
        print(listS)

# s = "hello"
# >>> "holle"

s = "leetcode"
# >>> "leotcede"

sol = Solution()
sol.reverseVowels(s)
