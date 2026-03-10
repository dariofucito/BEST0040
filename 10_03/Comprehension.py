
#con ciclo for:
quadrati = []
for x in range(10) :
    quadrati.append(x**2)

print(quadrati)

#con list comprehension:
cubi = [x**3 for x in range(10)]
print(cubi)

#con condizione
pari = [x**3 for x in range(10) if x % 2 ==0]
print(pari)

#trasformazioni di strighe
nomi = ["alice", "DARIO"]
nomi_puliti = [n.strip().capitalize() for n in nomi]
print(nomi_puliti)

#CON IF ED ELSE

valori = [1,-2,3,-4,-5]
assoluti = [x if x >= 0 else -x for x in valori]
assoluti2 = [abs(x) for x in valori]
print(assoluti) 
print(assoluti2)

#DICT E SET COMPREHENSION
lunghezze = {nome: len(nome)for nome in nomi}
print(lunghezze) 