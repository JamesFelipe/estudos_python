"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
    
    Homens: (72.7 * h) — 58
    Mulheres: (62,1 * h) - 44,7


"""
altura = float(input('Digite a sua altura: '))
sexo = input('Digite se você é Masculino/Feminino: ').strip().lower()[0]
if sexo == 'm':
    homens = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {homens}')
elif sexo == 'f':
    mulheres = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {mulheres}')
else:
    print('Valor inválido')
