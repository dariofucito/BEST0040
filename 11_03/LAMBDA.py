
#LAMBDA
# def quadrato1 : return x**2 ->ERRATO

quadrato2 = lambda x:x**2
print(quadrato2(5))

somma = lambda a,b:a+b
print(somma(5,7)) 

saluta = lambda nome, prefisso="Ciao": f"{prefisso}, {nome}"
print(saluta("Mario"))

#argomento a funzioni higher-order

persone= [
    {"nome": "Mario", "eta":38},
    {"nome": "Giovanni", "eta":30},
    {"nome": "Marco", "eta":37},
]

print(persone)

per_eta=sorted(persone, key=lambda p:p["eta"])
print([p["nome"]for p in per_eta])

#ordinare per lunghezza del nome, poi alfabeticamente
parole=["banana","mela","ananas","kiwi","pera"]
ordinate= sorted(parole,key=lambda p: (len(p),p))
print(ordinate)

#map() - applicare una funzione ad ogni elemento
numeri=[1,2,3,4,5]
quadrati= list(map(lambda x:x**2,numeri))
print(quadrati)
# [x**2 for x in numeri] -> alternativa con comprehension

#filter() con lambda
pari=list(filter(lambda x: x%2==0, numeri))
print(pari)

