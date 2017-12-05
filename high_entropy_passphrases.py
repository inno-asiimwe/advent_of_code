
file = open("input.txt")
valid = 0

for row in file:
  valid_passphrase = True
  words = row.split()
  for p in range(0, len(words)):
    for q in range(p + 1, len(words)):
      if words[p] == words[q]:
        valid_passphrase = False
    if valid_passphrase is False:
      break
  if valid_passphrase is True:
    valid += 1

print valid