activate = True
while activate:
    activate = input('Digite o ingrendiente para pizza[quit para encerrar]: ').strip()
    if activate == 'quit':
        break
    print(f'{activate} adicionado a pizza')
