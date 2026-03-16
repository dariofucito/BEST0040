from pathlib import Path
from collections import defaultdict, Counter
from contextlib import contextmanager
import re

Path('dati').mkdir(exist_ok=True)
Path('dati/app.log').write_text(LOG_CONTENT, encoding='utf-8')


def analizza_log(percorso):
    """Analizza un file di log, restituisce statistiche strutturate."""
    p = Path(percorso)
    if not p.exists():
        raise FileNotFoundError(f'File di log non trovato: {p.resolve()}')

    pattern = re.compile(
        r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)$'
    )

    stats = {
        'totale_righe': 0,
        'per_livello': Counter(),
        'errori': [],
        'prima_riga': None,
        'ultima_riga': None,
        'righe_non_parsabili': 0,
    }

    with open(p, 'r', encoding='utf-8', errors='replace') as f:
        for riga in f:
            riga = riga.strip()
            if not riga:
                continue
            stats['totale_righe'] += 1
            stats['ultima_riga'] = riga
            if stats['prima_riga'] is None:
                stats['prima_riga'] = riga

            m = pattern.match(riga)
            if m:
                ts, livello, messaggio = m.groups()
                stats['per_livello'][livello] += 1
                if livello == 'ERROR':
                    stats['errori'].append({'timestamp': ts, 'messaggio': messaggio})
            else:
                stats['righe_non_parsabili'] += 1

    return stats


if __name__ == '__main__':
    try:
        r = analizza_log('dati/app.log')
        print(f'Righe totali:  {r["totale_righe"]}')
        print(f'Distribuzione: {dict(r["per_livello"])}')
        print(f'Errori ({len(r["errori"])}):')
        for e in r['errori']:
            print(f'  [{e["timestamp"]}] {e["messaggio"]}')
        print(f'Prima riga: {r["prima_riga"][:60]}...')
        print(f'Ultima riga: {r["ultima_riga"][:60]}...')
    except FileNotFoundError as e:
        print(f'Errore: {e}')
