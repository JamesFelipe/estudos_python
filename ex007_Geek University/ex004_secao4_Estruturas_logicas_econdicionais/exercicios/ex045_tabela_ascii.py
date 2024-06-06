"""
Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCI para tesolver o problema.
"""
# O ord ler os números e o chr converte para os valores ascii
# somando ao 32 que faz pular os caraceteres e vai direto para o alfabeto minúsculo
letra_maiuscula = ord(input('Digite uma letra Maiúscula: ')) + 32
print(chr(letra_maiuscula))
