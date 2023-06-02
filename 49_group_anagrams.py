from typing import Collection

def groupAnagrams(strs):
    # res = {} # maping charCount to list of Anagrams
    res = Collection.defaultdict(list)
    # ans = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            count[ord(c) - ord("a")] += 1 # ord() returns an integer representing the unicode character

            # ord("a") = 97
            # so ord("a") - ord("a") = 0
            # so "a" is in the 0th index
        res[tuple(count)].append(s)
        # Changed to tuple because python is weird
