import mysql.connector
from interface import *
def newcadastro():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca',
    )
    cursor = conexao.cursor()
    linha(f'{"Novo Cadastro":^30}')
    nome = str(input('Nome: '))
    comando = f'INSERT INTO jogadores (NOME) VALUES ("{nome}")'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return nome
def deletar():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca'
    )
    cursor = conexao.cursor()
    comando = f'SELECT ID, NOME FROM jogadores'
    cursor.execute(comando)
    linha(f'{"DELETAR JOGADOR":^30}')
    resultado = cursor.fetchall()
    print(f'\033[33m{"INDICE":<15}{"NOME":>15}\033[m')
    for indice, jogador in resultado:
        print(f'\033[33m{indice:<15}{jogador:>15}\033[m')
    while True:
        delete = str(input('Qual jogador quer deletar? '))
        if delete.isnumeric() and int(delete) <= len(resultado) and int(delete) != 0:
            print(f'Jogador {resultado[int(delete) - 1][1]} excluido com Sucesso!')
            break
        else:
            print(f'"{delete}" não é válido, utilize o indice para selecionar o jogador ')

    comando1 = f'DELETE FROM jogadores WHERE ID = {int(delete)}'
    comando2 = f'ALTER TABLE jogadores DROP ID'
    comando3 = f'ALTER TABLE jogadores ADD ID INT NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (ID)'
    cursor.execute(comando1)
    cursor.execute(comando2)
    cursor.execute(comando3)
    conexao.commit()
    cursor.close()
    conexao.close()
def mostrarjogadores():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca'
    )
    cursor = conexao.cursor()
    linha(f'{"JOGADORES":^30}')
    comando = f'SELECT ID, NOME, PARTIDAS FROM jogadores'
    cursor.execute(comando)
    jogadores = cursor.fetchall()
    print(f'\033[34m{"INDICE":<6}{"NOME":^15}{"PARTIDAS":>7}\033[m')
    for indice, nome, partidas in jogadores:
        print(f'{indice:<6}{nome:^15}{partidas:^7}')
    jogador = str(input('Quem está jogando? '))
    while not jogador.isnumeric() or int(jogador) == 0 or int(jogador) > len(jogadores):
        jogador = str(input(f'"{jogador.upper()}" não é um indice válido, tente novamente \nQuem está jogando? '))
    cursor.close()
    conexao.close()
    return jogador
def partidas(jogador):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca'
    )
    cursor = conexao.cursor()
    comando = f'SELECT PARTIDAS FROM jogadores WHERE ID = {jogador}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado[0][0]
def editarpartida(partida, jogador):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca',
    )
    cursor = conexao.cursor()
    comando = f'UPDATE jogadores SET PARTIDAS = {partida} where ID = {jogador}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
def vitorias(jogador):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca'
    )
    cursor = conexao.cursor()
    comando = f'SELECT VITORIAS FROM jogadores WHERE ID = {jogador}'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultado[0][0]
def editarvitorias(vitorias, jogador):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca',
    )
    cursor = conexao.cursor()
    comando = f'UPDATE jogadores SET VITORIAS = {vitorias} where ID = {jogador}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
def editarpontos(pontos, jogador):
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca',
    )
    cursor = conexao.cursor()
    comando = f'UPDATE jogadores SET PONTOS = {pontos} where ID = {jogador}'
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
def verpontos():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='jogoforca'
    )
    cursor = conexao.cursor()
    linha(f'{"RANKING DOS JOGADORES":^30}')
    print(f'\033[34m{"Jogador":<8}{"PARTIDAS":^10}{"VITÓRIAS":^10}{"PONTOS":>6}\033[m')
    comando = f'SELECT NOME,PARTIDAS, VITORIAS, PONTOS FROM jogadores ORDER BY PONTOS DESC'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for jogador, partida, vitoria, ponto in resultado:
        print(f'\033[34m{jogador:<8}{partida:^10}{vitoria:^10}{ponto:>6.2f}\033[m')
    cursor.close()
    conexao.close()

