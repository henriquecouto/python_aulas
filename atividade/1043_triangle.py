a = float(input())
b = float(input())
c = float(input())

if(b-c < a < b+c and a-c < b < a+c and a-b < c < a+b):
  print(f'Perimetro = {a+b+c}')
else:
  print(f'Área = {(a+b)*c/2}')