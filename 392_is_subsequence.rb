# @param {String} s
# @param {String} t
# @return {Boolean}

# Input: s = "abc", t = "ahbgdc"
# Output: true

# Input: s = "axc", t = "ahbgdc"
# Output: false

# def is_subsequence(s, t)
#   test_sub = []
#   t.chars.each do |char|
#     test_sub << char if s.include?(char)
#   end
#   test_sub.join.include?(s)
#   test_sub.join == s
# end

# My first solution (didn’t pass all tests)
# def is_subsequence(s, t)
#   test_sub = []
#   t.chars.each do |char|
#     test_sub << char if s.include?(char)
#   end
#   test_sub.join.include?(s)
#   test_sub.join == s
# end

# Test fails when there are duplicates - i.e. s = 'ab' and t = 'baab'

# Solutions used a two-pointer method (new solution using references)
def is_subsequence(s, t)
  point1 = 0
  point2 = 0

  t.chars.each do
    point1 += 1 if s[point1] == t[point2]
    point2 += 1
  end
  point1 == s.length
end

# - reading while using two hands to point at comparison string and reading text analogy
