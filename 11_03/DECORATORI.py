
#decoratori di base
def saluta():
    return "ciao"

mia_funzione = saluta
print((mia_funzione))
print(mia_funzione())
print(type(mia_funzione))
print(type(mia_funzione()))

def esegui(funzione):
    return funzione()

print(esegui(saluta))

#restituire una funzione da un'altra funzione (closure)
def crea_moltiplicatore(n):
    def moltiplica(x):
        return x*n #n è catturata dalla closure
    return moltiplica #restituire la funzione, NON IL RISULTATO

doppio = crea_moltiplicatore(2)
triplo = crea_moltiplicatore(3)

print(doppio(5))
print(triplo(5))

#struttura di un decoratore

def mio_decoratore(funziona_originale):
    def wrapper(*args,**kwargs):
        print("[PRIMA] della funzione")
        risultato= funziona_originale(*args, **kwargs)
        print("[DOPO] della funzione")
        return risultato
    return wrapper

def saluta2(nome):
    print(f"Ciao, {nome}")
    
saluta2_decorata = mio_decoratore(saluta2)("Giovanni")
#saluta2_decorata ("Mario")
saluta2("Marco")

