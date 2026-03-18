#come utilizzare in pandas varie tipologie di file

import pandas as pd

#per leggere un file csv e metterlo in un dataframe
df = pd.read_csv('files/pokemon.csv')
print(df)
#per i csv che usano il tab come separatore al posto della virgola (csv tabulati) si usa
#df = pd.read_csv('files/pokemon.csv', sep="\t", delimiter="\n")
#se voglio vedere il dataframe in formato stringa -> df.to_string()

#per leggere un file json e metterlo in un dataframe
df1 = pd.read_json('files/pokemon.json')
print(df1)

#per i file excel
df2 = pd.read_excel('files/file-excel.xlsx')
print(df2)
print(df2.loc[2])

#per aprire gli excel dovete fare -> pip install openpyxl
#se non vogliamo l'indice nel dataframe quando ci arrivano i dati da un excel per esempio si può
#usare un parametro dedicato nel metodo read_excel -> index_col=0
df3 = pd.read_excel('files/file-excel.xlsx', index_col=0)
print(df3)
#print(df3.loc[2]) #non si può più fare se non hai indice
print(df3.loc["Mario"])