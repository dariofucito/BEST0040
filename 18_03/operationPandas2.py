#iterare sui dataframe
#iteritems() -> otteniamo chiave:valore
#deprecato ora si usa items()
#iterrows() -> otteniamo indice e la riga
#itertuples() -> otteniamo la tupla (riga senza indice)

import pandas as pd

#per il nostro dataframe di esempio prendiamo solo i primi 10 valori
df = pd.read_csv('files/pokemon.csv').head(10)

#items
for key, value in df.items():
    print(key, value)
    
#iterrows
for index, row in df.iterrows():
    #row["Type 1"] = "Fire"
    print(index, row)
    
#itertuples
for row in df.itertuples():
    print(row)
    
#print(df)
    
#con itertuples non riconosce gli spazi e alcuni caratteri speciali nei nomi di colonna
#con gli iteratori dei dataframe non posso modificare i dati del dataframe perchè lavoriamo non sul dataframe
#ma su una copia del dataframe, di conseguenza se faccio modifiche mentre itero le modifiche le vedo sulla copia
#ma il dataframe rimane uguale

#-----------------------------------
#come ordinare i dati nel dataframe
#------------------------------------

#df = pd.read_csv('files/pokemon.csv')

#per sortare il dataframe ci serve un nuovo dataframe per contenere quello sortato
sdf = df.sort_index()
print(sdf.head(3))
#come prima perchè era gia sortanto per l'indice del dataframe

#possiamo cambiare il tipo di ordinamento
sdf = df.sort_index(ascending=False)
print(sdf.head(3))

#posso anche creare un dataframe dove scelgo la colonna dell'ordinamento
sdf = df.sort_values(by="Name")
#anche qui volendo posso scendere ascendente o discendente
print(sdf.head(3))

#posso anche specificare più colonne
sdf = df.sort_values(by=["Total", "HP"], ascending=False)
print(sdf.head(10))

#------------------------------------------------------
#come manipolare le colonne su un dataframe
#come aggiungere colonne al dataframe o come rimuoverle
#------------------------------------------------------

df = pd.read_csv('files/pokemon.csv')

#aggiungere una colonna in coda al dataframe
df["Allenatore"] = "Riccardo"
print(df)
#posso aggiungere anche più colonne contemporaneamente
#df["Col1", "Col2", "Col3"] = ["dato1", "dato2", "dato3"]

#per aggiungere in punti specifici una colonna (non in coda)
#insert -> indice, nome_colonna, valore
df.insert(1, "Allenatore", "Giovanni")
print(df)

#rimuovere colonne, passando il nome
df.drop("Legendary", inplace=True, axis=1)
print(df)

del df["Generation"]
print(df)

#se la colonna eliminata volete salvarla in un area di memoria perchè poi ti può riservire
colPop = df.pop("Name")
print(df.head(2))
print(colPop.head(2))