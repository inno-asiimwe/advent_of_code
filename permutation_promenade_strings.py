import time

file = open("input16.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0:len(file_contents)-1]

# file_input = 's1,x3/4,pe/b'

file_input = file_input.split(',')

programs = 'abcdefghijklmnop'
# programs = 'abcde'

def spin(order, num):
  return order[-num:] + order[0:len(order)-num]

def swap_places(order, a, b):
  if a < b:
    return order[0:a] + order[b] + order[a+1:b] + order[a] + order[b+1:]
  else:
    return order[0:b] + order[a] + order[b+1:a] + order[b] + order[a+1:]

def swap_programs(order, a, b):
  return swap_places(order, order.index(a), order.index(b))

times = {}
def dance(layout, moves):
  order = layout
  for dance_move in moves:
    start_time = time.time()
    if dance_move[0] == 's':
      new_order = spin(order, int(dance_move[1:]))
    elif dance_move[0] == 'x':
      new_order = swap_places(order, int(dance_move[1:dance_move.index('/')]), int(dance_move[dance_move.index('/') + 1:]))
    elif dance_move[0] == 'p':
      new_order = swap_programs(order, dance_move[1], dance_move[3])

    order = new_order
    # if times.has_key(dance_move[0]):
    #   times[dance_move[0]] += time.time() - start_time
    # else:
    #   times[dance_move[0]] = time.time() - start_time
  return order

programs = dance(programs, file_input)
print programs

dances = 1000000000
count = 1
seen = {programs: 1}
while count < dances:
  if seen.has_key(programs):
    print 'seen it!', programs, seen[programs]
  else:
    seen[programs] = count
  programs = dance(programs, file_input)
  count += 1

print programs