class Planta:
    plantas = []

    def __init__(self, nome, nome_cientifico, genero, grupo):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.grupo = grupo
        self.extinta = False
        Planta.plantas.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.nome_cientifico} | {self.genero} | {self.grupo} | {self.extinta}'
    
    def listar_plantas():
        for planta in Planta.plantas:
            print(f'{planta.nome} | {planta.nome_cientifico} | {planta.genero} | {planta.grupo} | {planta.extinta}')

planta_maracuja = Planta('Maracuja', 'Passiflora edulis', 'Passiflora', 'Angiosperma')
planta_jabuticaba = Planta('Jabuticaba', 'Plinia cauliflora', 'Plinia', 'Angiosperma')
planta_araucaria = Planta('Pinheiro','Araucaria angustifolia', 'Araucaria', 'gimnosperma')

Planta.listar_plantas()
