#Moduli, Pacchetti, Namespace e Scope

#1. Import del modulo intero (raccomandato)
import math

#2 import selettivo 
from math import sqrt, pi, factorial

#3 import con alias
import datetime as dt

#SCONSIGLIATO 
#from math import *

#PACKAGE

#mio_progetto/
#--__init__.py
#--matematica.py
#--strumenti.py
#--sottopackage/
#----__init__.py
#----geometria.py

#NAMESPACE E SCOPE, LA REGOLA LEGB
#Local 
#Enclosing (closure)
#Global
#Built-in

#Dimostrazione LEGB

x="globale" #G - LIVELLO GLOBALE

def esterna():
    x = "esterna" #E- Enclosing
    def interna():
        x="locale" #L - Locale rispetto ad interna()
        print(f"interna : {x}")
    interna()
    print(f"esterna: {x}")
esterna()
print(f"globale: {x}")

