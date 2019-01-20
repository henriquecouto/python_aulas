n = int(input())

nIn, nOut = 0, 0

for x in range(n):
  a = int(input())
  if(a>=10 and a<=20):
    nIn += 1
  else:
    nOut += 1

print(f'{nIn} in\n{nOut} out')