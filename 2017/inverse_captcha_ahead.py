import sys

captcha = sys.argv[1]
sum = 0
half = len(captcha)/2

# if captcha[0] == captcha[len(captcha)-1]:
#   sum += int(captcha[0])

for num in range(0, half):
# first half
  if captcha[num] == captcha[num+half]:
    sum += int(captcha[num])
# second half
  if captcha[num+half] == captcha[num]:
    sum += int(captcha[num])

print sum