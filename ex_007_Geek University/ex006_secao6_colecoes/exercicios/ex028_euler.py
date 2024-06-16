"""
Faça um programa que leia um valor N inteiro e positivo, 
calcule o mostre o valor E, conforme a fórmula a seguir
E=1+1/1!+1/2+1/3!+...+1/N!
"""
# Código ChatGpt
# Solicita ao usuário um valor inteiro e positivo para N
n = int(input("Digite um valor inteiro e positivo para N: "))

# Verifica se o valor de N é válido
if n < 0:
    print("O valor de N deve ser inteiro e positivo.")
else:
    # Inicializa o valor de E como 1
    e = 1
    
    # Calcula o valor de E conforme a fórmula fornecida
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
        e += 1 / fatorial
    
    # Exibe o valor de E
    print(f"O valor de E é: {e:.2f}")
