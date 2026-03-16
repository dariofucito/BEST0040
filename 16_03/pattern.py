
#pattern 1:
def cerca_nel_log(ppercorso, pattern='ERROR'):
    trovati = []
    with open('percorso','r', encoding='utf-8', errors='replace') as f:
        for n, riga in enumerate(f ,1):
            if pattern in riga:
                trovati.append((n, riga))
    return trovati

#pattern 2

for n, riga in enumerate(f, 1):
    if pattern in riga:
        yield n, riga
            