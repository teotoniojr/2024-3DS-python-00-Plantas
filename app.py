from modelos.planta import Planta

planta_maracuja = Planta('Maracuja', 'Passiflora edulis', 'Passiflora', 'Angiosperma')
planta_jabuticaba = Planta('Jabuticaba', 'Plinia cauliflora', 'Plinia', 'Angiosperma')
planta_araucaria = Planta('Pinheiro','Araucaria angustifolia', 'Araucaria', 'gimnosperma')

planta_araucaria.alterar_estado()
planta_jabuticaba.receber_raridade('Paraná', 83)
planta_jabuticaba.receber_raridade('Santa Catarina', 70)
planta_jabuticaba.receber_raridade('Maranhão', 50)


def main():
    Planta.listar_plantas()

if __name__ == '__main__':
    main()