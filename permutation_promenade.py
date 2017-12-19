import time

file = open("input16.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0:len(file_contents)-1]

# file_input = 's1,x3/4,pe/b'

file_input = file_input.split(',')

programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n', 'o', 'p']
# programs = ['a', 'b', 'c', 'd', 'e']

def spin(num):
  nums = []
  for i in range(0, int(num)):
    nums.append(programs.pop())

  nums.reverse()

  for i in range(0, int(num)):
    programs.insert(0,nums.pop())

def swap_places(a, b):
  hold = programs[a]
  programs[a] = programs[b]
  programs[b] = hold

def swap_programs(a, b):
  swap_places(programs.index(a), programs.index(b))

times = {}
def dance(moves):
  for dance_move in moves:
    start_time = time.time()
    if dance_move[0] == 's':
      spin(dance_move[1:])
    elif dance_move[0] == 'x':
      swap_places(int(dance_move[1:dance_move.index('/')]), int(dance_move[dance_move.index('/') + 1:]))
    elif dance_move[0] == 'p':
      swap_programs(dance_move[1], dance_move[3])

    if times.has_key(dance_move[0]):
      times[dance_move[0]] += time.time() - start_time
    else:
      times[dance_move[0]] = time.time() - start_time


def get_answer():
  answer = ''
  for program in programs:
    answer += program
  return answer

dance(file_input)

print get_answer()
print times

dances = 1000000000
count = 1
# while count < dances:
#   if count % 100 == 0:
#     print count
#   dance(file_input)
#   count += 1
# print get_answer()

