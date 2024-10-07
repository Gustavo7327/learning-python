from math import sqrt


def fatorial(num):
    result = 1
    for x in range(num,1,-1):
        result *= x    
    return result

def maiorAB(num1,num2):
    if(num1 < num2):
        return num2
    else:
        return num1

def pow(num, pot):
    pot
    result = num
    for x in range(1,pot):
        result *= num
    return result

def sqrt2(num):
    num = num ** 0.5
    return num

def descobrirCateto(cat1,hipo):
    cat2 = pow(hipo,2) - pow(cat1,2)
    cat2 = sqrt(cat2)
    print(cat2)

def descobrirHipotenusa(cat1,cat2):
    hipo = pow(cat1,2) + pow(cat2,2)
    hipo = sqrt(hipo)
    print(hipo)

def pitagoras():
    dec = int(input("Escolha uma decisao: \nDescobrir cateto = 1 \nDescobrir hipotenusa = 2\n"))
    if(dec ==  1):
        descobrirCateto(int(input("cateto: ")), int(input("hipotenusa: ")))
    elif(dec == 2):
        descobrirHipotenusa(int(input("cateto1: ")),int(input("cateto2: ")))
    else:
        print("Operacao invalida!")

def eq2grau(coeficienteA, coeficienteB, coeficienteC):
    delta = pow(coeficienteB,2) - 4*coeficienteA*coeficienteC
    if(delta < 0):
        print("Equacao nao possui raizes reais")
    elif(delta == 0):
        x = (coeficienteB*-1)/(2*coeficienteA)
        print("x = {}".format(x))
    elif(delta > 0):
        x1 = (coeficienteB*-1 + sqrt2(delta))/(2*coeficienteA)
        print("x1 = {}".format(x1))
        x2 = (coeficienteB*-1 - sqrt2(delta))/(2*coeficienteA)
        print("x2 = {}".format(x2))
    else:
        print("Operacao invalida!")

def verticeeq2Grau(coeficienteA, coeficienteB, coeficienteC):
    xV = (coeficienteB)*-1/(2*coeficienteA)
    delta = pow(coeficienteB,2) - 4*coeficienteA*coeficienteC
    yV = (delta*-1)/(4*coeficienteA)
    print("xV = {} \nyV = {}".format(xV, yV))

def valorMinAndValorMax(coeficienteA,coeficienteB,coeficienteC):
    delta = pow(coeficienteB,2) - 4*coeficienteA*coeficienteC
    yV = (delta*-1)/(4*coeficienteA)
    if(coeficienteA < 0):
        print("Valor Max = {}".format(yV))
    elif(coeficienteA > 0):
        print("Valor Min = {}".format(yV))

def jurosSimples(capital,taxaPorcento,tempo):
    taxaPorcento /= 100
    juros = capital*taxaPorcento*tempo
    montante = capital + juros
    print("Juros = {:.2f} \nMontante = {:.2f}".format(juros,montante))

def jurosCompostos(capital,taxafixa,tempo):
    taxafixa /= 100
    montante = capital*pow(1+taxafixa,tempo)
    juros = montante - capital
    print("Montante = {:.2f} \nJuros = {:.2f}".format(montante,juros))
