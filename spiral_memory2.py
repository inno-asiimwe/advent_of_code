import sys

target = int(sys.argv[1])
size = int(sys.argv[2])

grid = []

for row in range(0, size):
  grid.append([])
  for col in range(0, size):
    grid[row].append(0)

# for row in grid:
#   print row


center = [(size-1) / 2, (size-1) / 2]
print center

def addAllSides(loc):
  top = 0
  bottom = 0
  left = 0
  right = 0
  top_left = 0
  top_right = 0
  botom_left = 0
  bottom_right = 0
  if loc[0] > 0:
    top = grid[loc[0]-1][loc[1]]
  if loc[0] < size-1:
    bottom = grid[loc[0]+1][loc[1]]
  if loc[1] > 0:
    left = grid[loc[0]][loc[1]-1]
  if loc[1] < size-1:
    right = grid[loc[0]][loc[1]+1]
  if loc[0] > 0 and loc[1] > 0:
    top_left = grid[loc[0]-1][loc[1]-1]
  if loc[0] > 0 and loc[1] < size-1:
    top_right = grid[loc[0]-1][loc[1]+1]
  if loc[0] < size-1 and loc[1] > 0:
    botom_left = grid[loc[0]+1][loc[1]-1]
  if loc[0] < size-1 and loc[1] < size-1:
    bottom_right = grid[loc[0]+1][loc[1]+1]

  return top + bottom + left + right + top_left + top_right + botom_left + bottom_right

def up(loc):
  if loc[0] > 0:
    return grid[loc[0]-1][loc[1]]
  else:
    return None

def down(loc):
  if loc[0] < size-1:
    return grid[loc[0]+1][loc[1]]
  else:
    return None

def right(loc):
  if loc[1] < size-1:
    return grid[loc[0]][loc[1]+1]
  else:
    return None

def left(loc):
  if loc[1] > 0:
    return grid[loc[0]][loc[1]-1]
  else:
    return None

def move(loc):
  if up(loc) is 0 and right(loc) is 0 and left(loc) is 0 and down(loc) is 0:
    # print "in the center"
    loc[1] += 1
  elif up(loc) is 0 and left(loc) is not 0:
    # print "go up"
    loc[0] -= 1
  elif down(loc) is not 0 and left(loc) is 0:
    # print "go left"
    loc[1] -= 1
  elif down(loc) is 0 and right(loc) is not 0:
    # print "go down"
    loc[0] += 1
  elif right(loc) is 0 and up(loc) is not 0:
    # print "go right"
    loc[1] += 1


grid[center[0]][center[1]] = 1
cell = center

count = 0

while grid[cell[0]][cell[1]] < target:
# while count < 300:
  move(cell)
  grid[cell[0]][cell[1]] = addAllSides(cell)
  # move(cell)
  # grid[cell[0]][cell[1]] = addAllSides(cell)
  # move(cell)
  # grid[cell[0]][cell[1]] = addAllSides(cell)
  # move(cell)
  # grid[cell[0]][cell[1]] = addAllSides(cell)
  # break
  count += 1


for row in grid:
  print row

print grid[cell[0]][cell[1]]