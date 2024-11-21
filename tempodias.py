dias = int(input())

anos = 0
meses = 0

if(dias >= 365):
    anos = int(dias/365)
    dias -= anos * 365 

if(dias >= 30):
    meses = int(dias/30)
    dias -= meses * 30


print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")