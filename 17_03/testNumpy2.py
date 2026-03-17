#NUMPY
import numpy as np
#RANDOM CON NUMPY
#generare array con valori randomici
#choice per estrarre valori e generare array
#data distribution con probabilità
#shuffle e permutation

from numpy import random

#per creare un numero random con limite 100
numero = random.randint(100)
#print(numero)

#per creare un array randomico di numeri con un limite massimo e una dimensione
arr = random.randint(100, size=(12))
#print(arr)
#si può anche generare a più dimensioni l'array
arr2D = random.randint(100, size=(3,5))
#print(arr2D)
#con rand il range è tra 0 e 1
arr = random.rand(7)
#print(arr)

#con choice viene scelto randomicamente un valore da un array numpy
arr = np.array([3,9,2,6,7,77,21,76,34,30])
valore_random = random.choice(arr)
#print(valore_random)

#si può anche generare un array da un altro con scelte randomiche
arr = np.array([3,9,2,6,7,77,21,76,34,30,87,95,64,11,72])
arrChoice = random.choice(arr, size=(100))
#print(arrChoice)

#si può anche decidere la probabilità con cui scegliere gli elementi
valori = np.array([10,20,30,40,50])
probabilita = np.array([0.3, 0.1, 0.2, 0.1, 0.3])
arrRandom = random.choice(valori, p=probabilita, size=(20))
print(arrRandom)

#mescolamenti degli elementi in maniera randomica
arr = np.array([1,2,3,4,5,6,7,8,9])
random.shuffle(arr)
print(arr)

arr1 = np.array([1,2,3,4,5,6,7,8,9])
arrMischiato = random.permutation(arr1)
print(arr1)
print(arrMischiato)

#UNIVERSAL FUNCTIONS (UFUNC)
#funzioni standard aritmetiche che operano sugli oggetti di tipo array numpy
#ufunc standard di numpy: add, subtract, multiply, divide, power, mod, trunc, ceil, floor

arr1 = np.array([10,20,30,40,50])
arr2 = np.array([5,10,15,20,25])

arrSommePosizionali = np.add(arr1, arr2)
print(arrSommePosizionali)

#in numpy è possibile creare delle ufunc custom per implementare una funzionalità che di base
#la libreria non ti offre da standard, la cosa comoda è che una volta definita la ufunc e registrata
#la si può utilizzare come una qualsiasi ufunc di numpy

#creo una ufunc che moltiplica un numero per 10
def multiply10(numero):
    return numero*10

#per poterla usare nel tuo progetto va registrata nel modulo numpy come universal function
#per registrarla bisogna dire il nome della function, quanti parametri ha in input e quanti
#parametri ha in output
multiply10 = np.frompyfunc(multiply10,1,1)

#test
arr_test_ufunc = np.array([1,2,3,4,5,6,7,8,9])
arr_per10 = multiply10(arr_test_ufunc)
print(arr_per10)

#ufunc matematiche
x = np.array([1.0, 4.0, 9.0, 16.0, 25.0])
print(np.sqrt(x))
print(np.square(x))

#ufunc con due argomenti (binary function)
a = np.array([3,6,2,8,1])
b = np.array([1,7,5,2,4])
print(np.maximum(a,b))

#metodi delle ufunc
#reduce() -> riduce l'array applicando la ufunc cumulativa
print("somma di tutti gli elementi: " , np.add.reduce(a))

print("somma di tutti gli elementi: " , np.add.accumulate(a))