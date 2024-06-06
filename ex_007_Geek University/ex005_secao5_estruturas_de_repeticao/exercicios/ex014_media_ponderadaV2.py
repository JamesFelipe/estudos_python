"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de O até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. 

A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; 
       Avaliação Semestral: 3;
       Exame Final: 5. 
       
De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""
trabalho_laboratorio = float(input('Digite a nota do trabalho de laboratorio: '))
avaliacao_semestral = float(input('Digite sua nota da avaliação semestral: '))
exame_final = float(input('Digite sua nota do exame final: '))
media = (trabalho_laboratorio * 2 + avaliacao_semestral * 3 + exame_final * 5) / (2 + 3 + 5)
if media <= 2.9:
    print(f'A média é: {media:.2f}, Aluno Reprovado')
elif media >= 3 and media <= 4.9:
    print(f'A média é: {media:.2f}, Aluno em Recuperação')
elif media >= 5:
    print(f'A média é: {media}, Aluno Aprovado')
