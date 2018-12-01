
num_steps = 355
buff = [0]
current_position = 0

steps = 0
while steps < 2017:
  steps += 1
  insert_location = (num_steps - (len(buff) - 1 - current_position)) % len(buff)
  buff.insert(insert_location + 1, steps)
  current_position = insert_location
  # print buff, current_position
  # print insert_location + 1

print buff[buff.index(2017) + 1]



buff_len = 1
current_position = 0
value_at_1 = 0
steps = 0
while steps < 50000000:
  steps += 1
  insert_location = (num_steps - (buff_len - 1 - current_position)) % buff_len
  if insert_location == 0:
    value_at_1 = steps
  buff_len += 1
  current_position = insert_location

print value_at_1