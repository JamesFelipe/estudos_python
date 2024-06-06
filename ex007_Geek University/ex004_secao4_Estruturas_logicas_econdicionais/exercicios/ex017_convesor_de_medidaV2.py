"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = c / 2.54 , sendo C' o comprimento em centímetros e P o
comprimento em polegadas.
"""
centimetros = float(input('Digite um valor em centimetros: '))
print(f'{centimetros} em polegadas é: {centimetros / 2.54:.2f}')
