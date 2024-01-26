"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões,
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova
e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
a - Maior e Menor Acerto;
b- Total de Alunos que utilizaram o sistema;
c - A Média das Notas da Turma

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova 
antes dos alunos usarem o programa.
"""
# Código ChatGpt
def main():
    gabarito = obter_gabarito()
    alunos = []

    while True:
        respostas_aluno = obter_respostas_aluno()
        acertos = calcular_acertos(gabarito, respostas_aluno)
        alunos.append(acertos)

        continuar = input("Outro aluno vai utilizar o sistema? (s/n): ")
        if continuar.lower() != 's':
            break

    exibir_resultados(alunos)

def obter_gabarito():
    gabarito = {}
    print("Digite as respostas do gabarito:")
    for i in range(1, 11):
        questao = f"{i:02d}"
        resposta = input(f"Questão {questao}: ").upper()
        gabarito[questao] = resposta
    return gabarito

def obter_respostas_aluno():
    respostas_aluno = {}
    print("\nDigite as respostas do aluno:")
    for i in range(1, 11):
        questao = f"{i:02d}"
        resposta = input(f"Questão {questao}: ").upper()
        respostas_aluno[questao] = resposta
    return respostas_aluno

def calcular_acertos(gabarito, respostas_aluno):
    acertos = 0
    for questao, resposta in gabarito.items():
        if resposta == respostas_aluno[questao]:
            acertos += 1
    return acertos

def exibir_resultados(alunos):
    if not alunos:
        print("Nenhum aluno utilizou o sistema.")
        return

    total_alunos = len(alunos)
    maior_acerto = max(alunos)
    menor_acerto = min(alunos)
    media_acertos = sum(alunos) / total_alunos

    print("\nResultados:")
    print(f"a - Maior acerto: {maior_acerto}")
    print(f"b - Menor acerto: {menor_acerto}")
    print(f"c - Total de alunos: {total_alunos}")
    print(f"d - Média de acertos: {media_acertos:.2f}")

if __name__ == "__main__":
    main()
