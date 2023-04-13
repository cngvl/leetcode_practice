# @param {String} ransom_note
# @param {String} magazine
# @return {Boolean}
def can_construct(ransom_note, magazine)
  # both are strings
  # create a magazine stack
  # for each char for ransom note, pop a letter from magazine stack
  ransom_note_chars = ransom_note.chars
  magazine.each_char do |magazine_char|
    # p magazine_char
    # p ransom_note_chars.index(magazine_char)
    # ransom_note_chars.delete_at(ransom_note_chars.index(magazine_char))
    (x = ransom_note_chars.index(magazine_char)) && ransom_note_chars.delete_at(x)
  end
  ransom_note_chars.empty?
end

ransom_note = 'aa'
magazine = 'ab'

p can_construct(ransom_note, magazine)
