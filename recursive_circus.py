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
      first_child = programs[self.children[0]].getTowerWeight()
      for child in self.children[1:len(self.children)]:
        if programs[child].getTowerWeight() != first_child:
          return False
      return True

  def find_imbalance(self):
    # print
    # print 'searching', self.name
    # for child in self.children:
    #   print child, programs[child].getTowerWeight(), programs[child].is_balanced()

    child_count = len(self.children)

    if child_count == 0:
      print 'no children'
      return None
    elif child_count == 1:
      return programs[self.children[0]].find_imbalance()
    elif child_count > 0:
        for child in self.children:
          if programs[child].is_balanced() == False:
            return programs[child].find_imbalance()
        
        # if above fails check if all children are equal
        # first check if first child is equal to second child
        # we must use three children because with only two the imbalance cannot be determined
        first_child = programs[self.children[0]]
        second_child = programs[self.children[1]]
        third_child = programs[self.children[2]]

        if first_child.getTowerWeight() == second_child.getTowerWeight():
          # first child is a reliable comparison
          for child in self.children[2:child_count]:
            if programs[child].getTowerWeight() != first_child.getTowerWeight():
              weight_diff = first_child.getTowerWeight() - programs[child].getTowerWeight()
              return programs[child].weight + weight_diff
        else:
          if first_child.getTowerWeight() == third_child.getTowerWeight():
            # second child is off
            weight_diff = first_child.getTowerWeight() - second_child.getTowerWeight()
            return second_child.weight + weight_diff
          elif second_child.getTowerWeight() == third_child.getTowerWeight():
            # first child is off
            weight_diff = first_child.getTowerWeight() - second_child.getTowerWeight()
            return first_child.weight + weight_diff

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

# for sub_tower in root.children:
#   print programs[sub_tower].name
#   print programs[sub_tower].is_balanced()
#   print programs[sub_tower].getTowerWeight()

imblance = root.find_imbalance()
print imblance

# for child in imblance.children:
#   print programs[child].getTowerWeight()

# get tower weight test
# print 'pgvds', programs['pgvds'].weight, programs['pgvds'].getTowerWeight()
'''
lessons learned (again)
* read the instructions
* this is how to make a comment block in python
* python regex
* writing your assumptions in docs isn't that bad
'''