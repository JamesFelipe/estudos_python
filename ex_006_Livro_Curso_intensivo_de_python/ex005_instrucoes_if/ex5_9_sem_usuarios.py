nomes = ['james', 'carla', 'pablo', 'jessíca', 'raissa', 'admin']
nomes.clear()

if len(nomes) == 0:
    print('Precisamos adicionar novos usuários')
else:
    for nome in nomes:
        if nome == 'admin':
            print(f'Olá {nome.title()}, gostaria de ver um ralátorio de status?')
        else:
            print(f'Olá, {nome.title()}, obrigado por fazer login novamente') 