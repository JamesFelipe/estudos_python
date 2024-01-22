"""
Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

dados = []
while True:
    nome = input('Digite seu nome[Maior que 3 caracteres]: ')
    if len(nome) < 3:
        print('Digite mais caracteres....')
    else:
        dados.append(nome)
        print('Nome registrado com sucesso')
        break

while True:
    idade = int(input('Digite sua idade[entre 0 e 150]: '))
    if idade > 0 and idade <= 150:
        dados.append(idade)
        print('Idade registrada com sucesso')
        break
    else:
        print('Digite um valor válido...')

while True:
    salario = float(input('Digite seu salário[maior que 0]: '))
    if salario > 0:
        dados.append(salario)
        print('Salário registrado com sucesso')
        break
    else:
        print('Digite um salário válido...')
        
while True:
    sexo = input('Digite seu sexo[F/M]: ').strip().lower()[0]
    if sexo == 'm' or sexo == 'f':
        dados.append(sexo)
        print('Sexo registado com sucesso')
        break
    else:
        print('Valor inválido... Digite um valor válido...')

while True:
    estado_civil = input('Digite seu estado civil[S/C/V/D]: ').strip().lower()
    dados.append(estado_civil)
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil =='d':
        print('Estado civil registrado com sucesso')
        break
    else:
        print('Digite um valor válido...')

print(f'Os dados que você registrou foi: {dados}')
