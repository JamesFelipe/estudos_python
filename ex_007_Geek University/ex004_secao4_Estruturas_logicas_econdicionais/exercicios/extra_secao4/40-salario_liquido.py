# quanto a pessoa recebe por dia trabalhado
dia = 30 
dia_trabalho = int(input('Quantos dias inteiros você trabalhou? '))

# quanto a empresa vai pagar dependendo da quantidade de dias trabalhados
pagar = dia_trabalho * dia

 # valor do imposto sobre quanto o funcionário irá receber
imposto = pagar - (pagar * 8/100)

# apenas o resultado do imposto
saldo = imposto 

print(f'Já com 8% de imposto você irá receber: {saldo:.2f}')
