"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    
    O total a pagar com desconto de 10%;
    o valor de cada parcela, no parcelamento de 3x sem juros;
    a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    a comissão do vendedar, no caso da venda ser parcelada (5% sobre a valor total)
"""
valor_total = float(input('Digite o valor total da venda: '))
desconto_10 = valor_total - (valor_total * 10/100)
print(f'Com desconto de 10% o valor total é: {desconto_10:.2f} R$')
parcelas = desconto_10 / 3
print(f'Com desconto de 10% e parcelados em 3X você iria pagar {parcelas:.2f} R$ na parcela')
comisao_vendedor = desconto_10 * 0.05
print(f'A comisão do vendedor será de {comisao_vendedor:.2f} R$')
comisao_parcelas = parcelas * 0.05
print(f'A comisão do vendedor nas parcelas é: {comisao_parcelas:.2f} R$')
