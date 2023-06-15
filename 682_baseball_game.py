# integer x = base score
# '+' = a new score that is the sum of the previous two
# 'd' = a new score that is double the previous score
# 'c' = invalidate the previous score, removing it from the record



class Solution:
    def calPoints(self, operations: list[str]) -> int:
        # print(operations)
        record = []
        for item in operations:
            # print(item)
            if item == '+':
                record.append(record[-1] + record[-2])
            elif item == 'D':
                record.append(record[-1] * 2)
            elif item == 'C':
                del record[-1]
            else:
                record.append(int(item))
        return sum(record)






# ops = ["5","2","C","D","+"]
# >>> 30

ops = ["5","-2","4","C","D","9","+","+"]
# >>> 27

# ops = ["1","C"]
# >>> 0



s = Solution()
print(s.calPoints(ops))
