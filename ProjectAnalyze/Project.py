import pandas as pd
#Saving data in a variable
readThis = pd.read_csv('C:/Users/Damaris-PC/AnalyzeProperties/DataArch/aluguel.csv', sep=';')
# read dataframe
print(readThis)

type_data = pd.DataFrame(readThis.dtypes, columns =['Data Types'])
type_data.columns.name = 'Variables'
print(type_data)
print('The database presents {} records (real estate) and {} variables'.format(readThis.shape[0], readThis.shape[1]))