# Constraints:
# 1 <= columnNumber <= 231 - 1

# Looks like much simpler version of q263 ugly number
# Not sure if I need to map out each val to letter?
# Can just loop and minus 26 until cant anymore
    # Will need to do some form of division
    # Will I need to do some forms of POWER? / Logging?¿¿¿¿/??
    # For each subtraction? of 26, need to iterate over the prev vals
# Don't need to deal with -ve columnNumber

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letterHash = {
            1 : "A",
            2 : "B",
            3 : "C",
            4 : "D",
            5 : "E",
            6 : "F",
            7 : "G",
            8 : "H",
            9 : "I",
            10 : "J",
            11 : "K",
            12 : "L",
            13 : "M",
            14 : "N",
            15 : "O",
            16 : "P",
            17 : "Q",
            18 : "R",
            19 : "S",
            20 : "T",
            21 : "U",
            22 : "V",
            23 : "W",
            24 : "X",
            25 : "Y",
            26 : "Z",
        }
        divisionCount = 0
        minusCount = 0
        returnString = ''

        lastLetter = columnNumber % 26
        while columnNumber // 26 > 0:
            # check =  columnNumber % 26
            # letterCheck = letterHash[check]
            # columnNumber = columnNumber // 26
            divisionCheck = columnNumber // 26
            remainderCheck = columnNumber % 26
            columnNumber = columnNumber - 26
            minusCount += 1

        # while divisionCount // 26 > 0:
        #     divisionCount = divisionCount // 26


        prefix = letterHash[minusCount]
        suffix = letterHash[lastLetter]
        returnString = prefix + suffix
        print(returnString)

        return returnString

    def convertToTitle2(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
                offset = (columnNumber - 1 ) % 26
                res += chr(ord('A') + offset)
                columnNumber = ( columnNumber - 1 ) // 26

        return res[::-1]

# columnNumber = 1
# >>> "A"

# columnNumber = 28
# >>> "AB"

# columnNumber = 53
# >>> "BA"

# columnNumber = 701
# >>> "ZY"

columnNumber = 12345
# >>> "RFU"

sol = Solution()
sol.convertToTitle(columnNumber)
