"""
Escreva um programa que leia o número de habitantes de uma determinada cidade,
o valor do kwh, e para cada habitante entre com os seguintes dados: 
consumo do mês e o código do consumidor 
(1-Residencial, 2-Comercial, 3-Industrial). 
No final imprima o maior, o menor e a média do consumo dos habitantes; 
e por fim o total do consumo de cada categoria de consumidor.

"""
# Código ChatGPt
# Solicitar o número de habitantes e o valor do kWh
num_habitantes = int(input("Informe o número de habitantes da cidade: "))
valor_kwh = float(input("Informe o valor do kWh: "))

# Inicializar variáveis para armazenar os dados de consumo
consumos = []
total_consumo_residencial = 0
total_consumo_comercial = 0
total_consumo_industrial = 0

# Coletar os dados de consumo para cada habitante
for i in range(num_habitantes):
    consumo = float(input(f"Informe o consumo do mês para o habitante {i+1} (em kWh): "))
    codigo_consumidor = int(input(f"Informe o código do consumidor (1-Residencial, 2-Comercial, 3-Industrial) para o habitante {i+1}: "))
    
    consumos.append(consumo)
    
    if codigo_consumidor == 1:
        total_consumo_residencial += consumo
    elif codigo_consumidor == 2:
        total_consumo_comercial += consumo
    elif codigo_consumidor == 3:
        total_consumo_industrial += consumo

# Calcular o maior, o menor e a média do consumo dos habitantes
maior_consumo = max(consumos)
menor_consumo = min(consumos)
media_consumo = sum(consumos) / num_habitantes

# Exibir os resultados
print(f"\nMaior consumo: {maior_consumo:.2f} kWh")
print(f"Menor consumo: {menor_consumo:.2f} kWh")
print(f"Média de consumo: {media_consumo:.2f} kWh")

print(f"\nTotal de consumo por categoria:")
print(f"Residencial: {total_consumo_residencial:.2f} kWh")
print(f"Comercial: {total_consumo_comercial:.2f} kWh")
print(f"Industrial: {total_consumo_industrial:.2f} kWh")
