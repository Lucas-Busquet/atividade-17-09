class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Atleta(Pessoa):
    def __init__(self, nome, idade, modalidade):
        super().__init__(nome, idade)
        self.modalidade = modalidade
    def apresentar(self):
        info = super().apresentar()
        print(f"{info} Eu sou atleta da seguinte modalidade: {self.modalidade}")

class Equipe(Atleta):
    def __init__(self, nome_equipe):
        self.nome_equipe = nome_equipe
        self.lista_atletas = []
    def adicionar_membro(self, membro):
        self.lista_atletas.append(membro)
        return True
    def lista(self):
        for item in self.lista_atletas:
            print(f"Atleta:{item}")
    def contar(self):
        return len(self.lista_atletas)

alt_1 = Atleta("João", 25, "Futebol")
alt_2 = Atleta("Maria", 22, "Natação")
alt_3 = Atleta("Carlos", 28, "Futebol")
            
eq1 = Equipe("Time A")
eq1.adicionar_membro(alt_1.nome)
eq1.adicionar_membro(alt_2.nome)
eq1.adicionar_membro(alt_3.nome)