file = open("input20.txt")
file_contents = file.read()
file.close()
raw_particle_data = file_contents[0:len(file_contents)-1].split('\n')

class Particle(object):
  """docstring for Particle"""
  def __init__(self, pid, p, v, a):
    self.pid = pid
    self.p = p
    self.v = v
    self.a = a

  def details(self):
    print self.p, self.v, self.a

  def manhattan(self):
    return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

  def manhattan_acceleration(self):
    return abs(self.a[0]) + abs(self.a[1]) + abs(self.a[2])

def location_sort(a, b):
  a_manhattan = a.manhattan()
  b_manhattan = b.manhattan()

  if a_manhattan < b_manhattan:
    return -1
  elif b_manhattan < a_manhattan:
    return 1
  else:
    return 0

def acceleration_sort(a, b):
  a_manhattan = a.manhattan_acceleration()
  b_manhattan = b.manhattan_acceleration()

  if a_manhattan < b_manhattan:
    return -1
  elif b_manhattan < a_manhattan:
    return 1
  else:
    return 0

def to_int(x): return int(x)

particles = []
for i in range(0, len(raw_particle_data)):
  particle = raw_particle_data[i]
  info = particle.split(', ')
  position_data = info[0][3:len(info[0]) - 1].split(',')
  position_data  = list(map((lambda x: int(x)), position_data))
  velocity_data  = info[1][3:len(info[1]) - 1].split(',')
  velocity_data  = list(map((lambda x: int(x)), velocity_data))
  acceleration_data = info[2][3:len(info[2]) - 1].split(',')
  acceleration_data  = list(map((lambda x: int(x)), acceleration_data))
  particles.append(Particle(i, position_data, velocity_data, acceleration_data))

particles.sort(cmp=location_sort)

for i in range(0, 10):
  print particles[i].manhattan(), particles[i].manhattan_acceleration()

particles.sort(cmp=acceleration_sort)

for i in range(0, 10):
  print particles[i].manhattan(), particles[i].manhattan_acceleration()


print particles[0].pid