valor = int(input())
valorz = valor
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0

if(valor >= 100):
    nota100 += int(valor/100)
    valor -= nota100 * 100

if(valor >= 50):
    nota50 += int(valor/50)
    valor -= nota50 * 50

if(valor >= 20):
    nota20 += int(valor/20)
    valor -= nota20 * 20

if(valor >= 10):
    nota10 += int(valor/10)
    valor -= nota10 * 10

if(valor >= 5):
    nota5 += int(valor/5)
    valor -= nota5 * 5

if(valor >= 2):
    nota2 += int(valor/2)
    valor -= nota2 * 2

if(valor == 1):
    nota1 += int(valor/1)
    valor -= nota1 * 1

print(valorz)
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")