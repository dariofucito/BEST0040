#gestione delle eccezioni (try/except/else/finally)

try:
    risultato = input("inserisci valore")
    
#except ZeroDivisionError:
 #   print("errore di divisione per 0")

except Exception as e:
    print(f"errore generico: {e}")
    print(type(e).__name__)
    
else:
   print(risultato)
   
finally:
    print("fine del programma")
    
    
    
# ValueError -> int("abc")
#TypeErroe -> "ciao" + 5
#KeyErrore -> dict con chiave inesistente
#IndexErrore -> list[50] si 10 elementi in lista
#AttributeErrore -> nome.uppperr
#FileNotFoundError -> file richiesto non è stato trovato