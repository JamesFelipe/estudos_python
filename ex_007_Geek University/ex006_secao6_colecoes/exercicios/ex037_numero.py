"""
Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive)
possuem a propriedade seguinte: 
a soma dos dois dígitos de mais baixa ordem
com os dois dígitos de mais alta ordem

elevada ao quadrado é igual ao próprio numero. 
Por exemplo, para o inteiro 3025, temos que: 30+25=55
55² = 3025
"""
# Código ChatGpt
def encontrar_numeros_com_propriedade():
    numeros_com_propriedade = []
    
    for numero in range(1000, 9999 + 1):
        # Convertendo o número em string para facilitar a separação dos dígitos
        str_num = str(numero)
        dois_digitos_altos = int(str_num[:2])  # Primeiros dois dígitos
        dois_digitos_baixos = int(str_num[2:])  # Últimos dois dígitos
        
        soma = dois_digitos_altos + dois_digitos_baixos
        if soma ** 2 == numero:
            numeros_com_propriedade.append(numero)
    
    return numeros_com_propriedade

# Executando a função e imprimindo os resultados
numeros = encontrar_numeros_com_propriedade()
print(numeros)
