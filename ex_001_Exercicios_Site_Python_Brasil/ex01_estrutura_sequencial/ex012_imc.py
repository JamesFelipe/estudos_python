"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Digite sua altura: '))
ideal = (72.7*altura) - 58
print(f'Sua altura é: {altura} e seu peso ideal é: {ideal:.2f}')
