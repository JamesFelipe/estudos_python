from datetime import date, time
while True:
    try:
        atual = date.today().year
        idade = int(input('Digite sua idade inteira: '))
        anos = atual - idade
    except ValueError:
        print('Apenas valores inteiros são aceitos...')
    else:
        print(f'O ano de seu nascimento é: {anos}') 
        break
