x = int(input())

anos = int(x/365)
meses = int(x%365/30)
dias = int(x%365%30)

print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')