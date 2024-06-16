"""
Dados n e dois números inteiros positivos, i e j, 
diferentes de 0, 
imprimir em ordem crescente os n primeiros naturais 
que são múltiplos de i ou de j e ou de ambos. 
Exemplo: Para n = 6, i = 2 e j = 3 a saída deverá ser: 0,2,3,4,6,8.
"""
# int(input("Digite o valor de n: "))
n = 6
if n != 0:
    # int(input("Digite o valor de i: "))
    i = 2
    # int(input("Digite o valor de j: "))
    j = 3
    for j in range(0, n-1):
        j *= i
        print(j, end=", ")
    print("Fim")
else:
    print("Valor inválido")
