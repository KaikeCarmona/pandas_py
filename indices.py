import pandas as pd

data = pd.read_csv('2004-2021.csv', sep=';')
print(data.index)

# atribuindo um index para as linhas, serve como indentificador 
pesquisa = pd.DataFrame({
    'bom': [1,2,3],
    'Medio': [3,4,5],
    'ruim': [6,3,0]
},index=['xbox', 'ybox','nintendo'])

# mostrando o cabeçalho do dataframe
print(pesquisa.head())

# mostrando os index do dataframe
print(pesquisa.index)

# selecionando a linha um do dataframa, no caso uma linha é uma series
print(data.iloc[1])

# selecionar as linhas com o indice de 0 a 5
print(data.iloc[slice(0,5)])

#mostrando itens soltos do dataframe pelo indice 
print(data.iloc[[1,6,8,23]])

# retorna as 
print(data.iloc[1,3])

# retorna as linhas de uma coluna com o nome xbox
print(pesquisa.loc['xbox'])

# retorna o calor da linha xbox, na coluna ruim
print(pesquisa.loc['xbox', 'ruim'])

# retorna dois indices
print(pesquisa.loc[['xbox', 'ybox']])

# retorna todas as linhas, mas apenas as colunas bom e ruim(: e o intervalo de linhas que ele retorna, no caso esta vazio, entao retorna todas as linhas)
print(pesquisa.loc[:,['bom', 'ruim']])

# excluindo uma coluna do dataframe, del nome_do_dataframe["nome da coluna"]
# del data['REGIÃO']

# salvando o arquivo, separando o mesmo por ;
data.to_csv('./preprocessado.csv', index=False, sep=";")
print(data)

# .unique() mostra todos os dados unicos na coluna selecionada
print(data['ESTADO'].unique())

# cont = 0
# for i in range(len(data)):
#     if data.loc[i, 'REGIÃO'] == 'NORTE':
#         print(data.i.head(1))
 
# crianto um vetor que armazena todas as linhas do dataframe que tem valor da coluna estado como sao paulo
selecao = data['ESTADO'] == 'SAO PAULO'

# mostrando as linhas armazenadas na variavel selecao
print(data[selecao])

# outra maneira de se fazer a filtragem e usando o emtodo query(), nele deve ser passado uma comparacao, entre a coluna procurada e o valor desejado
produtos_sp = data.query('ESTADO == "SAO PAULO"')
print(produtos_sp.head())

produtos_sp.reset_index()
print(produtos_sp.head())

# Retornando todos os valores da coluna estado com o valor rio de janeiro e com os valores da coluna preco medio revenda maiores que 2.0
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['NÚMERO DE POSTOS PESQUISADOS'] < 100)
print(selecao)

# usando o .query nao vai funcionar pois ele nao aceita nenhum caractere especial ou com acentos
# selecao2 = data.query('ESTADO == "SAO PAULO" and "NÚMERO DE POSTOS PESQUISADOS" > 100')

print(data[selecao])

# utilizando operador or na consulta
operadorOR = data.query('ESTADO == "SAO PAULO" or ESTADO == "RIO DE JANEIRO"')
print(operadorOR)

              
# para fazer filtragem de dois parametros, e melhor evitar o AND pois consome muita memoria e le duas vezes o data frame, dessa maneira o dataframe sera lido uma fez no filtroRJ, e depois a selecao_2 vai ler o filtro rj e pegar os valores menores que 100 desse dataframe prefiltrado
filtroRJ = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[filtroRJ]
selecao_2 = postos_rj['NÚMERO DE POSTOS PESQUISADOS'] < 100
# print(selecao_2)

# corrigindo a coluna PREÇO MÉDIO REVENDA para que seus valores sejam numericos
data['PREÇO MÉDIO REVENDA'] = pd.to_numeric(data['PREÇO MÉDIO REVENDA'], errors='coerce')



# duas maneiras de fazer filtragem com pandas

# essa primeira vai fazer a leitura do dataframe original varias vezes para encontrar os valores procurados de cada coluna
postos_sp_rj = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO' )
produto = (data['PRODUTO'] == 'OLEO DIESEL')
selecao_produto = (data['PREÇO MÉDIO REVENDA'] > 2)
selecao_final = postos_sp_rj & produto & selecao_produto
print(data[selecao_final])
 
# essa segunda forma esta procurando os valores das colunas ja no dataframe filtrado
# filtra os estados de sao paulo e rio de janeiro 
selecao_1 = (data['ESTADO'] == 'SAO PAULO') | (data['ESTADO'] == 'RIO DE JANEIRO' )
# cria um dataframe que tem somente os resultados da filtragem
postos_sp_rj = data[selecao_1]
# filtra os produtos que sao oleo diesel dentro do dataframe filtrado, ou seja, faz um filtro dentro do filtro
selecao_2 = (postos_sp_rj['PRODUTO'] == 'GASOLINA COMUM')
# define um novo dataframe com esses dois filtros
postos_sp_rj_gasolina = postos_sp_rj[selecao_2]
# faz um novo filtro para pegar todos as linhas com as colunas de PREÇO MÉDIO REVENDA maiores doq R$2,00
selecao3 = (postos_sp_rj_gasolina['PREÇO MÉDIO REVENDA'] > 2)
# define um novo dataframe com esse novo filtro
postos_sp_rj_gasolina_maior_que_2 = postos_sp_rj_gasolina[selecao3]
# resultado do filtro
print(postos_sp_rj_gasolina_maior_que_2)


# maneiras de fazer filtragem diferentes

# usando um array com valores e verificando se ele existe dentro da coluna
# anos = [2008, 2010, 2012]
# .isin devolve um valor boleano, se o valor buscado estiver na coluna devolve true se nao false
# print(data['ANO'].isin(selecao))

# dessa meneira usamos a querye, para podermos usar uma variavel na querye usamos o @ no comeco dela, assim procuramos o @ano dentro da coluna ANO
# print(data.query('ANO in @anos'))

# para cada index e linha das 10 primeiras linhas do dataframe, imprimir os nomes dos estados
for index, row in data.head(10).iterrows(): 
    print(f'indice{index} == {row["ESTADO"]}')



# Convertendo tipos de dados das colunas

data_pre = data.copy()
 
# Convertendo tipos de dados (O argumento format="%d/%m/%Y" especifica que as strings seguem o formato dia/mês/ano.)
data_pre["DATA INICIAL"] = pd.to_datetime(data_pre["DATA INICIAL"], format="%d/%m/%Y")
data_pre["DATA FINAL"] = pd.to_datetime(data_pre["DATA FINAL"], format="%d/%m/%Y")

# convertendo atributos das colunas para numericos
for atributo in ['MARGEM MÉDIA REVENDA', 'DESVIO PADRÃO DISTRIBUIÇÃO','PREÇO MÍNIMO DISTRIBUIÇÃO','PREÇO MÁXIMO DISTRIBUIÇÃO']:
    #em caso de erro na conversao, o argumento ERRORS retorna um valor Nan para o campo, identificando que o campo nao representa um numero
    data_pre[atributo]= pd.to_numeric(data_pre[atributo], errors='coerce')
print(data_pre.info())

# criando uma series que comporta todos os dados e retorna se o dado e null ou nao, de maneira booleana
mask = data_pre['MARGEM MÉDIA REVENDA'].isnull()
# nos dados originais, retorna os valores do PREÇO MÉDIO DISTRIBUIÇÃO dos registros que agora possuem valores Nan
print(data_pre[mask])

# retorna uma copia do data_pre com todos os valores Nan das colunas 'MARGEM MÉDIA REVENDA' 'DESVIO PADRÃO DISTRIBUIÇÃO' 'PREÇO MÍNIMO DISTRIBUIÇÃO' 'PREÇO MÁXIMO DISTRIBUIÇÃO'
# preenchidos com valores personalizados
data_pre_fill = data_pre.fillna(value={
    'MARGEM MÉDIA REVENDA': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})
print(data_pre_fill[mask])

# remove no proprio dataframe todas as linhas/registros com valores Nan em quaisquer colunas/atributos
data_pre.dropna(inplace=True)

print(data_pre.info())

data_pre.to_csv('./GasPricingBrazil_processado_final.csv', index=False)
print(data_pre)

data_final = pd.read_csv('./GasPricingBrazil_processado_final.csv')

# describe retorna algumas analises descritivas do dataframe, como: contagem, mediana...
stats = data_final.describe()
print(stats) 
print(stats[['PREÇO MÉDIO REVENDA', 'PREÇO MÍNIMO DISTRIBUIÇÃO']].describe())

# retorna algumas analises de uma coluna expecifica
print(data_final['PREÇO MÉDIO REVENDA'].describe())

# acessando estatisticas especificas
print(stats .loc[['min','max','mean']])

# mostrando estatisticas especificas (linhas) e colunas especificas
print(stats .loc[['min','max','mean'], ['NÚMERO DE POSTOS PESQUISADOS','PREÇO MÉDIO REVENDA','MARGEM MÉDIA REVENDA']])

# retorna o menor valor de uma coluna
min = data_final['PREÇO MÍNIMO DISTRIBUIÇÃO'].min()
# retorna a media de uma coluna
std = data_final['PREÇO MÍNIMO DISTRIBUIÇÃO'].std()

# :.2f deixa o valor formatado com duas casas decimais
print(f'a media dos precos minimos de distribuicao e {min:.2f} +- {std:.2f}')

# retorna todos os valores unicos da coluna estado de ESTADO de maneira organizada por ordem alfabetica em uma series
print(sorted(data_final['ESTADO'].unique()))

# retorna a quantidade de registros para cada valor da coluna e converte uma series em um dataframe
print(data_final['ESTADO'].value_counts().to_frame())

# criando um dataframe
df = pd.DataFrame({
    'A' : [1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]},
    index = ['LINHA1', 'LINHA2', 'LINHA3'])

# funcao que soma valores 
def soma_linha(linha):
    return linha.sum()
def soma_coluna(series):
    return series.sum()

# o metodo apply funciona como um for porem e mais eficaz, para usalo podemos escolher entre inteirar em linha ou coluna
# nesse caso usamos o axis=1 que intera sobre linha, axis=0 intera sobre coluna
# df.apply executa uma funcao dentro de uma linha ou coluna do df, soma_linha_coluna e a funcao que sera executada, axis=1 significa que ira inteirar sobre linha
df['SOMA_Linha'] = df.apply(soma_linha, axis=1)
print(df)

# criando uma nova linha que apresenta os valores somados das colunas
# df.loc cria uma nova linha
df.loc['SOMA_Coluna'] = df.apply(soma_coluna, axis=0)
print(df)

# criando uma nova coluna e inserindo dentro dela uma series com os valores das medias calculadas das linhas A, B, C que a funcao lambda retorna
df['MEDIA'] = df[['A','B','C']].apply(lambda series: series.mean(), axis=1)
print(df)

# criando uma nova coluna e inserindo dentro dela uma series com os valores das multiplicacao de todos os valores da coluna C por 3
df['C_MULT'] = df['C'].apply(lambda x: x * 2)
print(df)

nomes = pd.Series(['kaike', 'pedro','antonio'])

# .map retorna uma series com os valores tratados
print(nomes.map(lambda x: x.upper()))
print(nomes)

# usando o .str podemos acessar funcoes de string, como o .upper, .lower
print(nomes.str.upper())

# armazenando todos os dados em grupos, ordenados pela coluna REGIAO
grupos = data_final.groupby('REGIÃO')

# mostrando os elementos de cada grupo
print(grupos.groups)

# mostrando os grupos ordenados pelos indices
print(grupos.indices)

# mostrando os elementos de um grupo expeficico
print(grupos.get_group('CENTRO OESTE'))

# fazendo uma analise descritiva dos das colunas dos grupos, como a contagem, media, numero minimo e maximo
print(grupos.describe())

# mostrando valores expecificos das analises
# print(grupos.mean())
# print(grupos.min())
# print(grupos.max())

# mostrando os menores valores de cada coluna de cada grupo da coluna REGIÃO
# print(data_final.groupby('REGIÃO').min())

# criando uma series que armazena os dados de cada regiao e seus produtos
grupos = data_final.groupby(['REGIÃO', 'PRODUTO'])

# calcula as medias de cada valor de coluna de cada regiao
print(grupos.mean)

# calcula apenas a media da coluna PRECO MEDIO REVENDA
print(grupos['PREÇO MÉDIO REVENDA'].mean())

# a funcao .agg traz adiciona uma funcao ou mais para elementos de um dataframe, nocaso estamos calculando o numero minimo e maximo para a coluna preco medio revenda de cada elemento da coluna regiao 
print(grupos['PREÇO MÉDIO REVENDA'].agg([min, max]))

