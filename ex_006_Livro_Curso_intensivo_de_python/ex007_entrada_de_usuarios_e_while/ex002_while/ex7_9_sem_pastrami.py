sandwich_orders = ['pastrami', 'bauru', 'bacon', 'pastrami', 'vegetariano', 'pastrami']
finished_sandwich = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sanduiche in sandwich_orders:
    print(f'Preprei o seu sanduiche de {sanduiche}')
    finished_sandwich.append(sanduiche)
print(f'Lista de sanduiches disponiveis: {finished_sandwich}')
    

