file = open("input19.txt")
file_contents = file.read()
file.close()
the_grid = file_contents[0: len(file_contents)-1].split('\n')

def find_entrance(grid):
  found = False

  sides = ['left', 'bottom', 'right', 'top']
  current_side_idx = 0

  current_row = 0
  current_col = 0
  while current_side_idx < 5:
    current_cell = grid[current_row][current_col]
    current_side =  sides[current_side_idx]

    if current_cell == '|' and (current_side == 'top' or current_side == 'bottom'):
      return (current_row, current_col)
    elif current_side == '-' and (current_side == 'left' or current_side == 'right'):
      return (current_row, current_col)

    if current_side == 'left':
      current_row += 1
    elif current_side == 'bottom':
      current_col += 1
    elif current_side == 'right':
      current_row -= 1
    elif current_side == 'top':
      current_col -= 1

    # bottom of map
    if current_side == 'left' and current_row == len(grid) - 1:
      current_side_idx += 1
      current_col += 1
    elif current_side == 'bottom' and current_col == len(grid) - 1:
      current_side_idx += 1
      current_row -= 1
    elif current_side == 'right' and current_row == 0:
      current_side_idx += 1
      current_col -= 1

entrance = find_entrance(the_grid)

grid_height = len(the_grid)
grid_width = len(the_grid[0])
current_dir = ''
current_row = entrance[0]
current_col = entrance[1]
current_cell = the_grid[current_row][current_col]

if current_row == 0:
  current_dir = 'down'
elif entrance[1] == 0:
  current_dir = 'right'
elif current_row == grid_height - 1:
  current_dir = 'up'
else:
  current_dir = 'left'

letters_encountered = ''
steps = 0
while current_dir and current_cell != ' ':
  print current_cell, current_dir, current_row, current_col, steps

  if current_cell.isalpha():
    letters_encountered += current_cell
  elif current_cell == '+':
    # find next non empty cell
    possible_dirs = ['down', 'right', 'up', 'left']
    if current_dir == 'down' or current_dir == 'up' or current_row >= grid_height - 1 or the_grid[current_row + 1][current_col] == ' ':
      possible_dirs.remove('down')
    if current_dir == 'right' or current_dir == 'left' or current_col >= grid_width - 1 or the_grid[current_row][current_col + 1] == ' ':
      possible_dirs.remove('right')
    if current_dir == 'up' or current_dir == 'down' or current_row <= 0 or the_grid[current_row - 1][current_col] == ' ':
      possible_dirs.remove('up')
    if current_dir == 'left' or current_dir == 'right' or current_col <= 0 or the_grid[current_row][current_col - 1] == ' ':
      possible_dirs.remove('left')

    current_dir = possible_dirs[0]

  if current_dir == 'down':
    current_row += 1
  elif current_dir == 'right':
    current_col += 1
  elif current_dir == 'up':
    current_row -= 1
  elif current_dir == 'left':
    current_col -= 1

  current_cell = the_grid[current_row][current_col]
  steps += 1

print letters_encountered
print steps