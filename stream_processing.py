file = open("input9.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0: len(file_contents)-1]
print file_input
# file_input = "{{<ab!>},{<ab>},{<ab>},{<ab>}}" # 9
# file_input = "{{<!!>},{<!!>},{<!!>},{<!!>}}" # 9
# file_input = "{<a>,<a>,<a>,<a>}" # 1
# file_input = "{{<a!>},{<a!>},{<a!>},{<ab>}}" # 3
# file_input = "{{{},{},{{}}}}" # 16
# file_input = "{{<!>},{<!>},{<!>},{<a>}}" # 3

current_depth = 0
total_score = 0

excaped = False
in_garbage = False
garbage_count = 0

for idx in range(0, len(file_input)):
  char = file_input[idx]
  # print 'looking at', char
  if in_garbage == False:
    if char == '{' :
      current_depth +=1
    elif char == '<':
      in_garbage = True
    elif char == '}':
      total_score += current_depth
      current_depth -= 1
  
  elif in_garbage == True:
    if excaped == True:
      excaped = False
    elif char == '!':
      excaped = True
    elif char == '>':
      in_garbage = False
    else:
      garbage_count += 1

print total_score
print garbage_count