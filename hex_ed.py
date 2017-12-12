file = open("input11.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0: len(file_contents)-1].split(',')

# distances
y = 0
x = 0
max_distance = 0

def getDistanceAway(x, y):
  x = abs(x)
  y = abs(y)
  if x == y:
    return x * 2

  count = abs(y - x)
  if x < y:
    count += x * 2
  else:
    count += y * 2
  return count

# file_input = ['ne','ne','ne'] # 3
# file_input = ['ne','ne', 'ne', 'ne', 'sw', 'sw'] # 0
# file_input = ['ne','ne','s','s'] # 2 (se, se)
# file_input = ['se','sw','se','sw', 'sw'] # 3 (s, s, w)
for step in file_input:
  if step == 'n':
    y += 1
  if step == 'ne':
    x += 0.5
    y += 0.5
  if step == 'se':
    x += 0.5
    y -= 0.5
  if step == 's':
    y -= 1
  if step == 'sw':
    x -= 0.5
    y -= 0.5
  if step == 'nw':
    y += 0.5
    x -= 0.5

  if getDistanceAway(x, y) > max_distance:
    max_distance = getDistanceAway(x, y)

print 'y', y
print 'x', x

print getDistanceAway(x, y)
print max_distance

