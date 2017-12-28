# day 23
file = open("input23.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0:len(file_contents)-1].split('\n')

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Thread:
  def __init__(self, instructions, queue_in, queue_out, thread_id):
    self.instructions = instructions
    self.queue_in = queue_in
    self.queue_out = queue_out
    self.registers = {}
    self.registers['p'] = thread_id
    self.current_location = 0
    self.deadlock = False
    self.send_count = 0
    self.mul_count = 0

  def is_done(self):
    num_instructions = len(self.instructions) - 1
    if self.current_location > num_instructions or self.current_location < 0:
      return True
    else:
      return False

  def step(self):
    # print self.current_location
    command = self.instructions[self.current_location].split(' ')
    op = command[0]
    register = command[1]

    print command

    if self.registers.has_key(register) == False:
      self.registers[register] = 0

    if op == 'set':
      if RepresentsInt(command[2]) == True:
        self.registers[register] = int(command[2])
      else:
        self.registers[register] = self.registers[command[2]]
      self.current_location += 1

    elif op == 'add':
      if RepresentsInt(command[2]) == True:
        self.registers[register] += int(command[2])
      else:
        self.registers[register] += int(self.registers[command[2]])
      self.current_location += 1

    elif op == 'mul':
      if RepresentsInt(command[2]) == True:
        self.registers[register] = self.registers[register] * int(command[2])
        self.mul_count += 1
      else:
        self.registers[register] = self.registers[register] * int(self.registers[command[2]])
        self.mul_count += 1
      self.current_location += 1

    # elif op == 'mod':
    #   if RepresentsInt(command[2]) == True:
    #     self.registers[register] = self.registers[register] % int(command[2])
    #   else:
    #     self.registers[register] = self.registers[register] % int(self.registers[command[2]])
    #   self.current_location += 1

    # elif op == 'rcv':
    #   if len(self.queue_in) > 0:
    #     self.registers[register] = self.queue_in.popleft()
    #     # part one
    #     # self.registers[register] = self.queue_in.pop()
    #     # if self.registers[register] > 0:
    #     #   print 'sound', self.registers[register]
    #     #   self.current_location = len(self.instructions)
    #     self.current_location += 1
    #   else:
    #     self.deadlock = True
    #     self.current_location += 0

    elif op == 'sub':
      if register == 'e' and command[2] == '-1' and self.registers['e'] < 109900:
        # self.registers['g'] = 1
        self.registers['e'] = 109900
        self.current_location += 1
      elif RepresentsInt(command[2]) == True:
        self.registers[register] -= int(command[2])
      else:
        self.registers[register] -= int(self.registers[command[2]])
      self.current_location += 1
    # elif op == 'snd':
    #   self.send_count += 1
    #   if RepresentsInt(register) == True:
    #     self.queue_out.append(int(register))
    #   else:
    #     self.queue_out.append(self.registers[register])
    #   self.current_location += 1
    # elif op == 'jgz':
    #   jgz X Y
    #   check if X is register or int
    #   if RepresentsInt(register) == True:
    #     if int(register) > 0:
    #       if RepresentsInt(command[2]):
    #         self.current_location += int(command[2])
    #       else:
    #         self.current_location += int(self.registers[command[2]])
    #     else:
    #       self.current_location += 1
    #   else:
    #     if int(self.registers[register]) > 0:
    #       if RepresentsInt(command[2]):
    #         self.current_location += int(command[2])
    #       else:
    #         self.current_location += int(self.registers[command[2]])
    #     else:
    #       self.current_location += 1
    elif op == 'jnz':
      # jgz X Y
      # check if X is register or int
      if RepresentsInt(register) == True:
        if int(register) != 0:
          if RepresentsInt(command[2]):
            self.current_location += int(command[2])
          else:
            self.current_location += int(self.registers[command[2]])
        else:
          self.current_location += 1
      else:
        if int(self.registers[register]) != 0:
          if RepresentsInt(command[2]):
            self.current_location += int(command[2])
          else:
            self.current_location += int(self.registers[command[2]])
        else:
          self.current_location += 1

    print " ",self.registers, self.current_location

shared_queue = deque()
new_thread = Thread(file_input, shared_queue, shared_queue, 0)
new_thread.registers['a'] = 1
count = 0
# while new_thread.is_done() == False:
while count < 150:
  count += 1
  new_thread.step()

# print new_thread.mul_count
print new_thread.registers['h']