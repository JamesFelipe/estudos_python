"""
Desenvolva um programa que altere em tempo de execução a palavra 
Java pela palavra Python na frase Exercícios de Java
"""
from time import sleep
frase = "Exercícios de Java"
print(frase)
frase = frase.replace('Java', 'Python')
sleep(1)
print(frase)
