import os

# Indo trabalhar nos downloads
os.chdir(r"c:\Users\assis\Downloads")

# Confirmando se estou na pasta downloads
print(os.getcwd())

# listando o que tenho na pasta, arquivos e outras pastas
# print(os.listdir())

# Listando os arquivos na pasta Downloads
lista_arquivos = [arquivo for arquivo in os.listdir() if os.path.isfile(arquivo)]

# Criando uma lista de tipos de arquivos (extensões)
lista_tipos = {arquivo.split(".")[-1] for arquivo in lista_arquivos}
print(lista_tipos)

# Criando pastas para cada tipo de arquivo
for tipo in lista_tipos:
    if not os.path.exists(tipo):
        os.mkdir(tipo)

# Movendo os arquivos para as pastas correspondentes
for arquivo in lista_arquivos:
    pasta_destino = arquivo.split(".")[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.rename(de, para)
