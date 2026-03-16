#context_manager_classe.py
class GestoreRisorsa:
    """context manager, mostra il flusso"""
    
    def __init__(self, nome):
        self._nome = nome
        
    def __enter__(self, nome):
        """chiamata all'inizio del with, valore restituito = 'as'"""
        print(f'[__enter__] acquisco : {self._nome}')
        return self
    
    def __exit__(self, exc_type, exc, tb):
        print(f'[__exit__] Rilascio: {self._nome}')
        if exc_type:
            print(f'[__exit__] Eccezione: {exc_type} : {exc}')
        return False
    
with GestoreRisorsa('database') as r:
    print(f'[uso] {r._nome}')

try: 
    with GestoreRisorsa('database') as r:
        raise ValueError('Simulazione di errore')

except ValueError:
    print('Eccezione gestita esternamente')
    