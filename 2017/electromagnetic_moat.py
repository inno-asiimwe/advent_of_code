# day 24
from collections import deque

file = open("input24.txt")
file_contents = file.read()
file.close()
available_ports = file_contents[0:len(file_contents)-1].split('\n')

class Node(object):
  """docstring for Node"""
  def __init__(self, ports, side_used, remaining_ports):
    super(Node, self).__init__()
    # print 'making node for', ports
    self.ports = ports
    self.side_used = side_used
    self.remaining_ports = remaining_ports
    self.head = self.ports.split('/')[0]
    self.tail = self.ports.split('/')[1]

    self.free_side = ''
    if side_used == self.head:
      self.free_side = self.tail
    else:
      self.free_side = self.head

    self.compatible_ports = []
    for idx in range(0, len(remaining_ports)):
      if remaining_ports[idx].split('/')[0] == self.free_side or remaining_ports[idx].split('/')[1] == self.free_side:
        compat_side_used = ''
        if remaining_ports[idx].split('/')[0] == self.free_side:
          compat_side_used = remaining_ports[idx].split('/')[0]
        else:
          compat_side_used = remaining_ports[idx].split('/')[1]

        other_ports = remaining_ports[0:idx]
        other_ports.extend(remaining_ports[idx+1:])
        # print len(other_ports)

        new_node = Node(remaining_ports[idx], compat_side_used, other_ports)
        self.compatible_ports.append(new_node)

  def sum(self):
    return int(self.head) + int(self.tail)

  def get_strengths(self):
    if len(self.compatible_ports) < 1:
      return [self.sum()]
    else:
      strengths = []
      for compat in self.compatible_ports:
        sub_strengths = compat.get_strengths()
        for sub in sub_strengths:
          strengths.append(self.sum() + sub)
      return strengths

  def get_lengths(self):
    if len(self.compatible_ports) < 1:
      return [(1, self.sum())]
    else:
      lengths = []
      for compat in self.compatible_ports:
        sub_lengths = compat.get_lengths()
        for sub in sub_lengths:
          lengths.append((sub[0] + 1, sub[1] + self.sum()))
      return lengths

  def get_strongest(self):
    if len(self.compatible_ports) < 1:
      return self.sum()
    else:
      strongest = 0
      for compat in self.compatible_ports:
        strength = compat.get_strongest()
        if strength > strongest:
          strongest = strength
      return strongest + self.sum()

  def get_longest(self):
    if len(self.compatible_ports) < 1 and self.ports != '0/0': # root
      return 1
    else:
      longest = 1
      for compat in self.compatible_ports:
        length = compat.get_longest()
        if length > longest:
          longest = length
      return longest + 1

  def get_longest_and_strongest(self):
    if len(self.compatible_ports) < 1 and self.ports != '0/0': # root
      return (1, self.sum())
    else:
      current_winner = (0, 0)
      for compat in self.compatible_ports:
        constestant = compat.get_longest_and_strongest()
        if constestant[0] > current_winner[0] and constestant[1] > current_winner[1]:
            current_winner = constestant
      return (current_winner[0] + 1, current_winner[1] + self.sum())


root_node = Node('0/0', '0', available_ports)

print root_node.get_strongest()

### end part 1 ###

# for root in zero_nodes:
#   sub_lengths = root.get_lengths()
#   sub_lengths.sort()
#   print sub_lengths[len(sub_lengths) - 20: ]

print root_node.get_longest()

def len_sort(a, b):
  if a[0] < b[0]:
    return - 1
  elif a[0] > b[0]:
    return 1
  else:
    return 0

def str_sort(a, b):
  if a[1] < b[1]:
    return - 1
  elif a[1] > b[1]:
    return 1
  else:
    return 0

lengths = root_node.get_lengths()
lengths.sort(cmp=str_sort)
lengths.sort(cmp=len_sort)
print lengths[len(lengths) - 1]

# print root_node.get_longest_and_strongest()

