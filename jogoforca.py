from time import sleep
from dados import *
from random import randint
chances = 4
chutes = []
ganhou = False
try:
    while True:   #Continuar ou sair
        sortear = randint(0, len(palavra) - 1)

        while True:  # Jogo
#Jogo
            for letra in palavra[sortear]:
                if letra in chutes:
                    print(f'{letra}', end='')
                else:
                    print(f'_', end='')
#Validação do chute
            while True:
                player = input(str(f'\nSua palavra contem {len(palavra[sortear])} letras, qual é o seu palpite?')).upper().strip()
                if player in '':
                    print(f'Não foi passado nenhuma letra, tente novamente')
                elif player.isnumeric():
                    print(f'"{player}" não é uma letra, tente novamente')
                elif len(player) == len(palavra[sortear]):
                    break
                elif len(player) > 1:
                    print(f'Digite apenas uma letra ou a palavra inteira')
                else:
                    break
            print(f'Verificando', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.')

            if player in palavra[sortear]:
                chutes.append(player)
                for letra in chutes:
                    if letra == palavra[sortear]:
                        ganhou = True
                if ganhou == True:
                    print(f'Parabéns você ganhou, a palavra é {palavra[sortear]}')
                    break
                print(f'Parabéns a palavra contém a letra {player}')
            else:
                chances -= 1
                if chances == 0:
                    print(f'Infelizmente a palavra não possui a letra "{player}"')
                elif len(player) == len(palavra[sortear]):
                    print(f'Infelizmente a Palavra não é {player}, você ainda possui {chances} chances')
                else:
                    print(f'Infelizmente a palavra não possui a letra "{player}", você ainda possui {chances} chances')


#Validação do jogo
            ganhou = True
            for letra in palavra[sortear]:
                if letra not in chutes:
                    ganhou = False
            if ganhou == True:
                print(f'Parabéns você ganhou, a palavra é {palavra[sortear]}')
                break
            elif chances == 0:
                print(f'Oh não! Suas chances se esgotaram, Boa Sorte da proxima vez.')
                break
#Continuar ou sair
        while True:
            resposta = input(str(f'Deseja jogar novamente?[S/N]')).upper().strip()
            if resposta not in 'SN' or resposta in '':
                print(f'Opção inválida')
            else:
                break
        if resposta in 'N':
            print(f'Encerrando...')
            break
        else:
            chutes.clear()
            chances = 4
            ganhou = False
except KeyboardInterrupt:
    print(f'\nO usuário encerrou o jogo')