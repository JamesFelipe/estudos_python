altura = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo (Masculino/Feminino):  ')).strip().lower()
man = (72.7 * altura) - 58
woman = (62.1 * altura) - 44.7

if sexo == 'masculino':
    print(f'Seu peso ideal seria: {man}')
elif sexo == 'feminino':
    print(f'Seu peso ideal seria: {woman:.2f}')
