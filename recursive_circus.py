import re
file = open("input7.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0: len(file_contents)-1].split('\n')


class Program:
  'space for docs! cool'

  def __init__(self, name, weight, children):
    self.name = name
    self.weight = weight
    self.children = children

  def getTowerWeight(self):
    if len(self.children) > 0:
      total_weight = self.weight
      for child in self.children:
        total_weight += programs[child].getTowerWeight()
      return total_weight
    else:
      return self.weight

  def is_balanced(self):
    if len(self.children) == 0:
      print 'no children'
      return True
    else:
      random_child_weight = programs[self.children[0]].getTowerWeight()
      for child in self.children:
        if programs[child].getTowerWeight() != random_child_weight:
          return False
      return True

  def find_imbalance(self):
    

programs = {}
children = {}

test = file_input[0:10]
for item in file_input:
  # slice to first space
  name = item[0:item.find(' ')]
  # print "name", name
  # one or more numbers
  weight = int(re.search( r'[0-9]+', item).group())
  # print weight

  sub_towers = []
  on_disk = re.search( r'->\s(.*)', item)
  if on_disk: 
    sub_tower_list = on_disk.group()[3:] # skip -> 
    sub_towers_raw = sub_tower_list.split(',')
    for sub_tower in sub_towers_raw:
      sub_towers.append(sub_tower.strip())
      children[sub_tower.strip()] = 1
    # print sub_towers

  programs[name] = Program(name, weight, sub_towers)

root = []
for program in programs:
  if children.has_key(program):
    pass
  else:
    root = programs[program]

print "root is", root.name
print "weight", root.getTowerWeight()

for sub_tower in root.children:
  if 
  print programs[sub_tower].is_balanced()
  print programs[sub_tower].getTowerWeight()

