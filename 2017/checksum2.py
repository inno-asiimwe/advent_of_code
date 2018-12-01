import sys

file = open("input2.txt")
sum = 0

for row in file:
  if len(row):
    nums = row.split()
    for p in range(0, len(nums)):
      for q in range(0, len(nums)):
        if int(nums[q]) % int(nums[p]) == 0 and nums[p] is not nums[q]:
          sum += int(nums[q]) / int(nums[p])

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