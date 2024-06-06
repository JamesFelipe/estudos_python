sal_atual = float(input('Digite seu salário atual: '))
temp_sev = float(input('Digite o seu tempo de serviço na empresa(anos): '))

if sal_atual <= 500 and temp_sev < 1:
    aumento = sal_atual + (sal_atual * 0.25)
    print(f'25% de aumento você irá receber: R${aumento:.2f}')

elif sal_atual <= 1000 and temp_sev > 1 and temp_sev <= 3:
    aumento = sal_atual + (sal_atual + 0.2)
    print(f'20% de aumento você irá receber: R${aumento:.2f} + Bônus 100R$')
    print(f'Total: {aumento+100:.2f}')

elif sal_atual <= 1500 and temp_sev >= 4 and temp_sev <= 6:
    aumento = sal_atual + (sal_atual + 0.15)
    print(f'15% de aumento você irá receber: R${aumento:.2f} + Bônus 200$')
    print(f'Total: {aumento+200:.2f}')

elif sal_atual <= 2000 and temp_sev >= 7 and temp_sev <= 10:
    aumento = sal_atual + (sal_atual + 0.1)
    print(f'10% de aumento você irá receber: R${aumento:.2f} + Bônus 300$')
    print(f'Total: {aumento+300:.2f}')

elif sal_atual > 2000 and temp_sev > 10:
    print('Você irá receber um bônus de 500R$')
