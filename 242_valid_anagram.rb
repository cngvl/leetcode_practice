def is_anagram(s, t)
  # s is the input string
  s.split('').sort == t.split('').sort
  # t is the test anagram
  # t.split('').sort

  # return boolean value
end

# can also use a hashmap to count for each occurance of a given letter
# the sort feature may not be used in all langs
# hash = { letter , freq }
# s_hash = { a = 3, n = 1 ...}
# t_hash = { a = 3, n = 1 ...}
# see if s_hash == t_hash

s = 'anagram'
t = 'nagaram'

p is_anagram(s, t)
