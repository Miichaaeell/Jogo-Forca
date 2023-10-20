from time import sleep
from interface import *
from Funções import *
chances = 4
chutes = []
ganhou = False
jogadores = []
try:
    while True:   #Menu
        opcao = menu()
        if opcao == 2:
            while True:
                ranking(jogadores)
                opcao = menu()
                if opcao != 2:
                    break
        if opcao == 0:
            jogadores.append(cadastro())
            JOGADOR = int(len(jogadores) - 1)
        elif opcao == 1:
            JOGADOR = listarjogadores(jogadores)
        elif opcao == 3:
            linha(f'Saindo do jogo...')
            break
        palavra = aleatorio()
        while True:  # Jogo
            linha(f'Sua palavra contem {len(palavra)} letras')
            mostrarpalvra(palavra, chutes)
#Validação do chute
            chute = validarchute(palavra)
            print(f'Verificando', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.')
            if chute in palavra:
                if chute == palavra:
                    ganhou = True
                if ganhou == True:
                    print(f'Parabéns você ganhou, a palavra é {palavra}')
                    jogadores[int(JOGADOR)]['Partida'] += 1
                    jogadores[int(JOGADOR)]['Vitorias'] += 1
                    jogadores[int(JOGADOR)]['Pontos'] = jogadores[int(JOGADOR)]['Vitorias'] / jogadores[int(JOGADOR)][
                        'Partida']
                    chutes.clear()
                    chances = 4
                    ganhou = False
                    palavra = aleatorio()
                    resposta = continuar()
                    if resposta in 'nN':
                        break

                else:
                    chutes.append(chute)
                    print(f'Parabéns a palavra contém a letra {chute}')
            else:
                chances -= 1
                if chances == 0:
                    print(f'Infelizmente a palavra não possui a letra "{chute}"')
                elif len(chute) == len(palavra):
                    print(f'Infelizmente a Palavra não é {chute}, você ainda possui {chances} chances')
                else:
                    print(f'Infelizmente a palavra não possui a letra "{chute}", você ainda possui {chances} chances')
#Validação do jogo
            ganhou = True
            for letra in palavra:
                if letra not in chutes:
                    ganhou = False
            if ganhou == True:
                print(f'Parabéns você ganhou, a palavra é {palavra}')
                jogadores[int(JOGADOR)]['Partida'] += 1
                jogadores[int(JOGADOR)]['Vitorias'] += 1
                jogadores[int(JOGADOR)]['Pontos'] = jogadores[int(JOGADOR)]['Vitorias'] / jogadores[int(JOGADOR)][
                    'Partida']
                chutes.clear()
                chances = 4
                ganhou = False
                palavra = aleatorio()
                resposta = continuar()
                if resposta in 'nN':
                    break
            elif chances == 0:
                print(f'Oh não! Suas chances se esgotaram, Boa Sorte da proxima vez.')
                jogadores[int(JOGADOR)]['Partida'] += 1
                jogadores[int(JOGADOR)]['Pontos'] = jogadores[int(JOGADOR)]['Vitorias'] / jogadores[int(JOGADOR)][
                    'Partida']
                chutes.clear()
                chances = 4
                ganhou = False
                palavra = aleatorio()
                resposta = continuar()
                if resposta in 'nN':
                    break
#Continuar ou sair
except KeyboardInterrupt:
    print(f'\nO usuário encerrou o jogo')