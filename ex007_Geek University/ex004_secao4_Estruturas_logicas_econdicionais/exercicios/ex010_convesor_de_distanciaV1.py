"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
kmh e M em m/s.
"""
quilometro = int(input('Digite uma velociade em Km/h: '))
metros_por_segundos = quilometro / 3.6
print(f'{quilometro} Km/h em m/s é: {metros_por_segundos:.2f}')
