# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples

def sum_mul(n, m):
    multipleSum = 0
    multiples = []

    lastMultiple = 0
    counter = 1

    if m <= 0 or n <= 0:
        return "INVALID"

    while lastMultiple < m:
        lastMultiple = counter * n
        if lastMultiple < m:
            multiples.append(lastMultiple)
            multipleSum += lastMultiple
        counter += 1



    return multipleSum

# sumMul(2, 9)   ==> 2 + 4 + 6 + 8 = 20
# sumMul(3, 13)  ==> 3 + 6 + 9 + 12 = 30
# sumMul(4, 123) ==> 4 + 8 + 12 + ... = 1860
# sumMul(4, -7)  ==> "INVALID"

sum_mul(2, 9)
