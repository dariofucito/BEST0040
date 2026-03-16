import xml.etree.ElementTree as ET
tree = ET.parse('c:/Users/dario/Desktop/corso_python/16_03/dati/dipendenti.xml')
root = tree.getroot() #elemento radice <azienda>

print(f' azienda: {root.get("nome")}')
print(f' anno: {root.get("anno")}')
print(f' tag: {root.get("tag")}')

for dip in root: 
    print(f'Dipartimento: {dip.get("nome")} (id={dip.get("id")})')
    
primo_dip = root.find('dipartimento')
primo_emp = root.find('dipartimento/dipendente')
print(f'primo dipendente: {primo_emp.find("nome").text}')

for d in root.findall('dipartimento/dipendente'):
    id = d.get('id')
    nome = d.find('nome').text
    ruolo = d.find('ruolo').text
    stip = d.find('stipendio').text
    print(f'[{id}] - {nome} - {ruolo} - {stip}')
    
tutte_skills = {s.text for s in root.iter('skill')}
print(f'\nSkill uniche: {sorted(tutte_skills)}')

skill_target = 'Java'
con_python = []
for d in root.findall('dipartimento/dipendente'):
    skills = [s.text for s in d.findall('skills/skill')]
    if skill_target in skills:
        con_python.append(d.find('nome').text)
print(f'con {skill_target}: {con_python}')