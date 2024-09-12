class Plantas:
    def __init__(self, nome, nome_cientifico, genero, grupo):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.grupo = grupo
        self.extinta = False
        
    def __str__(self):
        return f'{self.nome} | {self.nome_cientifico} | {self.genero} | {self.grupo} | {self.extinta}'

planta_maracuja = Plantas('Maracuja', 'Passiflora edulis', 'Passiflora', 'Angiosperma')
planta_jabuticaba = Plantas('Jabuticaba', 'Plinia cauliflora', 'Plinia', 'Angiosperma')
planta_araucaria = Plantas('Pinheiro','Araucaria angustifolia', 'Araucaria', 'gimnosperma')

plantas = [planta_maracuja, planta_jabuticaba, planta_araucaria]

print(planta_araucaria)
print(planta_maracuja)
