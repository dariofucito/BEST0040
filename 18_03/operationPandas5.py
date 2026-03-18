#come creare dati aggregati con groupby
#raggruppare dataframe per una colonna o per più colonne
#iterare sui gruppi
#sum() -> somma
#mean() -> media
#count() -> conteggi
#min() -> valore minimi
#max() -> valore massimo

import pandas as pd

df = pd.read_csv('files/pokemon.csv')

#scegliamo la tipologia di raggruppamento che vogliamo fare
#in questo caso vogliamo raggruppare i dati per tipo
types = df.groupby('Type 1')
#print(types) #cosi non si capisce nulla

#print(types.groups) #vediamo la lista dei gruppi con gli id del dataframe assegnati ad ogni gruppo

#possiamo ciclare sul raggruppamento fatto per vedere ancora meglio questi dati
# for group_name, elements in types:
#     print(group_name) #nome del gruppo
#     print(elements) #gli elementi di ogni gruppo
    
#possiamo anche calcolare dati derivati più complessi
#media dei dati delle statistiche in base al tipo
types2 = df.groupby(['Type 1']).mean(numeric_only=True) #da errori per colonne di tipo non numeriche
#print(types2)
#ci sono però delle colonne numeriche delle quali non mi ineressa la media (id del pokedex, generazioni, leggendari)
#posso anche scegliere quali colonne mostrare, levando quelle non consistenti
stats_cols = ['Total', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
types3 = df.groupby(['Type 1'])[stats_cols].mean()
print(types3)
#vediamo anche come ordinare i dati derivati
types3 = df.groupby(['Type 1'])[stats_cols].mean().sort_values(by="Sp. Atk", ascending=False)
#print(types3)
#come ho usato mean() posso usare anche le altre funzioni di gruppo (sum, min, max, count)

types4 = df.groupby(['Type 1', 'Type 2']) #posso fare anche gruppi complessi

#ragioniamo sul count
types5 = df.groupby(['Type 1']).count()
#print(types5)

#così non è il massimo per vedere il conteggio dei pokemon in base al tipo, meglio creare
#una colonna  che contenga il conteggio e poi aggiungerla al dataframe
df['Count'] = 1
types5 = df.groupby(['Type 1'])['Count'].count()
#print(types5)
