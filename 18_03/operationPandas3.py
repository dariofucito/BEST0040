#come salvare dataframe python in file csv, csv compresso, excel
#su excel vediamo come scegliere il nome del folgio, fogli multipli, append to file

import pandas as pd

df = pd.read_csv('files/pokemon.csv')

df2 = df[["Name", "Type 1", "Type 2", "Total"]]

print(df2)

#voglio creare un file csv nuovo dal dataframe df2 che ho in python
df2.to_csv('files/mini-pokedex.csv', index=False)
#con index false non mi mette l'indice peculiare del dataframe nel file csv

#creare csv compresso
compressed_options = dict(method='zip', archive_name='mini-pokedex.csv')
df2.to_csv('files/mini-pokedex.zip', index=False, compression=compressed_options)

#come fare la stessa cosa ma con file excel
#creare un file excel da zero con un foglio solo
df2.to_excel('files/new-pokedex.xlsx', index=False, sheet_name="Pokemon with types and total stats")

df3 = df[["Name", "Type 1", "Type 2", "Generation"]]
#Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed
df4 = df[["Name", "Total", "HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]]

#creare un excel con più fogli, un foglio per ogni dataframe che mi arriva da python
with pd.ExcelWriter("files/nuovi-pokemon.xlsx") as writer:
    df3.to_excel(writer, sheet_name="Tipi pokemon", index=False)
    df4.to_excel(writer, sheet_name="Statistiche", index=False)
    
#come aggiungere un foglio ad un excel esistente
df5 = df.iloc[0:10, 0:4]
print(df5)

#devo aprire lo stream di comunicazione col file in modalità "append"
with pd.ExcelWriter("files/nuovi-pokemon.xlsx", mode="a") as writer:
    df5.to_excel(writer, sheet_name="Primi 10 pokemon", index=False)