"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um
código inteiro. Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem
direta; se for 2, mostre o vetor na ordem inversa. Caso, o código for diferente de 1 e 2
escreva uma mensagem informando que o código é inválido.
"""
numeros = []
for x in range(1, 6):
    numero = float(input(f'Digite o {x}º valor: '))
    numeros.append(numero)

numero2 = int(input('Digite um valor inteiro: '))
numeros.append(numero2)
opcao = int(input('''
===== Menu de Opções =====
0 - Para sair do programa
1 - Para mostrar o vetor na ordem direta 
2 - Para mostrar na ordem inversa 

Digite aqui sua opção[Numero]: '''))
match opcao:
    case 0:
        print('Programa encerrado')
    case 1:
        print(f'Ordem direta: {numeros}')
    case 2:
        print(f'Ordem inversa: {sorted(numeros, reverse=True)}')
