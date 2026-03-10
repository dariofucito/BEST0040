
#LISTE
vuota = []
numeri = [1,2,3,4]
mista = [1, "ciao", 2, True, None]
annidata = [[1,2],[3,4],[5,6]]

print(numeri)
print(numeri[0])
print(numeri[1])
print(numeri[-1])
print(numeri[-2])
print(numeri[1:3])

numeri[0] = 100
print(numeri)

numeri.append(6) #aggiunge il num 6
print(numeri)
numeri.insert(0,0) #inserisce
print(numeri)
numeri.extend([7,8,9])
print(numeri)
numeri.remove(100)
print(numeri)
elemento = numeri.pop()
print(elemento)
elemento = numeri.pop(5)
print(elemento)
print(numeri.index(3))
print(numeri.count(3))

numeri.reverse()
print(numeri)

print(len(numeri))
print(sum(numeri))
print(max(numeri))
print(min(numeri))

print(5 in numeri)


#TUPLE
singola = (42,)
rgb = (255,128,0)
punto = 3,4
print(type(punto).__name__)
print(rgb[0])
#UNPACKING
rosso, verde, blu = rgb
print(f"il rosso e': {rosso}, il blu e': {blu}")
#UNPACKING CON * (STARRED ASSIGNMENT)
primo, *resto = [1,2,3,4,5]
print(primo)
print(resto)
*inizio, ultimo = [1,2,3,4,5]
print(inizio)
print(ultimo)

#DIZIONARI
utente = {
    "nome": "Dario",
    "email": "dario.fucito",
    "attivo": True
}

print(utente)



print(utente["nome"])
print(utente.get("email"))
print(utente.get("telefono","33343"))

print(utente)
utente["nome"] = "Marco"
print(utente)

del utente["attivo"]
print("nome" in utente)

utente["lavoro"] = "it"
print(utente)

utente2 = dict(utente)
print(utente2)

utente3 = {
    **utente,
    "nome":"Luigi"
}

print(utente3)

#SET

numeri2 = {1,1,2,2,3,3,4,4}
set1 = set(numeri2)
print(set1)
set1.add(6) #aggiungere
print(set1)
set1.discard(1) #scarta, non da errore in caso di mananza di elemento richiesto
print(set1)
set1.remove(4) #rimuovi, rstituisce ERRORE se l'elemento richiesto non esiste
print(set1)
print(3 in set1)
#OPERAZIONI INSIEMISTICHE
a = {1,2,3,4,5}
b = {3,4,5,6,7}

print(a | b) #unione
print(a & b) #intersezione
print(a-b) #differenza
print(b-a) #differenza
print(a^b) #differenza di entrambi i set

#esempio reale
email_lista1 = {"alice.com","giovanni.com","mario.com"}
email_lista2 = {"giovanni.com", "sara.com"}

#chi si trova in entrambe le liste
print(email_lista1 & email_lista2)

#chi si trova nella lista 1 MA NON nella list 2
print(email_lista1 - email_lista2)
