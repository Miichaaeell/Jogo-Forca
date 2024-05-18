from dados import *
from interface import *
from Funções import *
try:
    while True:  # Menu
        jogador = inicar()
        if jogador == 0:
            break
        vitoria = vitorias(jogador)
        partida = int(partidas(jogador))
        resposta = 'S'
        while resposta not in 'Nn':  # CONTINUAR JOGANDO
            ganhou = False
            jogo = True
            chutes = []
            chances = 5
            palavras = aleatorio()
            palavra = palavras['palavra']
            dica = palavras['dica']
            while jogo == True: #JOGO
                linha(f'Sua palavra contem {len(palavra)} letras e a dica é {dica.upper()}') if chances <= 3 \
                    else linha(f'Sua palavra contem {len(palavra)} letras')
                mostrarpalvra(palavra,chutes)
                chute = validarchute(palavra)
                timercheck()
                if chute in palavra:
                    if chute == palavra:
                        ganhou = True
                    if ganhou == True:
                        print(f'\033[1:32mParabéns você ganhou, a palavra é {palavra}\033[m')
                        partida += 1
                        vitoria += 1
                        ponto = vitoria / partida
                        updateplayer(partida, vitoria,ponto, jogador)
                        jogo = False
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
                    updateplayer(partida, vitoria, ponto, jogador)
                    jogo = False
                elif chances == 0:
                    print(f'\033[31mOh não! Suas chances se esgotaram, Boa Sorte da proxima vez.\033[m')
                    partida += 1
                    ponto = vitoria / partida
                    updateplayer(partida, vitoria, ponto, jogador)
                    jogo = False
            resposta = continuar()
except KeyboardInterrupt:
    print(f'\n\033[31mO usuário encerrou o jogo\033[m')