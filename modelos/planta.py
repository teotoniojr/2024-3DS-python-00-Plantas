from modelos.raridade import Raridade

class Planta:
    plantas = []

    def __init__(self, nome, nome_cientifico, genero, grupo):
        self._nome = nome.upper()
        self._nome_cientifico = nome_cientifico.title()
        self._genero = genero
        self._grupo = grupo.title()
        self._extinta = False
        self._raridade = []
        Planta.plantas.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._nome_cientifico} | {self._genero} | {self._grupo} | {self.extinta}'
    
    @classmethod
    def listar_plantas(cls):
        print('''
              
                █▀█ █░░ ▄▀█ █▄░█ ▀█▀ ▄▀█ █▀   █▀▄ ▄▀█   █▀▄▀█ █ █▄░█ █░█ ▄▀█   █▀▀ ▄▀█ █▀ ▄▀█
                █▀▀ █▄▄ █▀█ █░▀█ ░█░ █▀█ ▄█   █▄▀ █▀█   █░▀░█ █ █░▀█ █▀█ █▀█   █▄▄ █▀█ ▄█ █▀█
                
        ''')
        print(f'{"Nome da planta".ljust(22)} | {"Nome científico".ljust(22)} | {"Gênero".ljust(22)} | {"Grupo".ljust(22)} | {"Extinto".ljust(22)} | {"Raridade em %"}')
        print('------------------------------------------------------------------------------------------------------------------')
        for planta in cls.plantas:
            print(f'{planta._nome.ljust(22)} | {planta._nome_cientifico.ljust(22)} | {planta._genero.ljust(22)} | {planta._grupo.ljust(22)} | {planta.extinta.ljust(22)} | {planta.media_porcentagem} ')
            
        print('------------------------------------------------------------------------------------------------------------------') 
        
    @property
    def extinta(self):
        return '⊘ Extinta' if self._extinta else '❍ Não extinta'
    
    def alterar_estado(self):
        self._extinta = not self._extinta
    
    def receber_raridade(self, estado, porcentagem):
        raridade = Raridade(estado, porcentagem)
        self._raridade.append(raridade)
        
    @property
    def media_porcentagem(self):
        if not self._raridade:
            return 0
        soma_das_porcentagens = sum(raridade._porcentagem for raridade in self._raridade)
        quantidade_estados = len(self._raridade)
        media = round(soma_das_porcentagens/quantidade_estados, 1)
        return media
    
    

