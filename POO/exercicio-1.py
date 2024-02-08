class Computador:
    def __init__(self, memoria, cpu, so):
        self._memoria = memoria
        self._cpu = cpu
        self._so = so
        pass

    def Ligar(self):
        print(f'\nLigando o computador!')

    def Desligar(self):
        print(f'\nDesligando o computador!')
    
    def Sobre(self):
        print(f'\nInformações sobre o computador:\n (*) CPU {self._cpu}\n (*) {self._memoria}GB de RAM\n (*) {self._so}')


meu_computador = Computador("16", "Ryzen 9", "ArchLinux")
print("------------------------\n" + ' '*10 + "MENU" + "\n------------------------\n(1) Ligar computador\n(2) Desligar computador\n(3) Info\n------------------------")
while True:
    usr_input = int(input('Digite a opção: '))
    if usr_input in [1,2,3]:
        break

meu_computador.Ligar() if usr_input == 1 else meu_computador.Desligar() if usr_input == 2 else meu_computador.Sobre()