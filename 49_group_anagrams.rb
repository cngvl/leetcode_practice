# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
  strs.each do |str|
    p str
  end
end


strs = ["eat","tea","tan","ate","nat","bat"]
# >>> [["bat"],["nat","tan"],["ate","eat","tea"]]

# strs = [""]
# >>> [[""]]

# strs = ["a"]
# >>> [["a"]]

group_anagrams(strs)
