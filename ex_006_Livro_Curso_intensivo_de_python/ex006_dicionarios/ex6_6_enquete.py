pessoas = ['rafaela', 'pachalok', 'phil', 'jen', 'james']
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for pessoa in pessoas:
    if pessoa in favorite_languages:
        print(f'Obrigado por responder a pesquisa, {pessoa}')
    else:
        print(f'Por favor, responda a pesquisa, {pessoa}')
