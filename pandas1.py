import pandas as pd

# carregando o dataset, usando o separador ';' para separar as colunas corretamente
data = pd.read_csv('2004-2021.csv', sep=';')
dataBKP = data
# print(data)

# a funcao .head() determina a quantidade de linhas a serem mostradas do dataframe
print(data.head(6))

# a funcao .info() mostra as informacoes do dataframe, como: nome das colunas, tipos de dados das colunas e quantidade de linhas das colunas
print(data.info())

# type mostra o tipo da variavel
print(type(data))

# .shape mostra a quantidade de linhas e de colunas do dataframe (row,collum)
print(data.shape)

# o comando pd.DataFrame cria um novo dataframe com os parametros que voce passar (como se fosse um json)
carro_df = pd.DataFrame({
    'Nome': ['Corsa', 'Chevete', 'Uno'],
    'Ano':['2001', '2003', '2002', ],
    'Preco':['20000','15000','55000',]
})

# mostrando o dataframe carro_df, mostrando as informacoes da tabela, e mostrando a quantidade de linhas e colunas 
print(carro_df , carro_df.info() , carro_df.shape)

# .columns mostra as colunas do dataframe
print(carro_df.columns)

# type() mostra o tipo da variavel
print(type(carro_df))

# list() transforma a variavel em uma lista
print(list(carro_df))

# .rename e usado para renomear dados da coluna, sendo eles: columns, index... (ps: essa funcao retorna uma COPIA do dataframe original, ou seja, o original nao deixa de existir)
carro_df_rename = carro_df.rename(columns={
    'Nome': 'Modelo',
    'Ano': 'Lancamento'
})
# print(carro_df_rename)

# o metodo inplace= True define que o rename vai passar a ser o valor original, assim excluindo a taela original e acomodando o rename no lugar dela
carro_df_rename = carro_df.rename(columns={'Nome': 'Modelo','Ano': 'Lancamento'}, inplace=True)
print(carro_df)


# mostrando todos os dados da coluna ESTADO
print('---------------------------\n',data['ESTADO'])

# .iloc[numero da linha] retorna todos os dados da linha passada como parametro para o mesmo
print(data.iloc[1])

# criando uima series e alterando o nome da serie 
notas = pd.Series([1,2,3], index=['prova 1','prova 2','prova 3'], name="Notas do kaike")
print(notas)

# .copy cria uma COPIA da series passada (PRODUTO)
produto_copy = data['PRODUTO'].copy()

# atribuindo o valor COMBUSTIVEL a todas as linhas da coluna PRODUTO
newValuesData = data['PRODUTO'] = 'Combustivel'
print(data['PRODUTO'])

# atribuindo os dois valores do data.shape para duas variaveis (numero de linhas, numero de colunas)
nrows, ncols = data.shape

# criando um for que percorre todas as linhas do dataframe e insere a string Produto e o numero da variavel de repeticao
novos_produtos = [f'Produto {i}'for i in range(nrows)]

# verificando a quantidade de linhas no dataFrame
print(len(novos_produtos))

# inserindo o valor da variavel novos produtos para todos os elementos da coluna PRODUTO
data['PRODUTO'] = novos_produtos
print(data)


for i in range(len(carro_df)):
    if carro_df.loc[i, 'Modelo'] == 'Corsa':
        carro_df.loc[i, 'Preco'] = '0'
print(carro_df)


# maneira de inserir nova coluna (no final do dataframe) com valores setados, nesse caso coloquei os valores das linhas como DEFAULT
data['NOVA COLUNA'] = 'DEFAULT'
print(data)

data['NOVA COLUNA'] = range(data.shape[0])
print(data)


data['PREÇO MÁXIMO DISTRIBUIÇÃO(dolares)'] = data['PREÇO MÁXIMO DISTRIBUIÇÃO'] * 6
print(data)


