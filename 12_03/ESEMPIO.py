
#ESEMPIO PRATICO: COME MISURARE IL TEMPO DI ESECUZIONE
import time
import functools

def timer(funzione):
    @functools.wraps(funzione) #preserva nome e docstring della funzione originale
    def wrapper(*args, **kwargs):
        inizio = time.perf_counter()
        risultato = funzione(*args, **kwargs) 
        fine = time.perf_counter()
        print(f"{funzione.__name__} eseguita in {fine-inizio:.4f} secondi")
        return risultato
    return wrapper

@timer
def calcola_primes(n):
    """trovs tutti i numeri primi fino a n"""
    primes = []
    for num in range(2,n):
        if all(num % i !=0 for i in range (2, int(num**0.5)+1)):
            primes.append(num)
    return primes

risultato = calcola_primes(10000)

#decoratore con argomenti (decoratore di decoratore)

def ripeti(n_volte):
    def decoratore(funzione):
        @functools.wraps(funzione)
        def wrapper(*args, **kwargs):
            for _ in range (n_volte):
                funzione(*args, **kwargs)
        return wrapper
    return decoratore

@ripeti(3)


def stampa_ciao():
    print("ciao")
    
stampa_ciao()