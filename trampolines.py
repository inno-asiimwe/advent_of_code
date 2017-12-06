file = open("input5.txt")
steps = []
for line in file:
  steps.append(int(line))

step_count = 0
current = 0
previous = 0

while current >= 0 and current < len(steps):
  current = steps[current] + current
  steps[previous] += 1
  previous = current
  step_count += 1

print step_count