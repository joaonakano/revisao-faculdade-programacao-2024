def Fatorial(a):
    if a == 0:
        return 1
    else:
        return a * Fatorial(a-1)
    
input_usr = int(input("Digite um número para transformá-lo em fatorial: "))
print(f"O fatorial do número {input_usr} será igual a " + str(Fatorial(input_usr)))