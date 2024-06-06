print(''' |===> Menu de Opções <===|
1- Soma
2- Subtração
3- Multiplicação
4- Divisão ''')

op: str = input('\033[32mEscolha uma opção: \033[m').strip().lower()
if op == '1' or op == 'soma':
    n1: int = int(input('Digite a primeira parcela: '))
    n2: int = int(input('Digite a segunda parcela: '))
    print(f'Soma: {n1} + {n2} = {n1 + n2}')
elif op == '2' or op == 'subtracao':
    n1: int = int(input('Digite o minuendo: '))
    n2: int = int(input('Digite o subtraendo: '))
    print(f'Resto: {n1} - {n2} = {n1 - n2}')
elif op == '3' or op == 'multiplicao':
    n1: int = int(input('Digite o multiplicando: '))
    n2: int = int(input('Digite o mutiplicador: '))
    print(f'Produto: {n1} X {n2} = {n1 * n2}')
elif op == '4' or op == 'divisao':
    n1: int = int(input('Digite dividendo: '))
    n2: int = int(input('Digite o divisor: '))
    print(f'Quociente: {n1} / {n2} = {n1 / n2}')
else:
    print('Valor inesitente')
