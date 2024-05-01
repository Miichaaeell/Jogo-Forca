def linha(msg):
    print('\033[1:35m-'*len(msg))
    print(f'{msg}')
    print('-' * len(msg), '\033[m')

def menu():
    linha(f'{"MENU":^34}')
    print(f'\033[36m1 - Criar Cadastro'
          f'\n2 - Selecionar jogador'
          f'\n3 - Ver pontuação'
          f'\n4 - Deletar jogador'
          f'\n0 - Sair do jogo\033[m')
    while True:
        resposta = str(input('Sua opção: '))
        if resposta.isnumeric() and int(resposta) < 5:
            return int(resposta)
            break
        else:
            print(f'Opção inválida, tente novamente!')



