#selezionare i dati dai dataframe con pandas
import pandas as pd

df = pd.read_csv('files/pokemon.csv')

#slicing, i pokemon dall'indice 0 al 9
#il secondo parametro è il primo dei non compresi
print(df[0:9]) #posso recuperare un blocco di righe dal dataframe

#prendere i primi tot dal dataframe
print(df.head(3))
#se non metto nulla tra parentesi prende i primi 5
#per prendere gli ultimi tot valori dal dataframe
print(df.tail())

#con lo slicing posso anche scegliere solo specifiche colonne da recuperare
#prendo solo i nomi dei primi 10 pokemon
print(df["Name"][0:10])
print(df["Type 1"].head(4))
#se voglio prendere più colonne contemporaneamente devo usare una lista
print(df[["Name", "HP", "Generation"]].tail(10))


#per selezionare i dati che vogliamo dal dataframe possiamo usare anche le funzioni loc e iloc
#loc -> localization
#iloc -> index localization
print(df.loc[0, "Name"])
print(df.iloc[0, 1])

#con loc localizziamo i dati che ci interessano con la coppia (indice riga, nome colonna)
#con iloc localizziamo i dati che ci interessano con la coppia (indice riga, indice colonna)

#volendo si puo aprire un csv per mettere i dati in un dataframe scegliendo una colonna 
#specifica del csv come indice, questo ci consente di usare loc e iloc in modo diverso

df1 = pd.read_csv('files/pokemon.csv', index_col=1)
#così abbiamo il nome del pokemon con indice

print(df1.loc["Caterpie"])
print(df1.iloc[55])
#avendo letto il csv con colonna indice sul nome, i comandi loc e iloc sono settati sul nome

#vogliamo prendere solo una riga e una colonna
print(df1.loc["Beedrill", "Total"])
print(df1.iloc[18,3])

#slicing con iloc
print(df1.iloc[0:3])

#slicing con loc
print(df1.loc["Bulbasaur": "VenusaurMega Venusaur"])

#prendere tutto il dataframe con loc
print(df1.loc[:])
#voglio recuperare tutte le righe ma solo alcune colonne 
print(df1.loc[:, ["Type 1", "HP", "Total"]])