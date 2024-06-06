a: int = int(input('Digite um valor: '))
b: int = int(input('Digite o mesmo/outro valor: '))
c: int = int(input('Digite o mesmo/outro valor: '))

if a + b > c and a + c > b and b + c > a:
    print('Os três lados formam um triângulo', end=' -> ')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os lados não formam um triângulo!')
