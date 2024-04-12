def make_album(nome_artista, titulo_album, faixas_album=0):
    album = {'nome': nome_artista, 'titulo': titulo_album,  'faixas': faixas_album}
    return album

while True:
    nome = input('Digite o nome do artista: ')
    titulo = input('Digite o nome do album: ')
    faixas = int(input('Digite quantos faixas o album tem: '))
    saida = input('Você quer continuar?[Sim/Nao]: ').strip().lower()[0]
    print(make_album(nome, titulo, faixas))
    if saida == 'n':
        break
