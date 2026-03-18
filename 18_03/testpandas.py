#per usare pandas -> pip install pandas

#pandas è un modulo python costruito sopra numpy utilizzato per analisi dati, manipolazione dei dati
#e visualizzazione dati (spesso combinato con altri moduli come matplotlib)

import pandas as pd
#import numpy as np

#creiamo un dataset su python -> dato sotto forma di oggetto (dict)

ds = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio"],
    "Giorni": [31, 28, 31, 30, 31]
}

print("Dati sotto forma di oggetto python")
print(ds)
print("-----------------------------------------------")

#con pandas non si lavora con gli oggetti python come i dict, che sono scomodi da utilizzare per analisi dei dati
#ma si lavora con i DATAFRAME -> vediamo i dati strutturati come se fosse una tabella

df = pd.DataFrame(ds)
print("Dati sotto forma di Dataframe")
print(df)
#da dati in oggetto python a dati strutturati in dataframe, utili per data analysis e machine learning

#series in pandas
#una series in pandas in pratica è una colonna di un dataframe, un array monodimensionale di numpy visto in python
#in un dataframe si passa da una visualizzazione orizzonatale a una verticale


dati = [5,10,15,20,25]
print(dati) #lista di interi, nulla di più

serie = pd.Series(dati)
print(serie) #la lista viene capovolta a colonna e gli vengono assciati gli indicu
#questa è la trasformazione che fa pandas, da lista a serie

#possiamo modificare l'indice dei valori della serie
serie = pd.Series(dati, index=["x1", "x2", "x3", "x4", "x5"])
print(serie)
#tramite indice abbiamo l'accesso agli elementi della serie
print(serie["x2"])

#possiamo creare una serie anche partendo da un dict
dictProva = {"a": 5, "b": 10, "c": 15, "d": 20, "e": 25}

#facendo così noi possiamo creare una serie solo con alcuni elementi scelti
serie2 = pd.Series(dictProva, index=["a", "b"])
print(serie2)


#cos'è un dataframe (oggetto principe utilizzato da pandas per contenere i dati sul codice)
#un dataframe in pandas(libreria per analisi di dati) è una struttura dati tabellare simile a una tabella excel
#o a una tabella sql con righe e colonne etichettate, le righe sono rappresentate con un indice, le colonne hanno dei nomi
#ogni colonna può avere tipi di dati diversi e il dataframe ci consente di fare molte operazioni in maniera semplice
#e veloce come filtraggi, ordinamenti, calcolo di dati derivati e analisi e visualizzazioni sui dati


#per cominciare vediamo come creare un dataframe da un oggetto python (dict), poi vedremo come crearlo da file csv json ecc.
dati2 = {
    'Mesi': ['Gennaio', 'Febbraio', 'Marzo'],
    'Giorni': [31,28,31],
    'Stagione': ['Inverno', 'Inverno', 'Primavera'],
    'Festività': ['Befana', 'Carnevale', 'Festa delle donne']
}
print(dati2)

df1 = pd.DataFrame(dati2)
print(df1)
#cambia del tutto la visualizzazione e quindi anche le modalità con le quali posso lavorare sui dati con le operazioni
#che un analista deve fare, il dataframe è quindi strutturato meglio rispetto ad un oggetto python (dict)

#per accedere a un singolo elemento del dataframe non posso fare come le series
#print(df1[0]) -> così non funziona!
#con la funzione loc posso accedere alle singole righe del dataframe -> loc (localization)
#dopo approfondiremo meglio
print("Elemento singolo dal dataframe")
print(df1.loc[0])
#volendo possiamo anche recuperare una lista di elementi scelti dal dataframe
print("Lista di elementi dal dataframe")
print(df1.loc[[0,2]])
#come abbiamo visto per le series, posso anche cambiare gli l'etichetta degli indici del dataframe
df2 = pd.DataFrame(dati2, index=["riga1", "riga2", "riga3"])
print(df2)
#posso usare l'etichetta nuova per selezionare gli elementi desiderati dal dataframe
print(df2.loc[["riga1", "riga2"]])