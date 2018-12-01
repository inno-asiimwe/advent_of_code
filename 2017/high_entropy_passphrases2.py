
file = open("input.txt")
valid = 0

def are_anagrams(a, b):
  if len(a) != len(b):
    return False
  for c in a:
    if a.count(c) != b.count(c):
      return False

  return True

for row in file:
  valid_passphrase = True
  words = row.split()
  for p in range(0, len(words)):
    for q in range(p + 1, len(words)):
      if are_anagrams(words[p], words[q]):
        valid_passphrase = False
    if valid_passphrase is False:
      break
  if valid_passphrase is True:
    valid += 1

print valid