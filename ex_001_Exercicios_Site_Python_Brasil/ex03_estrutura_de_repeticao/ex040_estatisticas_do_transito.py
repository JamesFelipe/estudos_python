"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade; X
Número de veículos de passeio (em 1999); X
Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber: X
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
# Código ChatGpt
# Dados fornecidos
codigos_cidades = [1, 2, 3, 4, 5]
veiculos_passeio = [1000, 1500, 1800, 2000, 2200]
acidentes_transito = [10, 5, 8, 15, 12]

# Calculando o índice de acidentes de trânsito para cada cidade
indices_acidentes = [acidentes / veiculos for acidentes, veiculos in zip(acidentes_transito, veiculos_passeio)]

# Encontrando a cidade com o maior e menor índice de acidentes
cidade_maior_indice = codigos_cidades[indices_acidentes.index(max(indices_acidentes))]
cidade_menor_indice = codigos_cidades[indices_acidentes.index(min(indices_acidentes))]

# Calculando a média de veículos nas cinco cidades juntas
media_veiculos = sum(veiculos_passeio) / len(veiculos_passeio)

# Filtrando as cidades com menos de 2.000 veículos de passeio
cidades_menos_2000 = [cod for cod, veiculos in zip(codigos_cidades, veiculos_passeio) if veiculos < 2000]

# Calculando a média de acidentes de trânsito nas cidades com menos de 2.000 veículos
media_acidentes_menos_2000 = sum(acidentes_transito[codigos_cidades.index(cod)] for cod in cidades_menos_2000) / len(cidades_menos_2000) if len(cidades_menos_2000) > 0 else 0

# Exibindo os resultados
print(f"Maior índice de acidentes: Cidade {cidade_maior_indice} - {max(indices_acidentes)}")
print(f"Menor índice de acidentes: Cidade {cidade_menor_indice} - {min(indices_acidentes)}")
print(f"Média de veículos nas cinco cidades: {media_veiculos}")
print(f"Média de acidentes nas cidades com menos de 2.000 veículos: {media_acidentes_menos_2000}")
