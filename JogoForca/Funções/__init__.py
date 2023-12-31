from JogoForca import interface
def cadastro():
    jogador = {}
    interface.linha(f'{"Novo Cadastro":^30}')
    jogador['Nome'] = str(input('Nome do Jogador(a): '))
    jogador['Partida'] = 0
    jogador['Vitorias'] = 0
    jogador['Pontos'] = 0
    return jogador

def listarjogadores(lista):
    interface.linha(f'{"JOGADORES":^30}')
    print(f'{"INDICE":<6}{"NOME":^15}{"PARTIDAS":>7}')
    for indice, valores in enumerate(lista):
        print(f'{indice:^6}{valores["Nome"]:^15}{valores["Partida"]:^7}')
    JOGADOR = str(input('Qual jogador é você?'))
    return JOGADOR

def ranking(lista):
    interface.linha(f'{"RANKING DOS JOGADORES":^30}')
    print(f'{"Jogador":<10}{"VITÓRIAS":^10}{"PONTOS":>10}')
    crescente = sorted(lista, key=lambda lista : lista['Pontos'], reverse=True)
    for indice, valores in enumerate(crescente):
        print(f'{valores["Nome"]:<10}{valores["Vitorias"]:^10}{valores["Pontos"]:>10.2f}')

def validarchute(palavra):
    while True:
        player = input(str(f'\nQual é o seu palpite?')).upper().strip()
        if player in '':
            print(f'Não foi passado nenhuma letra, tente novamente')
        elif player.isnumeric():
            print(f'"{player}" não é uma letra, tente novamente')
        elif len(player) == len(palavra):
            return player
            break
        elif len(player) > 1:
            print(f'Digite apenas uma letra ou a palavra inteira')
        else:
            return player
            break

def mostrarpalvra(palavra, chutes):
    for letra in palavra:
        if letra in chutes:
            print(f'\033[37m{letra}\033[m', end='')
        else:
            print(f'_', end='')

def continuar():
    while True:
        resposta = input(str(f'Deseja jogar novamente?[S/N]')).upper().strip()
        if resposta not in 'SN' or resposta in '':
            print(f'Opção inválida')
        else:
            return resposta
            break
def aleatorio():
    from random import randint
    palavras = (
    {'palavra': 'MELISSA', 'dica': 'nome feminino'}, {'palavra': 'ADRIANA', 'dica': 'nome feminino'}, {'palavra': 'MICHAEL', 'dica': 'nome masculino'},
    {'palavra': 'CLAUDETE', 'dica': 'nome feminino'}, {'palavra': 'KAMILLY', 'dica': 'nome feminino'}, {'palavra': 'CAROL', 'dica': 'nome feminino'},
    {'palavra': 'YURI', 'dica': 'nome masculino'}, {'palavra': 'THEO', 'dica': 'nome masculino'}, {'palavra': 'CAROLINE', 'dica': 'nome feminino'},
    {'palavra': 'ACSA', 'dica': 'nome feminino'}
    )
    return palavras[randint(0, len(palavras) - 1)]
