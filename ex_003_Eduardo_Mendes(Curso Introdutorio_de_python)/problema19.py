# Faça um programa, com uma função, que calcule a dispersão de uma lista
# Funções embutidas que podem te ajudar:
# min(lista) -> retorna o menor valor
# max(lista) -> retorna o maior valor 

# Código ChatGpt
def calcular_variancia(lista):
    # Calcular a média
    media = sum(lista) / len(lista)
    
    # Calcular a soma dos quadrados das diferenças entre cada valor e a média
    soma_quadrados_diferencas = sum((x - media) ** 2 for x in lista)
    
    # Calcular a variância
    variancia = soma_quadrados_diferencas / len(lista)
    
    return variancia

# Exemplo de uso
dados = [15, 22, 29, 31, 36, 40, 42, 51, 52, 57]

# Chamar a função para calcular a dispersão (variância)
dispersao = calcular_variancia(dados)

# Imprimir o resultado
print(f"A dispersão (variância) dos dados é: {dispersao}")
