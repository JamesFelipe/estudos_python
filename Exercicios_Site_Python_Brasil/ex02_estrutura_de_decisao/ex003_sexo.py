# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input('Digite um letra para cadastrar seu sexo: ').strip().lower()[0]
if sexo == 'f':
    print(f'Sexo "Feminino" registrado')
elif sexo == 'm':
    print(f'Sexo "Masculino" registrado')
else:
    print(f'Valor inválido... Só aceito Masculino/Feminino')
    