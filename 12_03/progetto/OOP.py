from abc import ABC, abstractmethod

#DEFINIZIONE DI UNA CLASSE
class Persona:
    """Rappresenta una persona con nome, cognome e età"""
    contatore_istanze = 0
    #attributo di classe - condiviso tra tutte le istanze
    def __init__(self, nome, cognome, eta):
        """inizializza una nuova istanza di Persona"""
        self._nome = nome
        self._cognome = cognome
        self._eta = eta
        Persona.contatore_istanze +=1
        
    def nome_completo(self):
        """Restituisce il nome completo"""
        return f"{self._nome} {self._cognome} {self._eta}"
    
    def saluta(self, altra_persona=None):
        if altra_persona:
            return f"ciao {altra_persona._nome}, sono {self._nome}"
        
    def compleanno(self):
        """incrementa età"""
        self._eta +=1
        print(f"{self._nome} ora ha {self._eta} anni")
        
    @classmethod
    def quante_persone(cls):
        return f"Istanze create: {cls.contatore_istanze}"
    
    
#creazione di istanze
p1 = Persona("Alice","Rossi",30)
p2 = Persona("Giovanni", "Verdi",40)

#accesso ad attributi e metodi
print(p1._nome)
print(p1.nome_completo())
print(p1.saluta(p2))
print(Persona.quante_persone())
p1.compleanno()
print(p1.nome_completo())


#EREDITARIETà E POLIMORFISMO
#Classe genitore
class Veicolo:
    def __init__(self,marca,modello,anno):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        
    def info(self):
        return f"{self._marca} {self._modello} {self._anno}" 
    
#classe figlio
class Auto(Veicolo):
    def __init__(self,marca,modello,anno, n_porte):
        super().__init__(marca,modello, anno) #richiamare init padre
        self._n_porte = n_porte #attributo specifico di AUTO
        
    def info(self): #OVERRIDE DEL METODO
        return f"{super().info()} - {self._n_porte}"
    
    def apri_bagagliaio(self):
        return f"Bagagliaio di {self._marca} aperto"
    

#classe figlio 2
class Moto(Veicolo):
    def __init__(self,marca,modello,anno, tipo):
        super().__init__(marca,modello, anno) #richiamare init padre
        self._tipo = tipo #attributo specifico di MOTO
        
    def info(self): #OVERRIDE DEL METODO
        return f"{super().info()} - {self._tipo}"
    
    def impenna(self):
        return f"la moto {self._marca} ha impennato"
    

#USO
auto = Auto("Fiat","500",2022,3)
moto = Moto("Ducati","Monster",2023,"naked")

print(auto.info())
print(moto.info())
         
#POLIMORFISMO
veicoli = [auto,moto,Veicolo("bici","City",2021)]
for v in veicoli:
    print(f"{v}: {v.info()}")
    
    
    
class Auto(ABC):
    """INTERFACCIA"""