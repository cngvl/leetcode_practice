def is_anagram(s, t)
  # s is the input string
  s.split('').sort == t.split('').sort
  # t is the test anagram
  # t.split('').sort

  # return boolean value
end


s = "anagram"
t = "nagaram"

p is_anagram(s, t)
