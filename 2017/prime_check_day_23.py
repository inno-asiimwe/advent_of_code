step = 17
start = 109900
count = 0

for x in range(0, 1001):
  num = start + (x * step)
  prime = True

  for y in range(2,num):
    if num % y == 0:
      prime = False
      count += 1
      break

print count
print num