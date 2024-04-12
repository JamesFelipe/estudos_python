convidados = ['Esopo', 'Jesus', 'Kant', 'Izabelly', 'Tesla', 'Ford']

print('Infelismente minha mesa não chegará a tempo, então terei espaço apenas para duas pessoas')
print(f'Sinto muito por isso {convidados.pop()}')
print(f'Sinto muito por isso {convidados.pop()}')
print(f'Sinto muito por isso {convidados.pop()}')
print(f'Sinto muito por isso {convidados.pop()}')
print()

print(f'Você ainda está convidado para o jantar: {convidados[0]}')
print(f'Você ainda está convidado para o jantar: {convidados[1]}')
print()

convidados.pop()
convidados.pop()

print(convidados)
