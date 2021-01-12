import pandas as pd

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
                      "\n 8 : Sair \n"))
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

if __name__ == "__main__":
    print(meu_switch())