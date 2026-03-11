#FUNZIONI

def nome_funzione(parametro1, parametro2):
    #Descrizione della funzione
    
    #corpo della funzione
    risultato = parametro1 + parametro2
    return risultato

#chiamata alla funzione


valore = nome_funzione(3,5)
print(valore)


#funzioni senza return
def saluta(nome):
    print(f"ciao, {nome}!")
    
saluta("Alice")

#Return anticipato - esce dalla funzione
def dividi_sicuro(a,b):
    if b==0:
        return None
    c=a/b
    return c

ris=dividi_sicuro(10,0)
print(ris)

#restituisce più valori
def min_max(lista):
    return min(lista), max(lista)

minimo, massimo = min_max([3,1,4,1,5,9,2,6])
print(f"il minimo: {minimo}, il massimo: {massimo}")


def calcola_iva(prezzo, aliquota=0.22):
    """
    Calcola il prezzo con IVA inclusa
    Args: ...
    Returns: ...
    Raises: ... ValueError
    """
    if prezzo <0:
        raise ValueError("Prezzo inferiore a 0")
    return prezzo * (1+aliquota)

help(calcola_iva)
print(calcola_iva.__doc__)

k=calcola_iva(5,0.33)
print(k)

def descrivi_persona(nome,eta,citta):
    print(f"{nome}, {eta} anni, da {citta}")

descrivi_persona("alice",30,"roma")
descrivi_persona(citta="Milano",eta=30,nome="Bob") #Keywords

descrivi_persona("Marco",citta="Torino", eta=28) #Keywords miste
# descrivi_persona(citta="Milano",30,nome="Bob") #ERRORE

#ARGOMENTI CON VALORI DI DEFAULT

def connetti(host, porta=5432, ssl=True, timeout=30):
    """
    Simulo una connessione al database
    Args: inserire host
    Returns: ...
    Raises: ...
    """
    print(f"Connessione a {host} : {porta} SSL={ssl} con timeout= {timeout} secondi")
    

connetti("localhost")
connetti("db.prod.com", 3306)
connetti("db.test.com", ssl=False, timeout=60)

#DEFINIZIONE DI VALORI DI FUNZIONE
#BAD DEFAULT VIENE CREATO UNA SOLA VOLTA

def aggiungi_a_lista_BAD(elemento, lista=[]):
    lista.append(elemento)
    return lista

print(aggiungi_a_lista_BAD(1))
print(aggiungi_a_lista_BAD(2))   
print(aggiungi_a_lista_BAD(3))   

#GOOD: usa None come default per creare la lista nel corpo

def aggiungi_a_lista_GOOD(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

print(aggiungi_a_lista_GOOD(1))
print(aggiungi_a_lista_GOOD(2))   
print(aggiungi_a_lista_GOOD(3))   

#forzare le keyword arguments con *

def crea_utente(nome, *, ruolo, attivo=True):
    print(f"{nome} - {ruolo} - {'attivo' if attivo else 'disabilitato'}")
    
crea_utente("Alice", ruolo= "admin")
crea_utente("Alice", ruolo= "admin", attivo=False)
#crea_utente("Alice", "admin") -> TypeError

#Forzare le posizionali con /
def calcola(x,y,/,operazione="somma"):
    # x e y DEVONO essere posizionali
    if operazione == "somma" : 
        c=x+y
    if operazione == "prodotto":
        c=x*y
    print(f" il risultato e' {c}")
    
calcola(3,4, operazione="prodotto")
#calcola(6,7, operazione="sottrazione")

    
# *args e **kwargs

def somma(*args):
    """somma un numero qualsiasi di valori"""
    print(f"args ricevuti: {args}")
    return sum(args)

print(somma(1,2,3))
print(somma(10,20,44,77))

#misto: parametri fissi + *args

def log(livello, *messaggi):
    for msg in messaggi:
        print(f"[{livello.upper()}] {msg}")
        
log("info", "Server avviato", "Porta 8080", "SSL abilitato")

def crea_profilo(**kwargs):
    """crea un profilo con qualsiasi attributo"""
    print(f"kwargs ricevuti: {kwargs}")
    for chiave, valore in kwargs.items():
        print(f"{chiave}:{valore}")
        
        
crea_profilo(nome="Alice", eta=30, ruolo="Analyst")
crea_profilo(nome="Marco", eta=42, team="Backend")

#ESEMPIO COMPLETO

def funzione_completa(obbligatorio, *args, keyword_only="default",**kwargs):
    print(f"obbligatorio: {obbligatorio}")
    print(f"args: {args}")
    print(f"keyword_only: {keyword_only}")
    print(f"kwarg: {kwargs}")
    
funzione_completa("primo","secondo","terzo",keyword_only="ciao",extra1="valore1", extra2="valore2")


