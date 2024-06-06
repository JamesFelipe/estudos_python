print('Digite o horário de início da experiência biológica')
hora_incio = int(input('Digite a hora: ')) 
min_inicio = int(input('Digite o(s) minutos: ')) 
segundos_inicio = int(input('Digite o(s) segundos: '))

duracao = int(input('Duração dos eventos (segundos): '))

segundos_final = (segundos_inicio + duracao) % 60
minutos_final = (min_inicio + (segundos_inicio + duracao) // 60) % 60
horas_final = (hora_incio + (min_inicio + (segundos_inicio + duracao)//60)//60) % 24

print(f'O experimento terminará as {horas_final}: {minutos_final}: {segundos_final}')
