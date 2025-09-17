class planta:
    def __init__(self, especie):
        self.especie = especie

class cacto(planta):
    def __init__(self, especie):
        super().__init__(especie)
meu_cacto=cacto("Opuntia")
print(meu_cacto.especie)
