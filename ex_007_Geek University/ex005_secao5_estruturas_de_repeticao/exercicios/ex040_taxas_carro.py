"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. 

A comissão e os impostos são calculados sobre o custo
de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao
consumidor.
_______________________________________________________________________________
|   CUSTO DE FÁBRICA                    | % DO DISTRIBUIDOR  | % DOS IMPOSTOS |
|      até R$12.000,00                  |       5            |     isento     |               
|      entre R$12.000,00 e 25.000,00    |       10           |       15       |
|      acima de R$25.000,00             |       15           |       20       |
------------------------------------------------------------------------------=

"""
custo_fabrica = float(input('Digite o custo da fábrica: '))
if custo_fabrica <= 12_000:
    distribuidor = custo_fabrica * 0.05
    total_consumidor = custo_fabrica + distribuidor
    print(f'O custo do consumidor será de {total_consumidor:.2f} R$')
elif custo_fabrica > 12_000 and custo_fabrica <= 25_000:
    distribuidor = custo_fabrica * 0.10
    imposto = custo_fabrica * 0.15
    total_consumidor = custo_fabrica + distribuidor + imposto
    print(f'O custo do consumidor será de {total_consumidor:.2f} R$')
elif custo_fabrica > 25_000:
    distribuidor = custo_fabrica * 0.15
    imposto = custo_fabrica * 0.20
    total_consumidor = custo_fabrica + distribuidor + imposto
    print(f'O custo do consumidor será de {total_consumidor:.2f} R$')
