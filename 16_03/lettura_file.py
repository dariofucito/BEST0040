import os
print(os.getcwd())

#METODO 1 
f= open('C:\\Users\\dario\\Desktop\\corso_python\\16_03\\dipendenti.txt', 'r', encoding= 'utf-8') #nome_cartella/nome_file
contenuto= f.read() #una stringa con tutti i newline
f.close() #OBBLIGATORIO
print(f"Letti {len(contenuto)} caratteri")

#METODO 2 readlines() ogni riga include \n
f= open('C:\\Users\\dario\\Desktop\\corso_python\\16_03\\dipendenti.txt', 'r', encoding= 'utf-8') #nome_cartella/nome_file
righe = f.readlines()
f.close()
print(righe[2])

#METODO 3 readline()
f= open('C:\\Users\\dario\\Desktop\\corso_python\\16_03\\dipendenti.txt', 'r', encoding= 'utf-8') #nome_cartella/nome_file
prima = f.readline()
seconda = f.readline()
f.close
print(prima)
print(seconda)

#METODO 4 iterazione diretta
with open('C:\\Users\\dario\\Desktop\\corso_python\\16_03\\dipendenti.txt', 'r', encoding= 'utf-8') as f: #nome_cartella/nome_file
    for riga in f:
        riga = riga.strip() #rimuovo gli spazi
        if not riga:
            continue
        nome, ruolo, team, stip = riga.split(',')
        print(f'{nome} | {ruolo} | {team} | {int(stip)}')
