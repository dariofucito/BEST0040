
#gestione con try - finally (senza context manager)
f = open('C:/Users/dario/Desktop/corso_python/16_03/dipendenti.txt', 'r', encoding='utf-8')
try:
    contento = f.read()
#    risultato = processa(contenuto)
finally:
    f.close()
    
#con context manager
with open('C:/Users/dario/Desktop/corso_python/16_03/dipendenti.txt', 'r', encoding='utf-8') as f:
    contenuto = f.read()
#    risultato = processa(contento)
f.close() #chiamato automaticamente

#context manager multipli, in una sola riga
with (
    open ('C:/Users/dario/Desktop/corso_python/16_03/dipendenti.txt', 'r', encoding='utf-8') as src,
    open ('C:/Users/dario/Desktop/corso_python/16_03/dipendenti.txt', 'w', encoding='utf-8') as dst,
):
    dst.write(src.read().upper())
