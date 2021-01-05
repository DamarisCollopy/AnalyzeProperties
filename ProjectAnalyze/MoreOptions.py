import pandas as pd
import xlrd
# more options for reading files using pandas
def meu_switch():
    validacao = True

    while validacao:
        z = int(input("Menu : "
                      "\n 1 : Open file in Json "
                      "\n 2 : Open file in Json Pandas "
                      "\n 3 : Open file TXT"
                      "\n 4 : Open file generated by excel"
                      "\n 5 : Open html file"
                      "\n 6 : Open web table"
                      "\n 7 : Series and DataFrame"
                      "\n 8 : Sair \n"))
        if z == 1:
            open_json()
        elif z == 2:
            open_json_pandas()
        elif z == 3:
            openTxt()
        elif z == 4:
            openExcel()
        elif z == 5:
            webForm()
        elif z == 6:
            webForms3()
        elif z == 7:
            series()
        elif z == 8:
            print("Programa encerrado")
            break
        else:
            print("opcao inválida")

def open_json():
    json = open('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/aluguel.json')
    print(json.read())

def open_json_pandas():
    df_json = pd.read_json('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/aluguel.json')
    print(df_json)

def openTxt():

    txt = open('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/aluguel.txt')
    print(txt.read())

    df_txt = pd.read_table('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/aluguel.txt')
    print(df_txt)

def openExcel():
    df_xlsx = pd.read_excel('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/aluguel.xlsx')
    print(df_xlsx)

def webForm():
    df_html = pd.read_html('C:/Users/Damaris-PC/AnalyzeProperties/Extras/data/dados_html_1.html')
    print(df_html[0])

    # web address
    df_html = pd.read_html('https://unafiscosaude.org.br/site/tabelas-de-precos-dos-planos-ativos-para-comercializacao/')
    print(df_html[0])

def webForms3():
    df_html = pd.read_html('https://www.federalreserve.gov/releases/h3/current/default.htm')
    print(len(df_html))
# select tables to read
    print(df_html[0])
    print(df_html[1])
    print(df_html[2])
def series():
    data = [1, 2, 3, 4, 5]
    s = pd.Series(data)
    print(s)

    index = ['Linha' + str(i) for i in range(5)]
    s = pd.Series(data=data, index=index)
    print(s)

    # Uma outra maneira é criar um dicionário e passá-lo para pd.Series
    data = {'Linha' + str(i): i + 1 for i in range(5)}
    s = pd.Series(data)
    s1 = s + 2
    s2 =  s + s1
    print(s1)
    print(s2)
    # Dataframe
    # usando lista
    data = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

    df1 = pd.DataFrame(data=data)
    print(df1)

    # criando rotulos para o dataframe
    index = ['Linha' + str(i) for i in range(3)]
    df1 = pd.DataFrame(data=data, index=index)
    print(df1)
    # Criando as colunas para o dataframe
    columns = ['Coluna' + str(i) for i in range(3)]

    # usando dicionário
    #data = {'Coluna0': {'Linha0': 1, 'Linha1': 4, 'Linha2': 7},
            #'Coluna1': {'Linha0': 2, 'Linha1': 5, 'Linha2': 8},
            #'Coluna2': {'Linha0': 3, 'Linha1': 6, 'Linha2': 9}}
    #print(data)

    #usando em vez de lista tuplas
    data = [(1, 2, 3),
            (4, 5, 6),
            (7, 8, 9)]
    # criando o dataframe com rotulo(index) e colunas(colums)
    df2 = pd.DataFrame(data=data, index=index, columns=columns)
    df1 = pd.DataFrame(data=data, index=index, columns=columns)
    df3 = pd.DataFrame(data=data, index=index, columns=columns)
    #concatenar DataFrames
    df1[df1 > 0] = 'A'
    df2[df2 > 0] = 'B'
    df3[df3 > 0] = 'C'

    print(df1)
    df4 = pd.concat([df1, df2, df3])
    print(df4)
    # juntar por linhas usando o axis
    df4 = pd.concat([df1, df2, df3], axis=1)
    print(df4)

if __name__ == "__main__":
    print(meu_switch())