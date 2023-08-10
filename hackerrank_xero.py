# Question 6

def decode(encoded):
    flippedString = encoded[::-1]
    storedNumber = ''
    returnedString = ''

    for singleChar in flippedString:
        # print(flippedString[singleNumber])

        storedNumber += singleChar

        if int(storedNumber) >= 65 and int(storedNumber) <= 90:
            returnedString += chr(int(storedNumber))
            storedNumber = '0'

        if int(storedNumber) >= 97 and int(storedNumber) <= 122:
            returnedString += chr(int(storedNumber))
            storedNumber = '0'

        if int(storedNumber) == 32:
            returnedString += chr(int(storedNumber))
            storedNumber = '0'

    return returnedString

encoded = "23511011501782351112179911801562340161171141148"
# >>> Truth Always Wins

decode(encoded)
