import pandas as pd
import matplotlib.pyplot as plt

#Saving data in a variable

readThis = pd.read_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/aluguel.csv', sep=';')

selectResidential = pd.read_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/residential.csv', sep=';')

def meu_switch():
    validacao = True

    while validacao:
        z = int(input("Menu : "
                      "\n 1 : Property Type"
                      "\n 2 : Selection only residential "
                      "\n 3 : Selection only apartments"
                      "\n 4 : Selection only condominium house, village house and houses"
                      "\n 5 : Properties with an area between 60 and 100 square meters"
                      "\n 6 : Properties with rent less than 2000 thousand reals and with 4 bedrooms"
                      "\n 7 : Eliminating null value"
                      "\n 8 : Creating new variables on the dataframe"
                      "\n 9 : Grouping: neighborhood media"
                      "\n 10 : Sair \n"))
        if z == 1:
            filter()
        elif z == 2:
            selection_residential()
        elif z == 3:
            selection_apart()
        elif z == 4:
            selection_home_villa_condo()
        elif z == 5:
            selection_area_properties()
        elif z == 6:
            selection_rooms_low_value()
        elif z == 7:
            selection_eliminating_null_value()
        elif z == 8:
            selection_new_variables()
        elif z == 9:
            selection_grouping()
        elif z == 10:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

def filter():
    propertyType = readThis['Tipo']
    type(propertyType)
    #inplace - quando seu dafault esta marcado como true,
    # ele modifica a variável a partir da execução do método,
    # não precisamos criar uma variável e atribuir a execução à ela.
    propertyType.drop_duplicates(inplace = True)

    #Criando um indice para visualizacao id
    propertyType = pd.DataFrame(propertyType)
    propertyType.index = range(propertyType.shape[0]) # retornar o número de registros de um DataFrame
    # df.index = range(len(df)) retornar o número de registros de um DataFrame
    propertyType.columns.name = 'id'
    print(propertyType)
def selection_residential():
    residential = ['Quitinete',
                   'Casa',
                   'Apartamento',
                   'Casa de Condomínio',
                   'Casa de Vila']
    # Vamos usar o isin(gera True e False) para selecionar, usamos a lista como corte
    selection = readThis['Tipo'].isin(residential)

    #Usaremos um método de seleção no DataFrame, de maneira que só tenhamos os registros que possuem a marcação True
    data_residential = readThis[selection]
    list(data_residential['Tipo'].drop_duplicates())
    #reformular o index para o corte de informacao da lista, gera o index novamento com nova contagem
    data_residential.index = range(data_residential.shape[0])
    print(data_residential.head(10))

    #Exportando a Base de Dados para csv
    # index false - índice da nossa tabela nao ser interpretado como sendo uma variável.
    data_residential.to_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/residential.csv', sep=';', index=False)
    data_residential_read = pd.read_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/residential.csv', sep=';',)
    print(data_residential_read)
    print(data_residential_read.Tipo.unique)
    print(data_residential_read.Tipo.value_counts())

    numeros = [i for i in range(11)]
    letras = [chr(i + 65) for i in range(11)]
    nome_coluna = ['N']

    df = pd.DataFrame(data=numeros, index=letras, columns=nome_coluna)
    selecao = df['N'].isin([i for i in range(11) if i % 2 == 0])
    df = df[selecao]
    print(df)

def selection_apart():
    selection_apartm = selectResidential['Tipo'] == 'Apartamento'
    print(selectResidential[selection_apartm].head(10))
    #Numero de ocorrencias
    print('There are {} registered apartments'.format(selectResidential[selection_apartm].shape[0]))

def selection_home_villa_condo():
    selection_home_villa_condo = (selectResidential['Tipo'] == 'Casa') | (selectResidential['Tipo'] == 'Casa de Vila') | (selectResidential['Tipo'] == 'Casa de Condomínio')
    print(selectResidential[selection_home_villa_condo].head(10))
    # Numero de ocorrencias
    print('There are {} records of condominium house, village house and houses'
          .format(selectResidential[selection_home_villa_condo].shape[0]))

def selection_area_properties():
    # Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
    # 60 <= Area <=100
    selection_area = (selectResidential['Area'] >= 60) & (selectResidential['Area'] <= 100)
    print(selectResidential[selection_area].head(10))
    # Numero de ocorrencias
    print('There are {} real estate records with an area between 60 and 100 square meters'
          .format(selectResidential[selection_area].shape[0]))

def selection_rooms_low_value():
    # Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.
    selection_value_rooms = (selectResidential['Quartos'] >= 4) & (selectResidential['Valor'] < 2000)
    print(selectResidential[selection_value_rooms].head(10))
    # Numero de ocorrencias
    print('There is {} registration of properties with a profile of 4 rooms and with a value of less than 2000 thousand rental rents'
          .format(selectResidential[selection_value_rooms].shape[0]))
def selection_eliminating_null_value () :
    #Possuímos dois métodos que nos ajudam a realizar a seleção que precisamos.
    # O primeiro deles é isnull(). Tal método irá gerar um DataFrame booleano,
    # em que a observação marcada como True caracteriza um dado nulo
    # método notnull(), que funciona exatamente da maneira inversa ao isnull(): se a informação for nula, será utilizada a notação False
    # Método info(), que nos exibe informações do DataFrame.
    print(selectResidential.info())
    # Iremos observar as variáveis que apresentam dados faltantes.
    print(selectResidential[selectResidential['Valor'].isnull()])

    # dropna() elimina dados do dataframe
    A = selectResidential.shape[0]
    selectResidential.dropna(subset=['Valor'], inplace=True)
    B = selectResidential.shape[0]
    print('Exists {} null records deleted'.format(A - B))

    # Agora vamos substituir esses valores nulos por 0
    selection = (selectResidential['Tipo'] == 'Apartamento') & (selectResidential['Condominio'].isnull())
    # Para eliminar as assinaturas nulas selecionadas ao invés de coletá-las, iremos adicionar ~ em selecao, que inverte a Series booleana.
    A = selectResidential.shape[0]
    data = selectResidential[~selection]
    B = selectResidential.shape[0]
    print('Exists {} null records deleted'.format(A - B))
    #O que faremos é manter esses dados, mas atribuir o valor 0 a eles.
    data = data.fillna({'Condominio': 0, 'IPTU': 0})
    print(data.info())
    # Agora vamos salvar esse dataframe, não queremos incluir o índice
    data.to_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/residential.csv', sep=';',index = False)

def selection_new_variables ():
    #Criando uma variavel Gross Value, e atribuindo a ela a soma do valor + condominio + iptu
    selectResidential['Gross Value'] = selectResidential['Valor'] + selectResidential['Condominio'] + selectResidential['IPTU']
    selectResidential['Value m2'] = selectResidential['Valor'] / selectResidential['Area']
    # Criou uma variavel value m2 e arredondou para 2 casas
    selectResidential['Value m2'] = selectResidential['Value m2'].round(2)
    selectResidential['Gross Value m2'] = (selectResidential['Gross Value'] / selectResidential['Area']).round(2)
    #Agora, criaremos uma variável que abrigue os tipos de imóvel casa e apartamento, para tanto, devemos coletar a variável Tipo e recolher
    # esses marcadores e indentifica-los. Criaremos uma lista com a identificação das house, então
    house = ['Casa', 'Casa de Condomínio', 'Casa de Vila']
    #apply() esse método pertmite que apliquemos uma função à cada registro do DataFrame. Para tanto, criaremos uma função lambda : 'lambda x: 'Casa' if x in casa else 'Apartamento'
    selectResidential['Aggregate Type'] = selectResidential['Tipo'].apply(lambda x: 'Casa' if x in house else 'Apartamento')
    print(selectResidential.head(10))

    #Formas de apagar uma variavel do dataframe
    #Criamos um DataFrame auxiliar para explorarmos as possibilidades disponíveis.
    data_aux = pd.DataFrame(selectResidential[['Gross Value', 'Value m2', 'Gross Value m2', 'Aggregate Type']])
    print(data_aux.head(10))
    #Deletar opcao:
    #1 del
    del data_aux['Gross Value']
    #2 pop
    data_aux.pop('Gross Value m2')
    #3 drop, axis metodo usado para definir coluna 1 linha 0, para funcionar com esse metodo deve ser usado o implace true
    selectResidential.drop(['Gross Value m2', 'Gross Value'], axis=1, inplace=True)
    print(selectResidential.head(10))
    selectResidential.to_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/residential.csv', sep=';',index = False)
    print(selectResidential.Tipo.unique())
    print(selectResidential.Tipo.value_counts())

def selection_grouping():
    tratNeigh = selectResidential['Bairro'].drop_duplicates()
    tratNeigh.to_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/neighborhood.csv', sep=';', index=False)
    #Transforma dataframe em lista, value.tolist()
    listNeigh  = tratNeigh.values.tolist()

    #Criei uma lista com todos os bairros, agora posso trabalhar agrupandos e assim fazendo uma media de valor por bairros
    selection = selectResidential['Bairro'].isin(listNeigh)
    data = selectResidential[selection]
    neighborhood_group = data.groupby('Bairro')
    print(neighborhood_group[['Valor', 'Condominio']].mean().round(2))
    #Estatísticas descritivas
    #describre() -  DataFrame com as colunas count a frequência; mean a média; std o desvio padrão; mino valor mínimo; 25%
    # o primeiro quartio, 50% a mediana, 75% o terceiro quartio e max, o valor máximo.
    print(neighborhood_group['Valor'].describe().round(2))
    #O método aggregate() permite selecionar um conjunto de estatísticas personalizado. É possível declarar o método de forma simplificada, utilizando agg()
    print(neighborhood_group['Valor'].aggregate(['min', 'max', 'sum']).rename(columns = {'min': 'Mínimo', 'max': 'Máximo'}))

    plt.rc('figure', figsize=(20, 10))
    fig = neighborhood_group['Valor'].mean().plot.bar(color='blue')
    fig.set_ylabel('Rent Value',fontsize=16)
    fig.set_title('Average Rental Price per Neighborhood', {'fontsize': 16})
    plt.show()

    classes = [0, 2, 4, 6, 100]
    labels = ['1 and 2 bedrooms', '3 and 4 bedrooms', '5 and 6 bedrooms', '7 bedrooms or more']
    #A função cut() é uma ferramenta do pandas que auxilia na criação distribuições de frequências.
    #É possível criar labels para as classes criadas pela função cut().
    #A função cut() permite que sejam especificados os limites de cada classe.
    bedrooms = pd.cut(selectResidential.Quartos, classes, labels=labels)
    #plt.bar(labels,bedrooms)
    print(pd.value_counts(bedrooms))

    # matplotlib para plotar um grafico
    plt.rc('figure', figsize=(20, 10))
    fig = pd.value_counts(bedrooms).plot.bar(color='blue')
    fig.set_ylabel('Number of Occurrences', fontsize=16)
    fig.set_title('List of Rooms', {'fontsize': 16})
    plt.show()

if __name__ == "__main__":
    print(meu_switch())