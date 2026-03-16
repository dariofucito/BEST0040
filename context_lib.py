from contextlib import contextmanager, suppress
import time, shutil
from pathlib import Path
import json

@contextmanager
def timer(nome='operazione'):
    inizio = time.perf_counter()
    try:
        yield
    finally:
        durata = time.perf_counter()
        print(f'[TIMER] {nome} : {durata:.4f}s')
        
with timer('caricamento dati'):
    numeri = list(range(1000))
    
@contextmanager
def dir_temp(percorso):
    p = Path(percorso)
    p.mkdir(parents=True, exist_ok=True)
    try:
        yield p
    finally:
        print("esecuzione non riuscita")
       # shutil.rmtree(p, ignore_errors=True)
        
with dir_temp('C:/Users/dario/Desktop/corso_python/16_03/tmp') as tmp:
    (tmp / 'step1.txt').write_text(json.dumps(numeri),encoding='utf-8')
    print(f'file creato in {tmp}')
    