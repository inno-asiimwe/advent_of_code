file = open("input22.txt")
file_contents = file.read()
file.close()
raw_map = file_contents[0:len(file_contents)-1].split('\n')

state = {}
start_infection = 0
top = len(raw_map) / 2
for row in range(0, len(raw_map)):
  for col in range(0, len(raw_map)):
    # print row, col
    # print top - row, col - top
    if raw_map[row][col] == '#':
      state[(top - row, col - top)] = 1
      start_infection += 1
    else:
      state[(top - row, col - top)] = 0

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

  if dir == 'RIGHT':
    return right[current]
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
steps = 10000
while steps > 0:
  steps -= 1
  # print 'current_node', current_node

  if state.has_key(current_node) == False:
    # print 'addding node', current_node
    state[current_node] = 0

  if state[current_node]:
    # print 'infected!'
    state[current_node] = 0
    current_dir = turn(current_dir, 'RIGHT')
    # print 'new dir', current_dir
  else:
    # print 'infecting node!'
    infection_count += 1
    state[current_node] = 1
    current_dir = turn(current_dir, 'LEFT')
    # print 'new dir', current_dir
  
  # move forward
  current_node = move_forward(current_node, current_dir)

print 'new infected', infection_count
print 'final sate', current_dir
