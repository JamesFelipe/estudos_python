# Código feito utilizando a Inteligência artifical Bard(Modificado)
def show_magicians(lista):
    for l in lista:
        print(l)

def make_great(lista):
    for i in range(len(lista)):
        lista[i] = "O Grande " + lista[i]
    return lista

nomes = ['Houdini', 'Howard', 'Pai indo comprar cigarro']
print(make_great(nomes))
show_magicians(nomes)
