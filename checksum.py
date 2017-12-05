import sys

file = sys.argv[1].split('\n')
sum = 0

for row in file:
  if len(row):
    nums = row.split()
    smallest = int(nums[0])
    largest = int(nums[0])
    for char in nums:
      current = int(char)
      if current > largest:
        largest = current
      elif current < smallest:
        smallest = current
    sum += largest - smallest

print sum

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