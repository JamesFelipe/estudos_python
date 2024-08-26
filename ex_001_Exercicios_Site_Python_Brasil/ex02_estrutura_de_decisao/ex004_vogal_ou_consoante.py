"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input('Digite uma letra: ')
if letra in 'a e i o u':
    print('Vogal')
elif letra in 'b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, y, w, z':
    print('Consoante')
else:
    print('Nem consoante, nem vogal')
    