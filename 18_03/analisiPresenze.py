import pandas as pd

#simulazione dei dati degli studenti (altrimenti se hai un csv puoi usarlo)
dati = {
    'Nome': ['Alice', 'Filippo', 'Carla', 'Davide', 'Elena'],
    'Corso': ['Fisica', 'Matematica', 'Fisica', 'Chimica', 'Matematica'],
    'Gennaio': [18,20,17,15,19],
    'Febbraio': [17,19,18,13,20],
    'Marzo': [19,20,16,12,20],
    'Aprile': [20,19,15,10,18],
    'Maggio': [20,20,19,13,17],
    'Giugno': [18,19,17,11,16],
    'Luglio': [20,20,18,12,19],
    'Agosto': [19,18,17,10,20],
    'Settembre': [18,19,20,14,19],
    'Ottobre': [17,20,19,13,18],
    'Novembre': [18,19,16,15,19],
    'Dicembre': [20,18,20,12,18]
}

df = pd.DataFrame(dati)


#1. calcolo presenze totali per ogni studente
mesi = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre', 'Ottobre', 'Novembre', 'Dicembre']
df['Totale'] = df[mesi].sum(axis=1) 
#creo la colonna totale che somme le presenze nei 12 mesi per ogni studente
#con axis=1 sommo sulle righe e non sulle colonne
print(df)

#2. calcolo la media mensile di presenze per ogni corso
media_mensile = df.groupby('Corso')[mesi].mean()
print(media_mensile)

#3. corso con media più alta di presenze
corso = media_mensile.mean(axis=1).idxmax() #idxmax identifica il valore più alto tra quelli restituiti
print(f"Il corso con la media più alta di presenze è: {corso}")

#4. classifica degli studenti con più presenze
top_studenti = df.sort_values(by="Totale", ascending=False).head(5)
print("\nTop 5 Studenti per presenze totali:")
print(top_studenti[['Nome', 'Totale']])

#5. classifica delle assenze per ogni corso in base al mese (presupponendo massimo 20 presenze per mese)
assenze = 20 - df[mesi] #calcolo le assenze per ogni mese su ogni studente
df_assenze = assenze.copy() #creo il dataframe delle assenze
df_assenze['Corso'] = df['Corso'] #aggiungo la colonna corso al nuovo dataframe delle assenze
media_assenze = df_assenze.groupby('Corso').mean() #calcolo la media delle assenze mensili per ognuno dei corsi
print("\nMedia assenze mensili per corso: ")
print(media_assenze)