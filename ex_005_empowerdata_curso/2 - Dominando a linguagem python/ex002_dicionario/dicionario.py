paises = {
'sigla': ['BRA', 'EUA', 'JPN', 'CHN'],
'nome': ['Brasil', 'Estados Unidos', 'Japão', 'China'],
'capital': ['Brasilia', 'Washigton', 'Tokyo', 'Pequin']
}


def escolha_pais(entrada):
    match entrada.upper():
        case 'BRA':
            return f"{paises['sigla'][0]}, {paises['nome'][0]}, {paises['capital'][0]}"
        case 'EUA':
            return f"{paises['sigla'][1]}, {paises['nome'][1]}, {paises['capital'][1]}"
        case 'JPN':
            return f"{paises['sigla'][2]}, {paises['nome'][2]}, {paises['capital'][2]}"
        case 'CHN':
            return f"{paises['sigla'][3]}, {paises['nome'][3]}, {paises['capital'][3]}"
        case _:
            return 'valor inválido'

print(escolha_pais('eua'))
