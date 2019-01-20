x = int(input())
y = int(input())

menor, maior = 0, 0

if(x<y):
  menor, maior = x, y
else:
  menor, maior = y, x

sum = 0

for x in range(menor+1,maior):
  if(x%2==1):
    sum+=x

print(sum)