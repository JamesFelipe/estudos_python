while True:
    ingredientes = input('Digite o ingrendiente para pizza[quit para encerrar]: ').strip()
    if ingredientes == 'quit':
        break
    print(f'{ingredientes} adicionado a pizza')
