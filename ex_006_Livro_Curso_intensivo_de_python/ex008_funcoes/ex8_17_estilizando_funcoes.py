# 1


def display_message():
    """Está função serve para exibir uma mensagme"""
    print('Estou aprendendo funções')


display_message()


# 2


def favorite_book(title):
    """
    Essa função recebe nomes de livros favoritos do usuário 
    Retorna os nomes de livros capitalizados
    """
    print(f'Um dos meus livros favoritos é {title.title()}')

favorite_book('O pequeno príncipe')
favorite_book('O alienista')


# 3

def make_shirt(size, text):
    """
    Essa função recebe os argumentos:
    size=tamanho
    text=texto

    return: retorna uma frase com o tamanho e o texto capitalizado
    """
    print(f'A camisa de tamnaho {size.upper()}, está estampado {text.title()}')

make_shirt('p', 'Python is language and snake')
make_shirt(text='freendom virtual', size='GG')
