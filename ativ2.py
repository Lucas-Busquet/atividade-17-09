class planta:
    def __init__(self, especie):
        self.especie = especie

class cacto:
    def __init__(self, especie):
        super().__init__(especie)
meu_cacto=cacto("Opuntia")
print("Espécie do cacto:", meu_cacto.especie)