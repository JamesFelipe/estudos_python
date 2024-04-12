def build_profile(first, last, **user_info):
    """Constroí um dicionário contendo tudo que sabemos sobre um usuário"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='phisycs')

print(user_profile)
my_profile = build_profile('James', 'Felipe',
                           location='São Miguel Do Guamá',
                           field='Programação e html',
                           game='Big Farm',
                           language='Português, um pouco de inglês e espanhol',
                           sexo='Masculino')
print(my_profile)