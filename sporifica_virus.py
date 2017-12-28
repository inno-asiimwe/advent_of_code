file = open("input22.txt")
file_contents = file.read()
file.close()
raw_map = file_contents[0:len(file_contents)-1].split('\n')

state = {}
start_infection = 0
top = len(raw_map) / 2
for row in range(0, len(raw_map)):
  for col in range(0, len(raw_map)):
    if raw_map[row][col] == '#':
      state[(top - row, col - top)] = '#'
      start_infection += 1
    else:
      state[(top - row, col - top)] = '.'

# print state

def turn(current, dir):
  right = {
    'UP': 'RIGHT',
    'RIGHT': 'DOWN',
    'DOWN': 'LEFT',
    'LEFT': 'UP'
  }
  left = {
    'UP': 'LEFT',
    'LEFT': 'DOWN',
    'DOWN': 'RIGHT',
    'RIGHT': 'UP',
  }
  reverse = {
    'UP': 'DOWN',
    'LEFT': 'RIGHT',
    'DOWN': 'UP',
    'RIGHT': 'LEFT',
  }

  if dir == 'RIGHT':
    return right[current]
  elif dir == 'REVERSE':
    return reverse[current]
  else:
    return left[current]


def move_forward(current, dir):
  if dir == 'UP':
    return (current[0] + 1, current[1])
  elif dir == 'RIGHT':
    return (current[0], current[1] + 1)
  elif dir == 'DOWN':
    return (current[0] - 1, current[1])
  else: # 'LEFT'
    return (current[0], current[1] - 1)


current_node = (0, 0)
current_dir = 'UP'

infection_count = 0
steps = 10000000
while steps > 0:
  steps -= 1
  # print 'current_node', current_node

  if state.has_key(current_node) == False:
    # print 'addding node', current_node
    state[current_node] = 0

  if state[current_node] == '#':
    # flag node
    # print 'flagging', current_node
    state[current_node] = 'F'
    current_dir = turn(current_dir, 'RIGHT')
    # print 'new dir', current_dir
  elif state[current_node] == 'W':
    # infect node
    # print 'infecting', current_node
    infection_count += 1
    state[current_node] = '#'
    # current_dir = turn(current_dir, 'RIGHT')
    # print 'new dir', current_dir
  elif state[current_node] == 'F':
    # clean node
    # print 'cleanning', current_node
    state[current_node] = '.'
    current_dir = turn(current_dir, 'REVERSE')
  else:
    # weaken node
    # print 'weakening', current_node
    state[current_node] = 'W'
    current_dir = turn(current_dir, 'LEFT')
    # don't move
  
  # move forward
  current_node = move_forward(current_node, current_dir)

print 'new infected', infection_count
print 'final sate', current_dir
