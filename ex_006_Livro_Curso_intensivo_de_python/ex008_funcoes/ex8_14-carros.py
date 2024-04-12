def carros(nome_fabricante, modelo_carro, **kwargs):
    carro = {}
    carro['fabricante'] = nome_fabricante
    carro['modelo'] = modelo_carro
    for chave, valor in kwargs.items():
        carro[chave] = valor
    return carro


car = carros('subaru', 'outbank', color='blue', tow_package=True)
print(car)