file = open("input10.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0: len(file_contents)-1].split(',')

rope = []
for idx in range(0,256):
	rope.append(idx)

current_position = 0
skip_size = 0

# def getReverseZone(cp, length):
# 	if cp + length < 255:

# file_input = [3,4,1,5]
# rope = [0, 1, 2, 3, 4]
rope_length = len(rope)
for length in file_input:
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
	if current_position > rope_length:
		current_position = current_position - rope_length

	skip_size +=1


print rope[0] * rope[1]
