custo_fab = float(input('Digite o custo da fábrica: '))

if custo_fab <= 12_000:
    pocen_distribuidor = custo_fab + (custo_fab * 5/100)
    print(f'O custo ao consumidor será de R${pocen_distribuidor} isento de imposto')
elif custo_fab > 12_000 and custo_fab <= 25_000:
    pocen_distribuidor = custo_fab + (custo_fab * 10 / 100)
    pocen_impostos = pocen_distribuidor * 0.15
    print(f'O custo ao consumidor será de R${pocen_impostos} já com 15% de imposto')
elif custo_fab > 25_000:
    pocen_distribuidor = custo_fab + (custo_fab * 15 / 100)
    pocen_impostos = pocen_distribuidor * 0.2
    print(f'O Custo ao consumidor será de R${pocen_impostos} já com 20% de imposto')
