while True:
    print("----------------------------------------\n"+ " "*10 + "Soma de Caracteres\n\n(1) Somar Números\n(2) Concatenar Caracteres\n----------------------------------------\n")
    op_usr = int(input("Selecione uma opção: "))
    if op_usr in [1,2]:
        break
    else:
        print("Número errado! Pressione ENTER para continuar.")
        input()

if op_usr == 1:
    ter1 = int(input("Digite o primeiro número: "))
    ter2 = int(input("Digite o segundo número: "))
    print("A soma será: " + str(ter1+ter2))
else:
    ter1 = str(input("Digite o primeiro caractere: "))
    ter2 = str(input("Digite o segundo caractere: "))
    print("A concatenação dos dois termos será: " + (ter1+ter2))