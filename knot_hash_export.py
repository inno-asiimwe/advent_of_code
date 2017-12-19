

def hash(input):
  ascii_input = []
  for char in input:
    ascii_input.append(ord(char))

  expander = [17, 31, 73, 47, 23]
  ascii_input.extend(expander)

  rope = []
  for idx in range(0,256):
    rope.append(idx)

  current_position = 0
  skip_size = 0

  rope_length = len(rope)
  for round in range(0, 64):
    for length in ascii_input:
      section_length = int(length)

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

  block_start = 0
  dense_hash_list = []
  store = 0
  while block_start < 256:
    for x in range(0, 16): 
      store ^= rope[block_start + x]
    dense_hash_list.append(store)
    block_start += 16
    store = 0

  dense_hash = ''
  for part in dense_hash_list:
    # print hex(part)[2:].zfill(2)
    dense_hash += hex(part)[2:].zfill(2)

  # return dense_hash.zfill(32)
  return dense_hash


