glossario = {
    'int': 'define valores  do tipo inteiros',
    'float': 'define valores do tipo ponto flutuante',
    'bool': 'defive valores booleanos',
    'boleano': 'resultado de alguma condição, com resultado True ou False',
    'if': 'testa as condições'
}

for chave, valor in glossario.items():
    print(chave + ":" + valor)
print()

glossario['list'] = 'lista do python'
glossario['dict'] = 'dicionário do python'
glossario['set'] = 'conjunto do python'
glossario['for'] = 'laço utilizado quando sabemos quantas vezes iremos repetir um valor'
glossario['else'] = 'exibe os valores caso a condição do if seja falsa'

for chave, valor in glossario.items():
    print(chave, ':', valor)
