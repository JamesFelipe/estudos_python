trab_lab = float(input('Digite sua nota no trabalho de laboratório: '))
aval_sem = float(input('Qual sua nota da avaliação semestral? '))
exa_final = float(input('Qual sua nota no exame final: '))
media = ((trab_lab * 2) + (aval_sem * 3) + (exa_final * 5)) / (2 + 3 + 5)
print(f'Sua média podenderada é: {media}')
if media == 0 and media < 2.9:
    print(f'Sua média é: {media} - Você está REPROVADO!')
elif media >= 3 and media <= 4.9:
    print(f'Sua média é: {media} - Bem vindo a RECUPERAÇÃO!')
elif media >= 5:
    print(f'Sua média é: {media} - PARABÉNS VOCÊ FOI APROVADO') 
