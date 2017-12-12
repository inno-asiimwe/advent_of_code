file = open("input10.txt")
file_contents = file.read()
file.close()
# part 1
# file_input = file_contents[0: len(file_contents)-1].split(',')
# part 2
file_input = file_contents[0: len(file_contents)-1]

ascii_input = []
for char in file_input:
  ascii_input.append(ord(char))

# print len(ascii_input)
expander = [17, 31, 73, 47, 23]
ascii_input.extend(expander)
print ascii_input

rope = []
for idx in range(0,256):
  rope.append(idx)

current_position = 0
skip_size = 0

# def getReverseZone(cp, length):
#   if cp + length < 255:

# file_input = [3,4,1,5]
# rope = [0, 1, 2, 3, 4]
rope_length = len(rope)
for round in range(0, 64):
  for length in ascii_input:
    section_length = int(length)
    # print 'current_position', current_position
    # print 'skip_size', skip_size
    # print 'section_length', section_length

    if current_position + section_length < rope_length:
      reverse_zone = rope[current_position : current_position+section_length]
      reverse_zone.reverse()

      for idx in range(current_position, current_position+section_length):
        rope[idx] = reverse_zone[idx-current_position]
    else:
      # grab current position until the end
      beginning = rope[current_position : rope_length]
      beginning_len = len(beginning)
      # grab beggining until the remander of current position + length of seciton - rope length
      end = rope[0:current_position + section_length - rope_length]
      end_len = len(end)

      beginning.extend(end)
      beginning.reverse()

      beginning_idx = 0
      for idx in range(0, beginning_len):
          rope[current_position + idx] = beginning[idx]

      for idx in range(0, end_len):
        rope[idx] = beginning[beginning_len + idx]

    # print 'rope', rope

    current_position += section_length + skip_size
    while current_position >= rope_length:
      current_position = current_position - rope_length

    skip_size +=1
    # if skip_size == rope_length:
    #   skip_size = 1

  # print 'end of round', round
  # print skip_size, current_position

# part 1 
# print rope[0] * rope[1]

# test = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
# print rope
# for i in range(0, 16):
#   rope[i] = test[i]

# print
# print rope

block_start = 0
dense_hash_list = []
store = 0
while block_start < 256:
  for x in range(0, 16): 
    store ^= rope[block_start + x]
  dense_hash_list.append(store)
  block_start += 16
  store = 0

print dense_hash_list

dense_hash = ''
for part in dense_hash_list:
  dense_hash += hex(part)[2:]

print dense_hash

'''
Lessones learned (maybe again)
slice to end [x:]
hex()
ord()
reset sum!
'''