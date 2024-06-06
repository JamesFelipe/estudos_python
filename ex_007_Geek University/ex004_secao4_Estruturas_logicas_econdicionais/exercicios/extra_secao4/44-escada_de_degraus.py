while True:
    try:
        altura = int(input('Qual a altura do degrau? '))
        alcance = int(input('Qual degrau você quer alcançar? '))
        total = altura - alcance
    except ValueError:
        print('Aepnas valores inteiros serão aceitos...')
    else:
        print(f'Para alcançar o degrau {alcance} você ainda terá que andar {total} degraus')
        break
