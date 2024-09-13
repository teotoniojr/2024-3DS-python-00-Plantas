class Planta:
    plantas = []

    def __init__(self, nome, nome_cientifico, genero, grupo):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.genero = genero
        self.grupo = grupo
        self._extinta = False
        Planta.plantas.append(self)
        
    def __str__(self):
        return f'{self.nome} | {self.nome_cientifico} | {self.genero} | {self.grupo} | {self.extinta}'
    
    def listar_plantas():
        print('''
              
                █▀█ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀   █▀▄ ▄▀█   █▀▄▀█ █ █▄░█ █░█ ▄▀█   █▀▀ ▄▀█ █▀ ▄▀█
                █▀▀ █▄▄ █▀█ █░▀█ ░█░ █▀█ ▄█   █▄▀ █▀█   █░▀░█ █ █░▀█ █▀█ █▀█   █▄▄ █▀█ ▄█ █▀█
                
        ''')
        print(f'{"Nome da planta".ljust(22)} | {"Nome científico".ljust(22)} | {"Gênero".ljust(22)} | {"Grupo".ljust(22)} | {"Extinto"}')
        print('---------------------------------------------------------------------------------------------------------')
        for planta in Planta.plantas:
            print(f'{planta.nome.ljust(22)} | {planta.nome_cientifico.ljust(22)} | {planta.genero.ljust(22)} | {planta.grupo.ljust(22)} | {planta.extinta}')
            
        print('---------------------------------------------------------------------------------------------------------') 
        
    @property
    def extinta(self):
        return '⊘ Extinta' if self._extinta else '❍ Não extinta'

planta_maracuja = Planta('Maracuja', 'Passiflora edulis', 'Passiflora', 'Angiosperma')
planta_jabuticaba = Planta('Jabuticaba', 'Plinia cauliflora', 'Plinia', 'Angiosperma')
planta_araucaria = Planta('Pinheiro','Araucaria angustifolia', 'Araucaria', 'gimnosperma')

Planta.listar_plantas()
