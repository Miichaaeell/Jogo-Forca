import os
import pandas as pd
import plotly.express as px
lista_lojas = os.listdir('Vendas')
tabela_total = pd.DataFrame()
for arquivo in lista_lojas:
    if 'vendas' in arquivo.lower():
        tabela = pd.read_csv(f'Vendas/{arquivo}')
        #print(tabela)
        tabela_total = tabela_total._append(tabela)
#print(tabela_total)
tabela_total['Faturamento'] = tabela_total['Preco Unitario'] * tabela_total['Quantidade Vendida']
tabela_Produto = tabela_total.groupby('Produto').sum()[['Quantidade Vendida', 'Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_Produto)
tabela_loja = tabela_total.groupby('Loja').sum()[['Faturamento']]
grafico = px.bar(tabela_loja, x=tabela_loja.index , y='Faturamento')
grafico.show()
