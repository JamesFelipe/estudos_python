"""
Faça um programa para ler 10 números DIFERENTES a serem armazenados em um vetor.
Os dados deverão ser armazenados no vetor na ordem que forem sendo lidos, 
sendo que caso o usuário digite um número que já foi digitado anteriormente, 
o programa deverá pedir para ele digitar outro número. 
Note que cada valor digitado pelo usuário deve ser pesquisado no vetor,
verificando se ele existe entre os números que já foram fornecidos. 
Exibir na tela o vetor final que foi digitado.
"""
numeros = []
numero = 1
while numero <= 10:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    elif n in numeros:
        print('Digite um valor diferente(Esse valor não foi adicionado) ')
    numero += 1
    
print(numeros)
