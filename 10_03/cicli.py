#CICLI
#IF
x=15

if x>20:
    print("x e' maggiore di 20")
elif x==15:
    print ("x e' uguale a 15")
else:
    print("x e' minore di 20")
    
#condizioni composte
eta = 25
ha_patente = True
if eta >=18 and ha_patente:
    print("puo' guidare")
elif eta < 16 or eta > 65:
    print("fascia eta' speciale")

#annidamento
voto = 55
if voto >=90:
    giudizio="ottimo"
elif voto >=75:
    giudizio="Buono"
elif voto >=60:
    giudizio= "Sufficiente"
else:
    giudizio = "insufficiente"
print(giudizio)

#match/case
comando = "star"
match comando:
    case "start":
        print("avvio")
    case "stop":
        print("fermo")
    case "pause":
        print("pausa")
    case _: #default
        print("comando non valido")
        
#FOR
for i in range (10,0,-1): 
    print(i, end= " ")
    
    
frutti = ["mela","pera","kiwi"]
for frutto in frutti:
    print(frutto)
    
print(frutti)

for i,frutto in enumerate(frutti):
   print(f"{i+1} : {frutto}")
    
#iterazione parallela su più sequenze
nomi = ["Dario","Carlo","Mario","Marco"]
voti = [88,75,92]
for nome, voto in zip(nomi, voti):
    print(f"{nome}: {voto}")
    
#iterazione su dizionario
persona = {"nome": "Alice", "eta":30, "citta": "Roma"}
for chiave, valore in persona.items():
    print(f"{chiave}: {valore}")

# Break - Continue
for i in range(10) : 
    if i==5:
        break
    print(i)
    
for i in range(4,7) : 
    if i==5:
        continue
    print(i)

#WHILE
contatore = 0
while contatore <5:
    print (contatore)
    contatore += 1
    
risposta = ""
while True:
    risposta = input("inserisci si per continuare : ")
    if risposta =="si":
        break
    print("risposta non valida")
    
