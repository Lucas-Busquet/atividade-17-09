class Planta:
    def __init__(self, especie):
        self.especie = especie

class Cacto(Planta):
    def __init__(self, especie):
        super().__init__(especie)
meu_cacto = Cacto("Opuntia")
print(meu_cacto.especie)
