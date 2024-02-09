'''
Desenvolva a classe Computador e faça as classes Desktop e Notebook herdarem da classe computador
1. Faça um método Sobre para Computador e instancie um Desktop e um Notebook. Faça a chamada e observe o comportamento
    I. Análise: O método Sobre do Computador é o mesmo para o Desktop e o Notebook, o mesmo output é gerado com valores pertinentes a cada subclasse.

2. Faça um novo método Sobre em Desktop e faça a chamada, observe seu comportamento
    II. Análise: Agora o método Sobre para o Desktop sobrescreve o da classe pai, Computador, o output não é o mesmo, mas customizado.

3. Faça uma alteração para Notebook herdar de desktop, chame o método Sobre e observe o resultado
    III. Análise: Agora o método Sobre para a subclasse Notebook é o mesmo da subclasse Desktop, o output é o mesmo da subclasse Desktop.

4. Por fim, faça um método Sobre em Notebook, faça a chama e observe
    IV. Análise: Agora o método Sobre para a subclasse Notebook sobrescreve o antigo método herdado da subclasse Desktop, o output não é o mesmo, mas customizado.
'''

class Computador:
    def __init__(self, memoria, cpu, so):
        self._memoria = memoria
        self._cpu = cpu
        self._so = so
    
    def Ligar(self):
        print(f'\nLigando o computador!')

    def Desligar(self):
        print(f'\nDesligando o computador!')

    def Sobre(self):
        print(f'\nInformações sobre o computador:\n (*) CPU {self._cpu}\n (*) {self._memoria}GB de RAM\n (*) {self._so}')


class Desktop(Computador):
    def __init__(self, memoria, cpu, so):
        super().__init__(memoria, cpu, so)

    def Sobre(self):
        print("É um desktop, sem dúvidas!")

class Notebook(Desktop):
    def __init__(self, memoria, cpu, so):
        super().__init__(memoria, cpu, so)

    def Sobre(self):
        print("É um notebook, sem dúvidas")

desktop1 = Desktop(16, "AMD Ryzen 9", "Arch Linux")
notebook1 = Notebook(4, "Intel Pentium", "Ubuntu")

desktop1.Sobre()
notebook1.Sobre()