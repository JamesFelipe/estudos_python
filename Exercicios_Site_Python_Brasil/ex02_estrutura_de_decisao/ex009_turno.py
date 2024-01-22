"""
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
turno = input('Digite em que turno você trabalha(M-matutino ou V-Vespertino ou N- Noturno): ').strip().lower()[0]

match turno:
    case 'm':
        print('Bom dia')
    case 'v': 
        print('Boa Tarde')
    case 'n':
        print('Boa noite')
    case _:
        print('Valor inválido')
