import sys

captcha = sys.argv[1]
sum = 0

if captcha[0] == captcha[len(captcha)-1]:
  sum += int(captcha[0])

for num in range(0, len(captcha) - 1):
  if captcha[num] == captcha[num+1]:
    sum += int(captcha[num])

print sum