while True:
    try:
        n = int(input('Digite um valor inteiro: '))
        soma = 0
    except ValueError:
        print('Apenas valores inteiros são aceitos...')
    else:
        while n > 0:
            resto = n % 10
            n = (n - resto) / 10
            soma = soma + resto
    break
print(f'A soma dos números é: {soma}')
