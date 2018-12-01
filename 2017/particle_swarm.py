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

  def update_location(self):
    self.v[0] += self.a[0]
    self.v[1] += self.a[1]
    self.v[2] += self.a[2]
    self.p[0] += self.v[0]
    self.p[1] += self.v[1]
    self.p[2] += self.v[2]

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

# for i in range(0, 10):
  # print particles[i].manhattan(), particles[i].manhattan_acceleration()

particles.sort(cmp=acceleration_sort)

# for i in range(0, 10):
  # print particles[i].manhattan(), particles[i].manhattan_acceleration()


print 'closest to center', particles[0].pid


### end part 1 ###
### part two: guess and check ###
def xyz_sort(a, b):
  if a.p[0] < b.p[0]:
    return -1
  elif b.p[0] < a.p[0]:
    return 1
  elif a.p[1] < b.p[1]:
    return -1
  elif b.p[1] < a.p[1]:
    return 1
  elif a.p[2] < b.p[2]:
    return -1
  elif b.p[2] < a.p[2]:
    return 1
  else:
    return 0

def check_for_collisions(particle_list):
  free_particles = []
  particle_list.sort(cmp=xyz_sort)
  for i in range(0, len(particle_list) - 1):
    if i > 0:
      if particle_list[i].p != particle_list[i + 1].p and particle_list[i].p != particle_list[i - 1].p:
        free_particles.append(particle_list[i])
      # else: 
        # print 'collision!'
    else:
      if particle_list[i].p != particle_list[i + 1].p:
        free_particles.append(particle_list[i])
      # else: 
        # print 'collision!'

    if i == len(particle_list) - 2:
      if particle_list[i].p != particle_list[i + 1].p:
        free_particles.append(particle_list[i + 1])
  return free_particles

def update_all_locations(particle_list):
  for particle in particle_list:
    particle.update_location()


particles_in_motion = particles
sims = 1000
while sims > 0:
  sims -= 1
  particles_in_motion = check_for_collisions(particles_in_motion)
  update_all_locations(particles_in_motion)

print len(particles_in_motion)