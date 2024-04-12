minhas_pizzas = ['catupiry', '4 queijos', 'portuguesa']
friend_pizzas = minhas_pizzas[::]
print(minhas_pizzas)
print(friend_pizzas)
minhas_pizzas.append('calabresa')

print('Minhas pizzas favoritas são: ')
for m_pizza in minhas_pizzas:
    print(m_pizza)
print()

friend_pizzas.append('chocolate')
print('As pizzas favoritas do meu amigo são: ')
for f_pizza in friend_pizzas:
    print(f_pizza)
