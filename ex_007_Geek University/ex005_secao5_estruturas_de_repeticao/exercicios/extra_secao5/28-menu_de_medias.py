print('Digite 3 valores inteiros positivos: ')
x = int(input('Valor1: '))
y = int(input('Valor2: '))
z = int(input('Valor3: '))

print('Selecione Como você quer a média')
print('''Menu de opções
1- Méida Geométrica
2- Média Ponderada
3- Média Harmônica
4- Média Aritmética''')
opcao = int(input('Qual opção você deseja (Número)? '))
if opcao == 1:
    geometrica = pow((x * y * z), 1/3)
    print(f'A média geométrica é: {geometrica}')
elif opcao == 2:
    ponderada = (((x + 2) * (y + 3)) * z) / 6
    print(f'A média ponderada é: {ponderada:.2f}')
elif opcao == 3:
    harmonica = 1 / (1/x) + (1/y) + (1/z)
    print(f'A média harmônica é: {harmonica:.2f}')
elif opcao == 4:
    arimetica = (x + y + z) / 3 
    print(f'A média aritmética é: {arimetica:.2f}')
