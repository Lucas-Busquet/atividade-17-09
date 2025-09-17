class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class estudante(pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso
joao=estudante("João", 23, "Engenharia")
print(joao.__dict__)
