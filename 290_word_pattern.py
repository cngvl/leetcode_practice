def wordPattern(pattern, s):
    patternHash = {}
    patternSplit = [*pattern]
    stringSplit = s.split()

    if len(stringSplit) != len(patternSplit): return False

    for letter, word in zip(patternSplit, stringSplit):
        if letter not in patternHash and word not in patternHash.values():
            patternHash[letter] = word
        else:
            if patternHash.get(letter) != word: return False

    return True


# pattern = "abba"
# s = "dog cat cat dog"
# >>> true

# pattern = "abbaa"
# s = "dog cat cat dog"
# >>> false

# pattern = "abba"
# s = "dog cat cat fish"
# >>> false

pattern = "aaaa"
s = "dog cat cat dog"
# >>> false

# pattern = "abba"
# s = "dog dog dog dog"
# >>> false

# pattern = "abcd"
# s = "dog dog dog dog"
# >>> false


print(wordPattern(pattern, s))
