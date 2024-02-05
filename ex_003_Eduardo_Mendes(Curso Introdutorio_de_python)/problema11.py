# Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string print o seu nome entre as letras
# Obs.: A vogal será subistítuida pelo menu nome

# string bananas
# b
# eduardo
# n
# n
# eduardo
# n
palavra = 'abracadabra'
for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('James')
    else:
        print(letra)