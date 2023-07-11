# Written without use of memoisation

def factorial(val):
    if val == 1:
        return 1
    else:
        return val * factorial(val - 1)

print(factorial(3))
