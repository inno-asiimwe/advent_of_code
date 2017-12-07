file = open("input6.txt")
file_contents = file.read()
file.close()
input_banks = file_contents[0: len(file_contents)-1].split('\t')

banks = []
for bank in input_banks:
  banks.append(int(bank))
print banks

def reallocate(memory):
  idx_of_largest = 0
  for idx in range(0, len(memory)):
    if memory[idx] > memory[idx_of_largest]:
      idx_of_largest = int(idx)

  memory_to_allocate = memory[idx_of_largest]
  memory[idx_of_largest] = 0

  bucket_to_fill = idx_of_largest
  while memory_to_allocate > 0:
    if bucket_to_fill < 15:
      bucket_to_fill += 1
    else: 
      bucket_to_fill = 0

    memory[bucket_to_fill] += 1
    memory_to_allocate -= 1

in_loop = True
seen = {}
count = 0
loops = 0
while in_loop:
  if seen.has_key(str(banks)):
    in_loop = False
    print loops - seen[str(banks)]
  else:
    seen[str(banks)] = loops
    count += 1
    loops += 1
    reallocate(banks)

print count