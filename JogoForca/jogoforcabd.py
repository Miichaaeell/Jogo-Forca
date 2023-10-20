from dados import *
from interface import *
from Funções import *
from time import sleep
chances = 4
chutes = []
ganhou = False
try:
    while True:  # Menu
        while True:
            resposta = menu()
            if resposta == 1:
                newjogador = newcadastro().upper()
                print(f'{newjogador} cadastrado com sucesso')
            elif resposta == 3:
                verpontos()
            elif resposta == 4:
                deletar()
            elif resposta == 2:
                jogador = mostrarjogadores()
                vitoria = vitorias(jogador)
                partida = int(partidas(jogador))
                break
            elif resposta == 0:
                break
        if resposta == 0:
            break
        palavras = aleatorio()
        palavra = palavras['palavra']
        dica = palavras['dica']
        while True:  # Jogo
            linha(f'Sua palavra contem {len(palavra)} letras e a dica é {dica.upper()}')
            mostrarpalvra(palavra,chutes)
            # Validação do chute
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
                    print(f'\033[1:32mParabéns você ganhou, a palavra é {palavra}\033[m')
                    partida += 1
                    vitoria += 1
                    ponto = vitoria / partida
                    editarpartida(partida, jogador)
                    editarvitorias(vitoria, jogador)
                    editarpontos(ponto, jogador)
                    chutes.clear()
                    chances = 4
                    ganhou = False
                    palavra = aleatorio()
                    resposta = continuar()
                    if resposta in 'nN':
                        break
                else:
                    chutes.append(chute)
                    print(f'\033[1:32mParabéns a palavra contém a letra {chute}\033[m')
            else:
                chances -= 1
                if chances == 0:
                    print(f'\033[31mInfelizmente a palavra não possui a letra "{chute}"\033[m')
                elif len(chute) == len(palavra):
                    print(f'\033[31mInfelizmente a Palavra não é {chute}, você ainda possui {chances} chances\033[m')
                else:
                    print(f'\033[31mInfelizmente a palavra não possui a letra "{chute}", você ainda possui {chances} chances\033[m')
            # Validação do jogo
            ganhou = True
            for letra in palavra:
                if letra not in chutes:
                    ganhou = False
            if ganhou == True:
                print(f'\033[1:32mParabéns você ganhou, a palavra é {palavra}\033[m')
                partida += 1
                vitoria += 1
                ponto = vitoria / partida
                editarpartida(partida, jogador)
                editarvitorias(vitoria, jogador)
                editarpontos(ponto, jogador)
                chutes.clear()
                chances = 4
                ganhou = False
                palavra = aleatorio()
                resposta = continuar()
                if resposta in 'nN':
                    break
            elif chances == 0:
                print(f'\033[31mOh não! Suas chances se esgotaram, Boa Sorte da proxima vez.\033[m')
                partida += 1
                ponto = vitoria / partida
                editarpartida(partida, jogador)
                editarpontos(ponto, jogador)
                chutes.clear()
                chances = 4
                ganhou = False
                palavra = aleatorio()
                resposta = continuar()
                if resposta in 'nN':
                    break
except KeyboardInterrupt:
    print(f'\n\033[31mO usuário encerrou o jogo\033[m')