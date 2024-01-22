# Faça um programa que peça para n pessoas a sua idade,
# ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
# e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
n = int(input('Digite quantas pessoas você quer adicionar: '))
cont = soma = 0
for i in range(1, n + 1):
    idade = int(input(f'Digite a idade da {i}ª pessoa: '))
    cont += 1
    soma += idade
media = soma / cont
if media > 0 and media <= 25:
    print(f'A média do grupo é de {media} anos e a Turma é Jovem')
elif media > 25 and media <= 60:
    print(f'A média do grupo é de {media} anos e a Turma é Adulta')
elif media > 60:
    print(f'A média do grupo é de {media} anos e a Turma é Idosa')
