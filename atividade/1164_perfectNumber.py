n = int(input())

for x in range(n):
  divisores = 0
  a = int(input())
  for y in range(a-1):
    value = y+1
    if(a%(value) == 0):
      divisores += value

  if(divisores == a):
    print(f'{a} eh perfeito ')
  else:
    print(f'{a} nao eh perfeito ')
  