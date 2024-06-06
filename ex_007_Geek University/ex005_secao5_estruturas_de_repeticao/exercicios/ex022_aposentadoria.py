"""
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se
aposentar. As condições para aposentadoria são

    Ter pelo menos 65 anos,
    Ou tor trabalhado pelo menos 30 anos,
    Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = int(input('Digite sua idade: '))
tempo_servico = int(input('Digite quanto tempo você tem de seriço: '))
if idade >= 65 or tempo_servico >= 30:
    print('Você pode se aposentar')
elif tempo_servico >= 25 and idade >= 60:
    print('Você pode se aposentar')
else:
    print('Você não pode se aposentar')
