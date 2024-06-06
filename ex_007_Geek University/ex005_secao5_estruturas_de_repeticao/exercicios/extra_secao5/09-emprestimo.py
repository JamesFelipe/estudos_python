sal = float(input('Digite o seu salário: '))
emprestimo = float(input('Qual o valor da prestação do emprestimo? '))
minimo = sal * 20 / 100

if emprestimo <= minimo:
    print('Emprestimo pode ser concedidio')
else:
    print('Emprestimo negado')
