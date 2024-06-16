numero = int(input("Digite um número entre 100 e 999: "))
if numero >= 100 and numero <= 999:
    for i in str(numero):
        print(i)
else:
    print("Valores fora da faixa")
