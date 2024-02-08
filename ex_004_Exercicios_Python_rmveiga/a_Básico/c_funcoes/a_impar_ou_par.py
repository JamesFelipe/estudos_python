def impar_par(numero):
    if numero == 0:
        return "O número Zero é PAR"
    else:
        if numero % 2 == 0:
            return f"O número {numero} é PAR"
        else:
            return f'O número {numero} é ÍMPAR'
    

print(impar_par(0))
print(impar_par(5))
print(impar_par(50))
