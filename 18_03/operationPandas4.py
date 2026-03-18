#filtrare i dati sui dataframe
#in base a delle condizioni specifiche

import pandas as pd

df = pd.read_csv('files/pokemon.csv')

#print(df["Name" == "Bulbasaur"]) -> così non funziona

#dobbiamo passargli il dataframe con la condizione
print(df[df["Name"] == "Bulbasaur"])
#possiamo usare !=, <, >, in, str.contains, &, |

#ricerca per stringhe parziali (like)
print(df[df["Name"].str.contains('saur')])

#filtraggio con più valori scelti, come clausola in su sql
filtro = ["Bulbasaur", "Charmander", "Squirtle"]
print(df[df["Name"].isin(filtro)])

#condizioni sui numeri
print(df[~(df["Total"] > 700)])
#per negare le condizioni si usa la tilde ~ e si mette tra parantesi la condizione normale

#condizioni complesse con and e or 
#and -> &
#or -> |
print(df[(df["Total"] > 700) & (df["Sp. Atk"] > 160)])

#altri modi per fare i filtraggi sui dataframe
#loc e query

#come possiamo usare  loc?
#è utile quando vogliamo anche dire quali colonne specifiche vogliamo prendere
print(df.loc[(df["Name"] == "Pikachu"), ["Name", "HP", "Type 1"]])

#funzione query per fare i filtraggi con un unica stringa
print(df.query('Total > 750 and Speed > 100'))

#------------------------------------------------------
#come modificare i dati specifici in un dataframe
#come modificare una colonna con loc, colonne multiple, valori multipli, condizioni multiple
print("---------------------------------------------------------")

df1 = pd.read_csv('files/pokemon.csv')

#uso la condizione per dire quale riga prendere e poi scecifico le colonna e assegno il nuovo valore
df1.loc[df1["Name"] == "Bulbasaur", "Name"] = "Riccardosaur"

print(df1.head(1))

#se la condizione filtra su più righe, il cambio del dato andrà su più righe
#ma se voglio cambiare dati in più colonne nello stesso momento?
#posso lavorare anche su valori multipli
df1.loc[df1["Name"] == "Charmander", ["Type 1", "Type 2"]] = ["Water", "Poison"]
print(df1.head(6))

#posso anche lavorare su condizioni multiple per attuare dei cambiamenti sui dati
df1.loc[(df1["Name"].str.contains('saur')) & (df1["Total"] > 500), ["Type 1", "Type 2"]] = ["Fire", "Rock"]
print(df1.head(4))
