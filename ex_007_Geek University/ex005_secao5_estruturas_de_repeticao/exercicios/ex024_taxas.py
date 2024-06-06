"""
Uma empresa vende o mesmo produto para quatro diferentes estados. 
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS
8%). 

Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto acrescido do imposto do estado
em que ele será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro.
"""
valor = float(input('Digite o valor do produto: '))
estado = input('Digite o estado de envio[MG, SP, RJ, MS]: ').strip().lower()
match estado:
    case 'mg':
        imposto = valor + (valor * 7/100)
        print(f'Você irá pagar {imposto:.2f} R$')
    case 'sp':
        imposto = valor + (valor * 12/100)
        print(f'Você irá pagar {imposto:.2f} R$')        
    case 'rj':
        imposto = valor + (valor * 15/100)
        print(f'Você irá pagar {imposto:.2f} R$')
    case 'ms':
        imposto = valor + (valor * 8/100)
        print(f'Você irá pagar {imposto:.2f} R$')
    case _:
        print('Valor inválido')
