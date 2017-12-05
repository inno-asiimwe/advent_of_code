import sys

target = int(sys.argv[1])

ring = 1
largest_in_ring = 1

while target > largest_in_ring :
  largest_in_ring += 8 * ring
  ring += 1

print "Ring"
print ring
print "Largest"
print largest_in_ring

if target is largest_in_ring:
  print ring * 2

size_of_side = ring * 2 - 1
distance_to_center = (size_of_side - 1) / 2

print "Size of side"
print size_of_side
print "Distance to center"
print distance_to_center

start_of_ring = largest_in_ring - (8 * (ring - 1))
number_in_ring = target - start_of_ring

print "Start of ring"
print start_of_ring
print "Num in ring"
print number_in_ring

side = number_in_ring / size_of_side
middle_of_side = start_of_ring + (side * (size_of_side - 1)) + distance_to_center


print "side"
print side
print "middle_of_side"
print middle_of_side

print "answer:"

if target is middle_of_side:
  print ring - 1
else:
  print abs(target - middle_of_side) + (ring - 1)
# for row in file:
#   if len(row):
#     nums = row.split()
#     for p in range(0, len(nums)):
#       for q in range(0, len(nums)):
#         if int(nums[q]) % int(nums[p]) == 0 and nums[p] is not nums[q]:
#           sum += int(nums[q]) / int(nums[p])

# print sum

# # if captcha[0] == captcha[len(captcha)-1]:
# #   sum += int(captcha[0])

# for num in range(0, half):
# # first half
#   if captcha[num] == captcha[num+half]:
#     sum += int(captcha[num])
# # second half
#   if captcha[num+half] == captcha[num]:
#     sum += int(captcha[num])

# print sum