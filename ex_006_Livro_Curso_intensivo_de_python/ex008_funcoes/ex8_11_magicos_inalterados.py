# Código feito utilizando a Inteligência artifical Bard
def show_magicians(lista):
    for l in lista:
        print(l)

def make_great(lista):
    new_lista = []
    for i in range(len(lista)):
        new_lista.append("O Grande " + lista[i])
    return new_lista

lista = ["David Copperfield", "David Blaine", "Penn & Teller"]

show_magicians(lista)
nova_lista = make_great(lista)
print(nova_lista)
