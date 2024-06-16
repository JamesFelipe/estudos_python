"""
Escreva um programa completo que permita a qualquer aluno introduzir, 
pelo teclado, uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) 
e que mostre na tela, como resultado, 
a correspondente média aritmética. 
O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, 
o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.
"""
# Código ChatGpt
# Inicializa uma lista vazia para armazenar as notas
notas = []

# Loop infinito para receber as notas até que uma nota inválida seja fornecida
while True:
    nota = float(input("Digite uma nota (entre 10 e 20): "))
    
    # Verifica se a nota está no intervalo válido
    if 10 <= nota <= 20:
        # Adiciona a nota à lista de notas
        notas.append(nota)
    else:
        # Se a nota não estiver no intervalo válido, encerra o loop
        print("Nota inválida. Encerrando o programa.")
        break

# Verifica se foram fornecidas notas
if len(notas) > 0:
    # Calcula a média aritmética das notas
    media = sum(notas) / len(notas)
    
    # Imprime a média aritmética
    print("A média aritmética das notas é:", media)
else:
    # Se nenhuma nota válida foi fornecida, imprime uma mensagem
    print("Nenhuma nota válida foi fornecida.")
