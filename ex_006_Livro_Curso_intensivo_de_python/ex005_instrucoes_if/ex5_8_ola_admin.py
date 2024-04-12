nomes = ['james', 'carla', 'pablo', 'jessíca', 'raissa', 'admin']

for nome in nomes:
    if nome == 'admin':
        print(f'Olá {nome.title()}, gostaria de ver um ralátorio de status?')
    else:
        print(f'Olá, {nome.title()}, obrigado por fazer login novamente') 
   