# Day 15

a_previous_value = 591
# a_previous_value = 65
b_previous_value = 393
# b_previous_value = 8921

a_factor = 16807
b_factor = 48271
common_divisor = 2147483647

# match_count = 0
# for i in range(0, 40000000):
#   a_result = (a_previous_value * a_factor) % common_divisor
#   b_result = (b_previous_value * b_factor) % common_divisor
  
#   if bin(a_result)[2:].zfill(32)[-16:] == bin(b_result)[2:].zfill(32)[-16:]:
#     match_count += 1

#   a_previous_value = a_result
#   b_previous_value = b_result
# print match_count

a_results = []
a_length = 0
b_results = []
b_length = 0
while a_length < 5000000 or b_length < 5000000:
  a_result = (a_previous_value * a_factor) % common_divisor
  b_result = (b_previous_value * b_factor) % common_divisor

  if a_result % 4 == 0:
    a_results.append(bin(a_result)[2:].zfill(32)[-16:])
    a_length += 1

  if b_result % 8 == 0:
    b_results.append(bin(b_result)[2:].zfill(32)[-16:])
    b_length += 1

  a_previous_value = a_result
  b_previous_value = b_result

new_match_count = 0
for i in range(0, 5000000):
  if a_results[i] == b_results[i]:
    new_match_count += 1

print new_match_count

