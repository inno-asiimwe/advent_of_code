import knot_hash_export as knot

base = 'hfdlxzhv'
# base = 'flqrgnkx'

size = 128
scale = 16 ## equals to hexadecimal
num_of_bits = 4

# print bin(int(hash1[0], scale))[2:].zfill(num_of_bits)
# print bin(int(hash1[1], scale))[2:].zfill(num_of_bits)

zone = []
for i in range(0, size):
  row = []
  layer = base + '-' + str(i)
  layer_hash = knot.hash(layer)
  if i == 2 or i == 3:
    print layer_hash

  for char in layer_hash:
    bits = bin(int(char, scale))[2:].zfill(num_of_bits)
    for bit in bits:
      if bit == '0':
        row.append('0')
      else:
        row.append(int(bit))

  zone.append(row)

# print zone[2]
# print zone[3]

num_ones = 0
for zone_row in zone:
  # print zone[i]
  for col in zone_row:
    if col == 1:
      num_ones += 1

print num_ones

for row in zone[0:8]:
  print row[0:8]

region_count = 0
def determine_region(y, x):
  zone[y][x] = str(region_count)
  if x > 0:
    if zone[y][x - 1] == 1:
        determine_region(y, x - 1)

  if y > 0 and x < len(zone[y-1]):
    if zone[y - 1][x] == 1:
        determine_region(y - 1, x)

  if x < len(zone[y]) - 1:
    if zone[y][x + 1] == 1:
        determine_region(y, x + 1)

  if y < len(zone) - 1 and x < len(zone[y+1]):
    if zone[y + 1][x] == 1:
        determine_region(y + 1, x)

## count regions
for y in range(0, len(zone)):
# for y in range(0, 8):
  for x in range(0, len(zone[y])):
  # for x in range(0, 8):
    if zone[y][x] == 1:
      region_count += 1
      determine_region(y, x)

print region_count

for row in zone[0:8]:
  print row[0:8]

