import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta

try:
    #1. creazione di un dataset simulato
    np.random.seed(42)
    
    #2. variabile che rappresenta le righe di dati casuali
    n_rows = 1000
    
    #3. Gestione delle date casuali tra il 01/01/2020 e 31/12/2025
    start_date = datetime(2020,1,1)
    end_date = datetime(2025,12,31)
    days_between = (end_date - start_date).days
    #generiamo una lista di date random tra il 01/01/2020 e il 31/12/2025
    #grazie al timedelta che userà l'intervallo di giorni tra start_date e end_date le date saranno per certo nell'intervallo
    date_range = [start_date + timedelta(days=random.randint(0, days_between)) for _ in range(n_rows)]
    
    #4. faccio delle liste di nomi di negozi e nomi di prodotti che randomicamente verranno scelti per essere messi nel dataset
    negozi = ['Negozio A', 'Negozio B', 'Negozio C', 'Negozio D']
    prodotti = ['Prodotto 1', 'Prodotto 2', 'Prodotto 3', 'Prodotto 4', 'Prodotto 5']
    
    #5. Quantità vendute casuali tra 1 e 20
    quantita = np.random.randint(1, 20, size=n_rows)
    
    #6. Prezzi unitari casuali tra 5.0 e 100.0
    prezzi_unitari = np.round(np.random.uniform(5, 100, size=n_rows),2)
    
    #7. selezionare 1000 volte negozi e prodotti tra i valori delle liste scritte sopra
    negozi_selezionati = np.random.choice(negozi, size=n_rows)
    prodotti_selezionati = np.random.choice(prodotti, size=n_rows)
    
    #8. creazione del dataframe con i dati casuali che ci siamo preparati sopra
    
    dati = {
        'Data': date_range,
        'Negozio': negozi_selezionati,
        'Prodotto': prodotti_selezionati,
        'Quantità': quantita,
        'Prezzo Unitario': prezzi_unitari
    }
    
    df = pd.DataFrame(dati)
    
    #print(df)
    
    #9. creazione della colonna "Vendita totale" nel dataframe
    df['Vendita Totale'] = df['Quantità'] * df['Prezzo Unitario']
    #print(df)
    
    #calcolo delle statistiche richieste
    
    #10. vendite totali per negozio
    vendite_per_negozio = df.groupby('Negozio')['Vendita Totale'].sum()
    
    #11. Vendite totale per prodotto
    vendite_per_prodotto = df.groupby('Prodotto')['Vendita Totale'].sum()
    
    #13. Media delle vendite giornaliere per negozio
    #per prima cosa voglio assicurarmi che la colonna Data del dataframe sia in formato datetime
    df['Data'] = pd.to_datetime(df['Data'])
    #raggruppo per data e negozio e sommo le vendite giornaliere per negozio
    vendita_giornaliere_per_negozio = df.groupby([df['Data'].dt.date, 'Negozio'])['Vendita Totale'].sum().reset_index()
    #calcolo della media delle vendite giornaliere per ogni negozio
    media_vendite_giornaliere_per_negozio = vendita_giornaliere_per_negozio.groupby('Negozio')['Vendita Totale'].mean()
    
    #14. Negozio con il fatturato maggiore di tutti
    negozio_max_vendite = vendite_per_negozio.idxmax()  #da il nome del negozio con vendite maggiori
    max_vendite = vendite_per_negozio.max()  #ci da il valore numerico della vendita totale massima
    
    #15. Prodotto più venduto per valore totale
    prodotto_max_vendite = vendite_per_prodotto.idxmax()
    max_vendite_prodotto = vendite_per_prodotto.max()
    
    #16. stampa dei risultati
    print("Vendite totali per negozio:")
    print(vendite_per_negozio)
    
    print("\nVendite totali per prodotto:")
    print(vendite_per_prodotto)
    
    print("\nMedia vendite giornaliere per negozio:")
    print(media_vendite_giornaliere_per_negozio)
    
    print("\nNegozio con il fatturato complessivo maggiore:")
    print(f"{negozio_max_vendite} con {max_vendite} di fatturato complessivo")
    
    print("\nProdotto più venduto per valore totale:")
    print(f"{prodotto_max_vendite} con {max_vendite_prodotto} di vendite totali")
    
except Exception as e:
    print(f"Si è verificato un errore durante l'esecuzione del codice: {e}") 
