file = open("input13.txt")
file_contents = file.read()
file.close()
file_input = file_contents[0:len(file_contents)-1].split('\n')

# file_input = ['0: 3',
# '1: 2',
# '4: 4',
# '6: 4']
layer_input = {}
deepest_layer = 0
for line in file_input:
  factors = line.split(': ')
  depth = factors[0]
  layer_range = factors[1]
  layer_input[depth] = layer_range

  if depth > deepest_layer:
    deepest_layer = depth

# print deepest_layer

def getSeverity(time_entered):
  severity = 0
  for layer in range(0, int(deepest_layer)+1):
  # for layer in range(0, 20):
    if layer_input.has_key(str(layer)):
      layer_range = int(layer_input[str(layer)])
      scanner_location = (layer + time_entered) % ((layer_range - 1) * 2)

      # if scanner_location == 0 and (layer / layer_range) % 2 == 1:
      #   scanner_location = layer_range - 1


      # print 'layer', layer, layer_range, scanner_location

      if scanner_location == 0:
        if layer == 0:
          severity = 1
        else: 
          severity += layer * layer_range
    else:
      pass
      # print 'layer', layer

  return severity

print getSeverity(0)
# print getSeverity(139656)

picos = 0
while getSeverity(picos) != 0:
  picos += 2

print picos

