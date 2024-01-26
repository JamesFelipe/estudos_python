"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 

valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

Quantidade de Parcelas      % de Juros sobre o valor inicial da dívida
1                                   0
3                                   10
6                                   15
9                                   20
12                                  25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
# Código bard
def main():
    # Leitura do valor da dívida
    valor_divida = float(input("Digite o valor da dívida: "))

    # Tabela de juros
    juros = {
        1: 0,
        3: 0.10,
        6: 0.15,
        9: 0.20,
        12: 0.25,
    }

    # Tabela de quantidade de parcelas
    quantidade_parcelas = {
        1: 1,
        3: 3,
        6: 6,
        9: 9,
        12: 12,
    }

    # Cálculo dos juros
    valor_juros = valor_divida * juros[quantidade_parcelas[1]]

    # Cálculo do valor da parcela
    valor_parcela = valor_divida + valor_juros / quantidade_parcelas[1]

    # Impressão da tabela
    print("| Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela |")
    print("|---|---|---|---|")
    print(f"| R$ {valor_divida:.2f} | R$ {valor_juros:.2f} | {quantidade_parcelas[1]} | R$ {valor_parcela:.2f} |")


if __name__ == "__main__":
    main()
