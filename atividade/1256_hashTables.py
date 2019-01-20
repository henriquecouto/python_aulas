n = int(input())

for x in range(n):
  a = input().split(' ')
  m, c = a[0], a[1]
  keys = input().split(' ')
  result = [''] * int(m)
  for x in keys:
    p = int(x) % int(m)
    result[p] = f'{result[p]}{x} -> '
  cont = 0
  for x in result:
    print(f'{cont} -> {x}\\')
    cont+=1


