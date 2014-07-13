#!/usr/bin/python

import sys

def count_letters(word):
  count = {}
  for letter in word:
    if letter not in count: count[letter] = 0
    count[letter] += 1
  return count

def spellable(word, rack):
    word_count = count_letters(word)
    rack_count  = count_letters(rack)
    return all( [word_count[letter] <= rack_count[letter] for letter in word] ) 

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def word_score(word):
  return sum([score[i] for i in word])

def reader(filename):
  return (word.strip() for word in open(filename))

if __name__ == "__main__":
  if len(sys.argv) == 2:
    # I want to make sure that only seven letters are used.
    # If not I want an Usage case to show up. I could put
    # with len(sys.argv) == 2 but I want a different Usage
    # case so anyone who uses it will know why it  is breaking
    if len(sys.argv[1]) == 15:
      # have to strip newline from input
      rack = sys.argv[1].strip()
    else:
      print "Usage: scribble_cheat.py <your race>"
      print "<your rack> should have 7 letters"
      exit()
  else:
    print "Usage: scribble_cheat.py <your rack>"
    exit()

  words = reader('/etc/dictionaries-common/words')
  scored =  ((word_score(word), word) for word in words if set(word).issubset(set(rack)) and len(word) > 1 and spellable(word, rack))

  for score, word in sorted(scored):
    print str(score), ':', word

