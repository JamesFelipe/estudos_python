n = int(input("Digite um valor inteiro par: "))
if n % 2 == 0:
    for i in range(1, n):
        if i % 2 == 0:
            print(i)
else:
    print("Só aceito números pares")
