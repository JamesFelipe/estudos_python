"""
Considere um dicionário com 5 nomes de alunos e suas notas. Escreva um programa que calcule
a média dessas notas.
"""
alunos = {
    'Ana': 10.00,
    'Ellen': 8.00,
    'Marcos': 10.00,
    'Naldo': 10.00,
    'Zuleica': 0.0
}
print(f'A média dos alunos é: {sum(alunos.values()) / len(alunos.values())}')
