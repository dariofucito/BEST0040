#gestione dei path
from pathlib import Path

p1 = Path('./dipendenti.txt')
p2 = Path('C:/Users/dario/Desktop/corso_python/16_03/')
p3 = Path.cwd()
p4 = Path.home()

file_csv = p3 / 'output.txt'

print(p2.name)
print(p2.stem)
print(p2.suffix)
print(p2.suffixes)
print(p2.parent)
print(p2.parents)
print(p2.parts)
print(p2.exists())
print(p2.is_file())
print(p2.is_dir())