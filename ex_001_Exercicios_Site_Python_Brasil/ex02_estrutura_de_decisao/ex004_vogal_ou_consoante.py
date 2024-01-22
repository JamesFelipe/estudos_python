# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input('Digite uma letra: ')
if letra in 'a e i o u'.split():
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')
    