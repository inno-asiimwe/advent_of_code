file = open("input12.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0:len(file_contents)-1].split('\n')

map = {}
for line in file_input:
  id = line[0:line.find(' ')]
  neighbors = line[line.find('<->')+4:].split(', ')

  # print neighbors
  if map.has_key(id):
    for neighbor in neighbors:
      if neighbor in map[id] == False:
        map[id].extend(neighbor)
        if map.has_key(neighbor):
          map[neighbor].extend(id)
        else:
          map[neighbor] = [id]
  else:
    map[id] = neighbors


def find_neighbors(id, phone_book):
  for neighbor in map[id]:
    if id_0_neighbors.has_key(neighbor) is False:
      id_0_neighbors[neighbor] = 1
      find_neighbors(neighbor, phone_book)

id_0_neighbors = {}
find_neighbors('0', id_0_neighbors)

print len(id_0_neighbors.keys())


groups = {1: id_0_neighbors}

for id in map:
  is_in_group = False
  for group in groups:
    if id in groups[group]:
      is_in_group = True

  if is_in_group is False:
    num_groups = len(groups.keys())
    groups[num_groups + 1] = {id: 1}
    find_neighbors(id, groups[num_groups + 1])

print len(groups.keys())