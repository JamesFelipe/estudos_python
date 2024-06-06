nota = float(input('Digite a nota: '))
n_faltas = int(input('Digite o número de faltas: '))

if nota >= 9 and nota <= 10 and n_faltas <= 20:
    print(f'Nota {nota}\nConceito A')
elif nota >= 9 and nota <= 10 and n_faltas >= 20:
    print(f'Nota {nota}\nConceito B')
elif nota >= 7.5 and nota <= 8.9 and n_faltas <= 20:
    print(f'Nota {nota}\nConceito B')
elif nota >= 7.5 and nota <= 8.9 and n_faltas >= 20:
    print(f'Nota {nota}\nConceito C')
elif nota >= 5 and nota <= 7.4 and n_faltas <= 20:
    print(f'Nota {nota}\nConceito C')
elif nota >= 5 and nota <= 7.4 and n_faltas >= 20:
    print(f'Nota {nota}\nConceito D')
elif nota >= 4 and nota <= 4.9 and n_faltas <= 20:
    print(f'Nota {nota}\nConceito D')
elif nota >= 4 and nota <= 4.9 and n_faltas >= 20:
    print(f'Nota {nota}\nConceito E')
elif nota == 0 or nota <= 3.9 and n_faltas <= 20:
    print(f'Nota {nota}\nConceito E')
elif nota == 0 or nota <= 3.9 and n_faltas >= 20:
    print(f'Nota {nota}\nConceito E')
