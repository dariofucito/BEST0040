from datetime import datetime

with open('C:/Users/dario/Desktop/corso_python/16_03/dipendenti.txt', 'r', encoding='utf-8') as f:
    righe = f.readlines()
    
header = righe[0].strip().split(',')
dati = righe[1:]

dipendenti = []

for riga in dati:
    campi = riga.strip().split(',')
    nome = campi[0]
    ruolo = campi[1]
    team = campi[2]
    dt_assunz = datetime.strptime(campi[3], '%Y-%m-%d')
    dt_nasc = datetime.strptime(campi[4], '%Y-%m-%d')
    stipendio = float(campi[5])
    
    dipendenti.append({
        'nome':nome,
        'ruolo' : ruolo,
        'team' : team,
        'dt_assunz' : dt_assunz,
        'dt_nasc': dt_nasc,
        'stipendio' : stipendio
    })
    
print(dipendenti)
