def make_album(nome_artista, titulo_album, faixas_album=0):
    album = {'nome': nome_artista, 'titulo': titulo_album,  'faixas': faixas_album}
    return album


print(make_album('Galinha Pintadinha', 'Galinha Pintadinha Vol1'))
print(make_album('Galinha Pintadinha', 'Galinha Pintadinha Vol2', 12))
