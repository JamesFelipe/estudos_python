n = int(input("Digite um valor inteiro ímpar: "))
if n % 2 == 1:
    for i in range(1, n):
        if i % 2 == 1:
            print(i)
else:
    print("Só aceito números ímpares")
