premio = float(input('Qual o valor do prêmio? '))
ap1 = float(input('Quanto você apostou? '))
ap2 = float(input('Quanto você apostou? '))
ap3 = float(input('Quanto você apostou? '))

# valor total das aspostas
total = ap1 + ap2 + ap3 

# divisão dos prêmios
premio1 = ap1 / total
premio2 = ap2 / total
premio3 = ap3 / total

# resultados de quanto cada um vai gnhar
print(f'O apostador1 receber: {premio * premio1:.2f}')
print(f'O apostador2 receber: {premio * premio2:.2f}')
print(f'O apostador3 receber: {premio * premio3:.2f}')
