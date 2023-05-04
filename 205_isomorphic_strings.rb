require 'pry-byebug'

# @param {String} s
# @param {String} t
# @return {Boolean}
def is_isomorphic(s, t)
  # Iterate over s + t with a counter?
  # s[n] / t[n]
  # s[n + 1] / t[n + 1]
  # maybe make some sort of hash
  # hash = {}
  # hash[s[n]] = t[n]

  # (hash.has_value?(t[counter]))
  return false if s.length != t.length

  hash = {}
  s.length.times do |counter|
    # Check if hash[s[counter]] has been seen before

    # If new, add it to the hash
    if hash.has_value?(t[counter]) || hash.key?(s[counter])
      # binding.pry
      return false if t[counter] != hash[s[counter]]

    elsif (!hash.key?(s[counter]))
      hash[s[counter]] = t[counter]

    end
  end

  return true
end

# s = "egg"
# t = "add"
# >>> true

# s = "foo"
# t = "bar"
# >>> false

s = "badc"
t = "baba"
# >>> false

p is_isomorphic(s, t)
