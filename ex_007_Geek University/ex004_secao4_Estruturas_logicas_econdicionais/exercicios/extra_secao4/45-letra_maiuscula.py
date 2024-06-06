 # grando um loop infinito, até a pessoa digitar uma letra, maiúsucla ou mínuscula
while True:
    letra = input('Digite uma letra: ').strip().upper()
    
    #tupla com o alfabeto já que não vou mudar os valores(valores fixos)
    alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    # se a letra não estiver na tupla, vai mandar a pessoa escrever outro valor
    if letra not in alfabeto:
        print(f'Digite uma letra do alfabeto')
    else:
        print(f'Letra em maiúsculo? {letra.upper()}')
        
        # esse valor só será exibido se for uma letra
        print(f'Letra em minúsculo: {letra.lower()}') 
        break
