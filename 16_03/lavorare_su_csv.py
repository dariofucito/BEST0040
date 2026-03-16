import csv
from collections import defaultdict
with open('c:/Users/dario/Desktop/corso_python/16_03/dati/dipendenti.csv','r',encoding='utf-8',newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f'colonne: {header}')
    for riga in reader:
        id_,nome,cog,ruolo,team,stip,data = riga
        print(f'{nome} {cog} - {ruolo} - {team} {int(stip):,}')
        
#csv.dictreader
with open('c:/Users/dario/Desktop/corso_python/16_03/dati/dipendenti.csv','r',encoding='utf-8',newline='') as f:
    reader = csv.DictReader(f)
    print(f'colonne: {reader.fieldnames}')
    dipendenti = list(reader)

    
print(f'Totale dipendenti: {len(dipendenti)}')
#filtrare i dati
tester = [d for d in dipendenti if d['team'] == 'Testing']
print(f'{[d["nome"] for d in tester]}')    

per_team = defaultdict(list)
for d in dipendenti: per_team[d['team']].append(d['nome'])
for team, nomi in sorted(per_team.items()):
    print(f'{team} : {nomi}')


