"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.
"""
temperaturas = []
while True:
    temperatura = float(input('Digite uma temperatura[0 para sair]: '))
    if temperatura > 0.0:
        temperaturas.append(temperatura)
    else:
        break

print(f'A menor temperatura é: {min(temperaturas)} e a maior temperatura é: {max(temperaturas)}')
print(f'A média das temperaturas digitadas é: {sum(temperaturas) / len(temperaturas)}')


