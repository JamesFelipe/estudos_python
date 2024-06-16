n = int(input("Digite um valor inteiro par: "))
if n % 2 == 1:
    for i in range(n, 1, -1):
        if i % 2 == 1:
            print(i)
else:
    print("Só aceito números ímpares")
