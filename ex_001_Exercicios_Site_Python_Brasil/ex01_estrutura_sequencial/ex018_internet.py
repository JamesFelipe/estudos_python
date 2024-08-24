"""
Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download 
do arquivo usando este link (em minutos).
"""
mb = int(input('Digite o tamanho do download em MB: '))
velocidade = int(input('Digite a velocidade: '))
formula = mb / (velocidade / 8)
print(f'O tempo de dowload será de {formula:.2f} segundos')
