operacao_mensagem = ""
def mensagem():
    global x
    x = input(f"Digite quais numeros voce deseja {operacao_mensagem}: ").split()
    x = list(map(int, x))
print("Bem vind@ á Calculadora das 6 operações!")
rodar = True
while rodar:
    operacao = input("""Escolha uma das operações apresentadas abaixo:
Adicão - Subtração - Multiplicação - Divisão - Potenciação - Radiciação
""")
    if operacao != "0":
        if operacao.isalpha() == True:
            operacao = operacao.lower()
            if operacao == "adição":
                operacao_mensagem = "somar"
                mensagem()
                print("O resultado da sua soma é:", x[0] + x[1], "\n")
            elif operacao == "subtração":
                operacao_mensagem = "subtrair"
                mensagem()
                print("O resultado da sua subtração é:", x[0] - x[1], "\n")
            elif operacao == "multiplicação":
                operacao_mensagem = "multiplicar"
                mensagem()
                print("O resultado da sua multiplicação é:", x[0] * x[1], "\n")
            elif operacao == "divisão":
                operacao_mensagem = "dividir"
                mensagem()
                print("O resultado da sua divisão é:", x[0] / x[1], "\n")
            elif operacao == "potenciação":
                operacao_mensagem = "realizar uma potência"
                mensagem()
                print("O resultado da sua potencia é:", x[0] ** x[1], "\n")
            elif operacao == "radiciação":
                operacao_mensagem = "obter a raiz"
                mensagem()
                print("O resultado da sua raiz é:", x[0]**(1/x[1]), "\n")
        else:
            print("Digite uma opção valida.")
    else:
        rodar = False