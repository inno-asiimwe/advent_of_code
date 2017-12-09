file = open("input8.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0: len(file_contents)-1].split('\n')

registers = {}

def check_register(register):
  if registers.has_key(register):
    pass
  else:
    registers[register] = 0
  pass

memory_needed = None
test = file_input[0:10]
for item in file_input:
  parts = item.split()
  register = parts[0]
  action = parts[1]
  value = parts[2]
  # parts 3 is if
  comparing_register = parts[4]
  comparing_op = parts[5]
  comparing_value = parts[6]
  
  check_register(register)
  check_register(comparing_register)

  comparison = str(registers[comparing_register]) + comparing_op + comparing_value
  # print comparison
  should_run = eval(comparison)
  if should_run:
    if action == 'inc':
      registers[register] += int(value)
    elif action == 'dec':
      registers[register] -= int(value)

  if registers[register] > memory_needed:
    memory_needed = registers[register]




register_values = registers.values()
register_values.sort()
print "highest at end", register_values[len(register_values) - 1]
print "highest during process", memory_needed
'''
lessons learned
* string slice
* 
* python regex
* writing your assumptions in docs isn't that bad
'''