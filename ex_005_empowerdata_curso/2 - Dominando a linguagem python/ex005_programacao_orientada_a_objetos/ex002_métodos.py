class Carro:

    # criando um método
    def hello_car(self):
        print("Hello Car!")


class Carro_inicializado:
    # utilizando o método construtor
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca
        
        # Valor default
        self.dono = "James"

    def hello_car(self):
        print("Hello car!")
        
    def retorna_marca(self):
        return self.marca
        
        
ferrari = Carro()
fusca_azul = Carro()

# Utilizando o método
ferrari.hello_car()
fusca_azul.hello_car()

# Intânciando um novo objeto
kombi = Carro()
kombi.hello_car()
print()

# ---------------------------- Novos veiculos -------------------------------
cybertruck = Carro_inicializado("Cinza", "Tesla")
hb20 = Carro_inicializado("Prateado", "Hyundai")
corolla = Carro_inicializado("Vermelho", "Toyota") 
print(cybertruck.cor)
print(hb20.cor)
print(corolla.cor)

kicks = Carro_inicializado("Azul", "Nissan")
print(kicks.dono)

print(corolla.retorna_marca())
