from math import sqrt

file = open("input21.txt")
file_contents = file.read()
file.close()
raw_rules = file_contents[0:len(file_contents)-1].split('\n')

canvas = '.#./..#/###'
# raw_rules = ['../.# => ##./#../...','.#./..#/### => #..#/..../..../#..#']

rule_book = {}
for rule_line in raw_rules:
  rule = rule_line.split(' => ')
  rule_book[rule[0]] = rule[1]
# print rule_book

def parse_canvas(canvas):
  rows = canvas.split('/')
  new_canvas = []
  for row in rows:
    new_row = []
    for char in row:
      new_row.append(char)
    new_canvas.append(new_row)
  return new_canvas

def flip(canvas):
  new_canvas = []
  canvas_size = len(canvas)
  for row in range(0, canvas_size):
    new_canvas.append([])
    for col in range(0, canvas_size):
      new_canvas[row].append(canvas[row][canvas_size - 1 - col])
  return new_canvas

def rotate(canvas, num):
  canvas = parse_canvas(str_canvas(canvas))
  canvas_size = len(canvas)
  new_canvas = []
  for i in range(0, num):
    new_canvas = []
    for col in range(0, canvas_size):
      new_canvas.append([])
      for row in range(0, canvas_size):
        new_canvas[col].append(canvas[canvas_size - 1 - row][col])
    canvas = new_canvas

  return new_canvas

def str_canvas(canvas):
  string = ''
  canvas_len = len(canvas)
  for row in range(0, canvas_len):
    for col in canvas[row]:
      string += col
    if row < canvas_len - 1:
      string += '/'
  return string

def divide_canvas(canvas, num):
  divisions = len(canvas) / num
  # print 'divisions', divisions
  canvas_list = []
  for row_divisions in range(0, divisions):
    for col_divisions in range(0, divisions):
      sub_canvas = []
      for row in range(row_divisions * num, (row_divisions + 1) * num):
        sub_canvas.append([])
        for col in range(col_divisions * num, (col_divisions + 1) * num):
          sub_canvas[len(sub_canvas) - 1].append(canvas[row][col])
      canvas_list.append(sub_canvas)
  return canvas_list

def find_match(canvas):
  key = str_canvas(canvas)
  # print 'key', key
  if rule_book.has_key(key):
    # print 'found match!'
    return parse_canvas(rule_book[key])

  for rotate_count in range(1, 4):
    rotated_canvas = rotate(canvas, rotate_count)
    rotate_key = str_canvas(rotated_canvas)
    # print 'rotate key', rotate_key
    if rule_book.has_key(rotate_key):
      # print 'found rotate match!'
      return parse_canvas(rule_book[rotate_key])

  flipped_canvas = flip(canvas)
  flipped_key = str_canvas(flipped_canvas)
  # print 'flipped key', flipped_key
  if rule_book.has_key(flipped_key):
    # print 'found flip match!'
    return parse_canvas(rule_book[flipped_key])

  for rotate_count in range(1, 4):
    flipped_rotated_canvas = rotate(flipped_canvas, rotate_count)
    rotate_key = str_canvas(flipped_rotated_canvas)
    # print 'rotate key', rotate_key
    if rule_book.has_key(rotate_key):
      # print 'found flip rotate match!'
      return parse_canvas(rule_book[rotate_key])

  print 'NO MATCH'



def match_canvases(canvas_list):
  new_sections = []
  for canvas in canvas_list:
    # print 'searching'
    # for row in canvas:
    #   print row
    new_sections.append(find_match(canvas))

  # print 'new_sections', new_sections
  new_canvas = []
  canvas_size = int(sqrt(len(new_sections)))
  # print 'canvas_size', canvas_size
  part_size = len(new_sections[0])
  # print 'part_size', part_size
  for i in range(0, canvas_size * part_size):
    new_canvas.append([])

  for new_row in range(0, canvas_size):
    row_sections = new_sections[new_row * canvas_size: (new_row + 1) * canvas_size]
    for section in row_sections:
      for row in range(0, part_size):
        destiation = new_row * part_size + row
        # print destiation
        new_canvas[destiation].extend(section[row])

  return new_canvas



canvas_canvas = parse_canvas(canvas)
print 'canvas'
for row in canvas_canvas:
  print row
print

###### tests ######
# print 'rotated_canvas 1'
# rotated_canvas = rotate(canvas_canvas, 1)
# for row in rotated_canvas:
#   print row
# print

# print 'rotated_canvas 2'
# rotated_canvas = rotate(canvas_canvas, 2)
# for row in rotated_canvas:
#   print row
# print

# print 'rotated_canvas 3'
# rotated_canvas = rotate(canvas_canvas, 3)
# for row in rotated_canvas:
#   print row
# print

# print 'rotated_canvas 4'
# rotated_canvas = rotate(canvas_canvas, 4)
# for row in rotated_canvas:
#   print row
# print

# print 'flip'
# flipped_canvas = flip(canvas_canvas)
# for row in flipped_canvas:
#   print row

# print str_canvas(flipped_canvas)
###### end tests ######

iterations = 18
canvas = parse_canvas(canvas)

for iteration in range(0, iterations):
  canvas_len = len(canvas)

  if canvas_len % 2 == 0:
    # print 'len', 2
    canvas_list = divide_canvas(canvas, 2)
    new_canvas = match_canvases(canvas_list)
    # print 'new_canvas'
    # for row in new_canvas:
    #   print row
    canvas =  new_canvas
  elif canvas_len % 3 == 0:
    # print 'len', 3
    canvas_list = divide_canvas(canvas, 3)
    new_canvas = match_canvases(canvas_list)
    # print 'new_canvas'
    # for row in new_canvas:
    #   print row
    canvas = new_canvas

# print
# print 'final:'
# for row in canvas:
#   print row

on_count = 0
for row in canvas:
  for col in row:
    if col == '#':
      on_count += 1

print 'on count', on_count