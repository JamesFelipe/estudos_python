"""
Refaça o exercício anterior, identificando o conceito aprovado (média superior a 6), exame (média
entre 4 e 6) ou reprovado (média inferior a 4).
"""
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('DIgite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print(f'Sua média foi {media:.2f}, APROVADO')
elif media < 6 and media >= 4:
    print(f'Sua média foi {media:.2f}, RECUPERAÇÃO')
elif media < 4:
    print(f'Sua média foi {media:.2f}, REPROVADO')
