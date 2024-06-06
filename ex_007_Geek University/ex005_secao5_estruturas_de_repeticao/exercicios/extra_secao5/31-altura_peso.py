alt = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))
if alt < 1.20 and peso < 60:
    print('A')
if alt > 1.20 and alt < 1.70 and peso < 60:
    print('B')
if alt > 1.70 and peso <= 60:
    print('C')
if alt < 1.20 and peso > 60 and peso < 90:
    print('D')
if alt > 1.20 and alt < 1.70 and peso > 60 and peso < 90:
    print('E')
if alt > 1.70 and peso > 60 and peso < 90:
    print('F')
if alt < 1.20 and peso > 90:
    print('G')
if alt > 1.20 and alt < 1.70 and peso > 90:
    print('H')
if alt > 1.70 and peso > 90:
    print('I')
