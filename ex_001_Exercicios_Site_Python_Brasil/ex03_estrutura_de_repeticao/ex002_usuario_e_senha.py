# Faça um programa que leia um nome de usuário e a sua senha
# e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input('Digite seu nome de usuário: ').strip()
    senha = input('Digite sua senha: ').strip()
    if nome == senha:
        print('Valores não podem ser iguais, digite outro valor...')
    else:
        print(f'{nome} registrado\n{senha} registrada')
        break
