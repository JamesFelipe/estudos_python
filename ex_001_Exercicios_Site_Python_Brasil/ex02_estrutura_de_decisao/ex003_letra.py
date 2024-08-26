"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = input('Digite seu sexo[F - Feminino, M - Masculino]: ').upper().strip()
if sexo == "F":
    print('Sexo Feminno registrado com sucesso')
elif sexo == "M":
    print('Sexo Masculino registrado com sucesso')
else:
    print('Valor Inválido')
