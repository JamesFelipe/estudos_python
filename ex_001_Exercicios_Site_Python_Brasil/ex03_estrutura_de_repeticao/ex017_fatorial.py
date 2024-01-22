# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
# Ex.: 5!=5.4.3.2.1=120
# Código bard
def fatorial(n):
    if n < 0:
        raise ValueError("Número inválido")
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)


def main():
    n = int(input("Digite um número inteiro: "))
    print(f"O fatorial de {n} é {fatorial(n)}")


if __name__ == "__main__":
    main()


