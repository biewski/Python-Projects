outra_soma = True
a = 0
b = 0


# Começo funções

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multiplicar(a, b):
    return a * b

def resto(a, b):
    return a % b

#Fim funções

while(outra_soma):
    operacao = input("Qual operação você deseja usar? (+, -, /, *): ")
    while operacao not in ["+", "-", "*", "/"] :
        print("Operação Inválida!")
        operacao = input("Qual operação você deseja usar? (+, -, /, *, %): ")

    a, b = input("Digite dois numeros separados por um espaço: ").split()
    a = int(a)
    b = int(b)
    if b ==  0:
        print("Você precisa deixar um espaço em branco entre os dois numeros!")
    if (operacao == "+"):
        print(somar(a, b))
    elif (operacao == "-"):
        print(subtrair(a, b))
    elif (operacao == "/"):
        print(dividir(a, b))
    elif (operacao == "*"):
        print(multiplicar(a, b))
    elif (operação == "%"):
        print(resto(a, b))
    else :
        print("Você deve escolher um dos operadores à cima!")
        continue

    yn = ""
    while (True):
        if yn == "y":
            break
        elif yn == "n":
            outra_soma = False
            break
        else :
            if (yn == ""):
                yn = input("Deseja fazer outra soma? (y/n): ")
                continue
            else :
                yn = input("Resposta inválida, escolha apenas entre (y/n): ")
                continue
