"""
As tarifas de certo parque de estacionamento são as seguintes:

 1º e2º hora - R$ 1,00 cada
 3º e 4º hora - R$ 1,40 cada
 5º hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo,
quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que pagaria
se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e partida
deste são apresentados na forma de pares de inteiros, representando horas e minutos.
Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida, escreva na tela
o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior
à da partida, isso não é uma situação de erro, antes significará que a partida ocorreu no
dia seguinte ao da chegada.
"""
# Código ChatGpt
import math

def calcular_tarifa(chegada_h, chegada_m, partida_h, partida_m):
    # Converter horários para minutos desde o início do dia
    minutos_chegada = chegada_h * 60 + chegada_m
    minutos_partida = partida_h * 60 + partida_m
    
    # Calcular diferença em minutos
    if minutos_partida < minutos_chegada:
        minutos_partida += 24 * 60  # Adicionar 24 horas se partida é no dia seguinte
    
    minutos_total = minutos_partida - minutos_chegada
    
    # Converter para horas inteiras, arredondando para cima
    horas_total = math.ceil(minutos_total / 60)
    
    # Calcular o custo total de estacionamento
    if horas_total <= 2:
        custo = horas_total * 1.00
    elif horas_total <= 4:
        custo = 2 * 1.00 + (horas_total - 2) * 1.40
    else:
        custo = 2 * 1.00 + 2 * 1.40 + (horas_total - 4) * 2.00
    
    return custo

# Exemplos de uso:
chegada_h = int(input("Hora de chegada: "))
chegada_m = int(input("Minuto de chegada: "))
partida_h = int(input("Hora de partida: "))
partida_m = int(input("Minuto de partida: "))

custo = calcular_tarifa(chegada_h, chegada_m, partida_h, partida_m)
print(f"Preço cobrado pelo estacionamento: R$ {custo:.2f}")
