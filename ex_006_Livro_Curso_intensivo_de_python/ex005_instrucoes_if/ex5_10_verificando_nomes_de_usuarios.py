current_users = ['gabi', 'e', 'i', 'o', 'u']
new_users = ['gabi', 'arturo', 'jesus', 'jessica', 'penny']

for new in new_users:
    if new in current_users:
        print(f'{new.title()}, já em uso, escolha outro nome de usuário')
    else:
        print(f'{new.title()}, Disponível para uso')
