lista = []
quantidade = 3
for i in range(quantidade):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = False) 
print(lista)
