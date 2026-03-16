

#set di dati iniziali
dipendenti = [
    ('Alice Rossi', 'developer', 'backend', 78001),
    ('Mario Verdi', 'tester', 'qa', 62000),
    ('Carlo Bianchi', 'analyst','data', 68000),
]

# scrittura delle newline
with open('C://Users/dario/Desktop/corso_python/16_03/output.txt', 'w', encoding='utf-8') as f:
    f.write('nome,ruolo,team,stipendio\n') 
    for nome, ruolo, team, stipendio in dipendenti:
        f.write(f'{nome}, {ruolo}, {team}, {stipendio}\n')

#lista di stringhe
righe = [f'{n}, {r},{t}, {s}\n' for n,r,t,s in dipendenti]
with open('C://Users/dario/Desktop/corso_python/16_03/output2.txt', 'w', encoding='utf-8') as f:
    f.writelines(righe)

#come formattare gli output
with open('C://Users/dario/Desktop/corso_python/16_03/output3_formattato.txt', 'w', encoding='utf-8') as f:
    print('=' * 58, file=f)
    print('   REPORT DIPENDENTI   ', file=f)
    print('=' * 58, file=f)
    for nome, ruolo, team, stipendio in dipendenti:
        f.write(f'{nome}, {ruolo}, {team}, {stipendio}\n')
        
        
nuovi = [
    ('Diana Neri', 'devops', 'infra', 74000)
]
with open('C://Users/dario/Desktop/corso_python/16_03/output2.txt', 'a', encoding='utf-8') as f:
    for n,r,t,s in nuovi:
        f.write(f'{n}, {r}, {t}, {s}\n')


#verifica, quante righe in un file?
with open('C://Users/dario/Desktop/corso_python/16_03/output2.txt', 'r', encoding='utf-8') as f:
    totale = 0
    for riga in f:
        totale +=1

print(f' righe totali: {totale}')