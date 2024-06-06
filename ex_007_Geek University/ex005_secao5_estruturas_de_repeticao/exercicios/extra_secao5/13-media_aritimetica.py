s1 = s2 = s3 = 0

for n in range(1, 5):
    p1 = float(input(f'Nota{n} da Prova1: '))
    s1 += p1 * 1
print('---' * 30)
for n in range(1, 5):
    p2 = float(input(f'Nota{n} da Prova2: '))
    s2 += p2 * 1
print('---' * 30)
for n in range(1, 5):
    p3 = float(input(f'Nota{n} da Prova3: '))
    s3 += p3 * 2

media_geral = s1 + s2 + s3 / 4
print(f'Sua média geral é: {media_geral}')
if media_geral > 60:
    print('Parabéns você foi APROVADO!')
elif media_geral < 60:
    print('Você foi REPROVADO!')
