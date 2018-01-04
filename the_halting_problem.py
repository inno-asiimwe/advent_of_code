# Begin in state A.
state = 'A'
# Perform a diagnostic checksum after 12302209 steps.
steps = 12302209
# steps = 6

tape = [0]
cursor = 0

current_step = 0

def update_tape(new_value, idx_update, new_state):
  global cursor, tape, state
  tape[cursor] = new_value
  cursor += idx_update
  state = new_state

while current_step < steps:
  current_step += 1

  # check tape idx
  if cursor == len(tape):
    tape.append(0)
  elif cursor == -1:
    new_tape = [0]
    new_tape.extend(tape)
    tape = new_tape
    cursor += 1

  # print tape, cursor, state
  current_value = tape[cursor]

# In state A:
  if state == 'A':
  # If the current value is 0:
    if current_value == 0:
    # - Write the value 1.
    # - Move one slot to the right.
    # - Continue with state B.
      update_tape(1, 1, 'B')
  # If the current value is 1:
    else:
  #   - Write the value 0.
  #   - Move one slot to the left.
  #   - Continue with state D.
      update_tape(0, -1, 'D')

# In state B:
  elif state == 'B':
  # If the current value is 0:
    if current_value == 0:
  #   - Write the value 1.
  #   - Move one slot to the right.
  #   - Continue with state C.
      update_tape(1, 1, 'C')
  # If the current value is 1:
    else:
  #   - Write the value 0.
  #   - Move one slot to the right.
  #   - Continue with state F.
      update_tape(0, 1, 'F')

# In state C:
  elif state == 'C':
#   If the current value is 0:
    if current_value == 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state C.
      update_tape(1, -1, 'C')
#   If the current value is 1:
    else:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
      update_tape(1, -1, 'A')

# In state D:
  elif state == 'D':
#   If the current value is 0:
    if current_value == 0:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state E.
      update_tape(0, -1, 'E')
#   If the current value is 1:
    else:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A.
      update_tape(1, 1, 'A')

# In state E:
  elif state == 'E':
#   If the current value is 0:
    if current_value == 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
      update_tape(1, -1, 'A')
    else:
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state B.
      update_tape(0, 1, 'B')

# In state F:
  elif state == 'F':
#   If the current value is 0:
    if current_value == 0:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state C.
      update_tape(0, 1, 'C')
#   If the current value is 1:
    else:
#     - Write the value 0.
#     - Move one slot to the right.
#     - Continue with state E.
      update_tape(0, 1, 'E')

  # print tape, cursor, state
  # print

checksum = 0
for val in tape:
  if val:
    checksum += 1

print checksum