"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

"""
# Código Bard
# Declaração de variáveis
tamanho = float()
velocidade = float()
tempo = float()

# Entrada de dados
print("Qual é o tamanho do arquivo para download (em MB)?")
tamanho = float(input())
print("Qual é a velocidade do link de Internet (em Mbps)?")
velocidade = float(input())

# Conversão de unidades
velocidade = velocidade / 8  # Convertendo Mbps para MB/s

# Cálculo do tempo de download
tempo = tamanho / velocidade
tempo = tempo / 60  # Convertendo segundos para minutos

# Impressão do resultado
print("O tempo aproximado de download é de", tempo, "minutos.")
