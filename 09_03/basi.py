from decimal import Decimal

#VARIABILI

x = 10 #intero
y = -25 
grande = 999_999_999
binario = 0b1010
esadecimale = 0xFF
pi = 3.14634334 #float
z = 3 + 4j #complex
print (z)
print (z.real, z.imag)

altezza = 1.82 #double
attivo = True #boolean


nome = "Dario" #stringa
nome2 = 'Giovanni' #stringa
nome3 = '''ciao''' #triple-quote (scrivere su più linee)
messaggio = '''
Ciao a tutti
benvenuti nel corso python
Giorno 1'''

#concatenazione 

completo = nome +" "+ nome2
print(completo)

#ripetizione
separatore = "-" *40
print(separatore)

#lunghezza
print(len(nome))
print(len("Buongiorno"))

#indicizzazione
print(nome[0])

#slicing
print(nome[0:3])
print(nome[1:3])
print(nome[1:])
print(nome[::-1])

#metodi delle stringhe

print("   ciao    ".strip()) #strip elimina gli spazi superflui
print("Dario Fucito".split()) #split divide
print("DARIO FUCITO".lower()) #minuscolo
print("dario fucito".upper()) # maiuscolo
print("dario rossi".replace("rossi","fucito")) #sostituisci
print("dario".startswith("fuc")) #comincia o finisce con (risposta in bool)
print("dario".endswith("io"))
print("!".join(["a", "b", "c"])) #unisci


#f-string BASE
print(f"mi chiamo {nome} e sono alto {altezza}")
print(f"mi chiamo {nome} e sono alto {altezza + 2}")

#formattazioni numeriche
print(f"in precentuale: {0.1234:.1%}")
print(f"separatore: {10457131131:,.0f}")

#padding e allineamento
print(f"{nome:>20}")
print(f"{nome:<20}")
print(f"{nome:^20}")

s=40
print(f"{s = }")

#assegnazioni multiple su una riga

a = b = c = 0 
x, y, z = 1, 2, 3

print(a,b,c)
print(x,y,z)

# precisione float
print(Decimal('0.1') + Decimal('0.2'))


# scambio di variabili

a, b = 1, 2
a, b = b, a
print(a,b)

#a1 # va bene
#1a # errore 



#operatori matematici
k, j = 10, 3
print(k+j)
print(k-j)
print(k*j)
print(k/j)
print(k//j)
print(k%j)
print(k**j)

#operatori di confronto
print (k==10)
print (k!=10)
print (k>10)
print (k<10)
print (1<k<7)

#operatori logici

t = True
f = False 
print(t and f) 
print(t or f) 
print(not t)


#conversioni
print(int("42")+5)
print(float("3.14"))
print(str(100))
print(bool(0))
print(bool("ciao"))
print(int(3.9))
print(round(3.9))

print(int("0xFF", 16))
print(int("1010", 2))
print(bin(16))
print(hex(16))

print(type(k))
print(type(k).__name__)
print(isinstance(k,(int,float)))

#nomeUtente # camel case (in java)
#nome_utente # snake_case (in python)
#PrimoUtente #PascalCase (java)




