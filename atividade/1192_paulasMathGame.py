n = int(input())

for x in range(n):
  a = list(input())
  
  result = None
  
  if(a[0] == a[2]):
    result = int(a[0]) * int(a[2])
  elif(a[1].istitle()):
    result = int(a[2]) - int(a[0])
  elif(not a[1].istitle()):
    result = int(a[0]) + int(a[2])
  
  print(result)