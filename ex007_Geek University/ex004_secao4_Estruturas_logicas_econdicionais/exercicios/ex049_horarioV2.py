"""
Faça um programa para leia o horário (hora, minuto e segundo) de inicío e a duração, em
segundos, do uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto & segundo) do termino da mesma.
"""

# inicio da experiência
hora_inicio = int(input('Digite a hora do inicio da experiência: ')) * 3600
minuto_inicio = int(input('Digite os minutos do início da experiÊncia: ')) * 60
segundos_inicio = int(input('Digite os segundos do início da experiência: '))

# Durante a exeriência
hora_durante = int(input('Digite a hora de durção da experiência: ')) * 3600
minuto_durante = int(input('Digite os minutos de duração da experiência: ')) * 60
segundos_durante = int(input('Digite os segundos de duração da experiência: '))
print(f'A experiência irá terminar: \
{(hora_inicio + hora_durante) / 3600, (minuto_inicio + minuto_durante) / 60, segundos_inicio + segundos_durante}')
