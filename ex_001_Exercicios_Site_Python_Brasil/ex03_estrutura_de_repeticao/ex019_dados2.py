# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
n = int(input('Digite quantas valores você quer adicionar: '))
numeros = []
for i in range(1, n + 1):
    numero =int (input(f'Digite o {i}º valor: '))
    if numero > 0 and numeros <= 1000:
        numeros.append(numero)
    else:
        numeros.append(0)
        print('Valor inválido, Digite números entre 0 e 1000...')
        break
print(f'O menor valor é o número: {min(numeros)}')
print(f'O maior valor é o número: {max(numeros)}')
print(f'A soma dos valores digitados é: {sum(numeros)}')
