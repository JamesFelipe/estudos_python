"""
Faça um programa que leia dois números a e b (positivos menores que 10000) e:
    • Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo menos significativo;
    • Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construídos anteriormente.
Dica: some as posições correspondentes. Se a soma ultrapassar 10, subtraia 10 do resultado e some 1 à próxima posição.

"""
# Código chatgpt
def somar_numeros(a, b):
    # Função para realizar a soma usando vetores
    def soma_vetores(vetor_a, vetor_b):
        resultado = []
        carry = 0  # Variável para armazenar o "vai um" da soma

        for i in range(max(len(vetor_a), len(vetor_b))):
            # Obtém os dígitos dos vetores, considerando 0 se não houver dígito
            digito_a = vetor_a[i] if i < len(vetor_a) else 0
            digito_b = vetor_b[i] if i < len(vetor_b) else 0

            # Realiza a soma e considera o "vai um" da soma anterior (carry)
            soma = digito_a + digito_b + carry

            # Atualiza o carry para a próxima iteração
            carry = soma // 10

            # Adiciona o dígito ao resultado
            resultado.append(soma % 10)

        # Se houver carry após a última iteração, adiciona ao resultado
        if carry:
            resultado.append(carry)

        return resultado

    # Converte os números para listas de dígitos
    vetor_a = [int(digito) for digito in str(a)][::-1]  # Inverte a ordem dos dígitos
    vetor_b = [int(digito) for digito in str(b)][::-1]  # Inverte a ordem dos dígitos

    # Realiza a soma dos vetores
    resultado = soma_vetores(vetor_a, vetor_b)

    # Imprime o resultado
    print(f'A soma de {a} e {b} é: {" ".join(map(str, resultado[::-1]))}')


# Solicita os números ao usuário
numero_a = int(input('Digite o primeiro número (positivo e menor que 10000): '))
numero_b = int(input('Digite o segundo número (positivo e menor que 10000): '))

# Verifica se os números atendem às condições
if 0 < numero_a < 10000 and 0 < numero_b < 10000:
    somar_numeros(numero_a, numero_b)
else:
    print('Por favor, insira números positivos menores que 10000.')
