import pandas as pd
# 1 - importar arquivos
olt = pd.read_excel(f'OLT2_cosmopolis/cosmopoliscto.xlsx')
depara = pd.read_excel(f'OLT2_cosmopolis/depara.xlsx')
# 2 - ler tabelas e salvar os dados
de = []
para = []
for cto in depara['PARA']:
   para.append(cto)
for cto in depara['DE']:
    de.append(cto)
planilha = olt
# 3 - substituir valores

for indice in range(0, len(de)-1):
    planilha.loc[planilha['CTO'] == de[indice], 'CTO'] = para[indice]

# 4 - novo arquivo alterado

planilha.to_excel('cosmopolis.xlsx')