#Data cleaning -> pulizia dei dati in un dataframe
#dati mancanti, dati incompleti, dati duplicati, dati formattati male, dati che non hanno senso in base al valore

import pandas as pd

#dati di allenamenti con durata in min, data, pulsazioni, pulsazione massima, calorie bruciate
df = pd.read_csv('files/calorie.csv')
print(df)

#ci sono dei problemi
#per esempio abbiamo dei dati nulli (NaN)
#abbiamo date in formati errati 
#abbiamo dei dati duplicati (11-12)
#abbiamo dei valori non realistici, durata di un allenamento 450 minuti

#cominiciamo a pulire i dati dalle celle vuote

new_df = df.dropna()
#elimina le righe con dati vuoti
#restituisce un nuovo dataframe
#se usiamo l'opzione inplace=True
print(new_df)

#possiamo anche rimpiazzare le celle vuote con un valore di default
# df.fillna(0, inplace=True)
# print(df)

#possiamo anche specificare su quale colonne attuare le sostituzioni del valore vuoto
df['Calories'].fillna(df['Calories'].mean(), inplace=True)
df['Date'].fillna('2020/12/22', inplace=True)
print(df)
#abbiamo fatto delle sostituzioni specifiche su calorie e date dell'allenamento

#sistemiamo le date che non sono formattate bene in tutte le righe
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
print(df)

#andiamo adesso a pulire dati errati e non realistici come per esempio la durata di 450 minuti
#per modifiche mirate si usa loc
df.loc[7, "Duration"] = 45
print(df)

#per modifiche ripetute si può usare un ciclo for
for index in df.index:
    if df.loc[index, "Duration"] > 60:
        df.loc[index, "Duration"] = 60
        
#se vogliamo lavorare sui duplicati e rimuoverli
#metodo per scoprire se ci sono duplicati
print(df.duplicated())
#se voglio rimuovere tutti i duplicati dal dataframe
df.drop_duplicates(inplace=True)
print(df)