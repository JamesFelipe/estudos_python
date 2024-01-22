"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 

O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. 

A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""
# Código bard
def main():
    # Inicializa as variáveis
    produtos = []
    precos = []
    total = 0
    dinheiro = 0

    # Loop para ler os produtos e preços
    while True:
        # Lê o produto
        produto = input("Insira o produto (0 para finalizar): ")

        # Se o produto for 0, finaliza o loop
        if produto == "0":
            break

        # Lê o preço
        preco = float(input("Insira o preço do produto: "))

        # Adiciona o produto e o preço à lista
        produtos.append(produto)
        precos.append(preco)

    # Exibe os produtos e preços
    print("Produtos:")
    for produto, preco in zip(produtos, precos):
        print(f"{produto}: R$ {preco}")

    # Exibe o total da compra
    print("Total: R$", total)

    # Lê o valor pago pelo cliente
    dinheiro = float(input("Insira o valor pago pelo cliente: "))

    # Calcula o troco
    troco = dinheiro - total

    # Exibe o valor do troco
    print("Troco: R$", troco)

if __name__ == "__main__":
    main()
