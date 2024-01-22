# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa que gere a série até que o valor seja maior que 500.

# Código Bard
def fibonacci(n):
    if n == 0 or n == 1:
        return n

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b


def main():
    n = 0
    while fibonacci(n) <= 500:
        n += 1
        print(fibonacci(n))


if __name__ == "__main__":
    main()
