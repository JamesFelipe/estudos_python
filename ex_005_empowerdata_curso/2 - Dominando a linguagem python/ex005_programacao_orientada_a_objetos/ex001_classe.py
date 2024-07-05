# para criar a classe utilizo o comando class
class Carro:
    pass


# criando um objeto(e instanciando)
ferrari = Carro()
fusca_azul = Carro
# Onde é a ferrari é o objeto

# mostrando que a ferrari é do tipo carro
print(type(ferrari))

# Atributos(Propriedades)
# Abaixo isso não é uma boa prática de programação
ferrari.cor = "Vermelha"

# Acessando o valor
print(ferrari.cor)

fusca_azul.cor = "Azul claro"
print(fusca_azul.cor)
