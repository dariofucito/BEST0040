#NUMPY
#pip install numpy
import numpy as np
print(np.__version__) #versione di numpy
print(np.__file__) #dove è installato numpy

#numpy è una libreria di python che si usa per utilizzare N-dimensional array (ndarray)
#gli array di numpy lavorano come le liste di python ma con velocità 10x-1000x superiori 
#oltretutto possiamo utilizzare molte funzioni che fanno operazioni complesse in maniera molto semplice

#dimostrazione pratica perchè numpy è più veloce
import time

N = 1_000_000

#metodo python puro
lista = list(range(N))
t0 = time.perf_counter()
risultato_lista = [x * 2 for x in lista]
t1 = time.perf_counter()
print(f'Lista Python:  {(t1-t0)*1000:.1f} ms')

#metodo con numpy
arr = np.arange(N)
t0 = time.perf_counter()
risultato_arr = arr * 2
t1 = time.perf_counter()
print(f'Array Numpy:  {(t1-t0)*1000:.1f} ms')

#creazione di un array di numpy
arr = np.array([1,2,3,4,5])
#operazioni matematiche su tutti gli elementi dell'array in maniera super semplice e veloce
print(arr+5)
print(arr*5)
#con le liste questo non puoi farlo

#si possono creare array di varie dimensioni
arr1D = np.array([1,2,3,4,5])
#matrice (array bidimensionale)
#attenzione che le due dimensioni devono avere la stessa shape (forma)
arr2D = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(arr2D)
#array 3D
arr3D = np.array([
                    [[1,2,3], [4,5,6]],
                    [[7,8,9], [10,11,12]]
                ])

print(arr3D)
#metodo semplice per sapere quante dimensioni ha un array
print(arr3D.ndim)

#posso anche creare velocemente un array di tot dimensioni (con tutti i valori a zero)
arrTest = np.array([2,3,3], ndmin=3)
print(arrTest)

#si può creare un array dandogli un range di inizio e fine(esclusa)
arr = np.arange(1,100) #100 è escluso
print(arr)
#mettendo un terzo parametro specifico gli step (i salti tra i numeri)
arr = np.arange(1,100,5)
print(arr)

#creare array con valori iniziali tutti uno o tutti zero con una lunghezza specifica
arr = np.zeros(5)
print(arr)
arr = np.ones(5)
print(arr)

#INDICIZAZZIONE DEGLI ARRAY DI NUMPY
#ricordarsi che l'indice parte da zero
arr3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,2]]])
print(arr3D[1,0,0])
print(arr3D[0,1,1])
arr1D = np.array([10,20,30,40])
print(arr1D[2])
arr2D = np.array([[5,15,25],[13,23,33],[66,99,88]])
print(arr2D[1,2])
#indicizzazione negativa
print(arr1D[-1])
print(arr3D[-1,-1,-2])

#SLICING DEGLI ARRAY, prendere degli elementi da un array usando gli indici
arr1D = np.array([1,2,3,4,5,6,7,8,9,10])
#da x a y con y escluso
arr = arr1D[0:2]
print(arr)
#posso anche prendere da un indice fino alla fine
arr = arr1D[4:]
print(arr)
#posso anche fare dall'inizio ad un punto
arr = arr1D[:3]
print(arr)
#si può ragionar anche con indici negativi
arr = arr1D[6:-2]
print(arr)
arr = arr1D[-3:1] #attenzione questo da array vuoto, sempre da sinistra verso destra
print(arr)
#posso anche mettere degli step di salto
arr = arr1D[1:7:2]
print(arr)

#TIPI DI DATO IN NUMPY
#documentazione: https://www.w3schools.com/python/numpy/numpy_data_types.asp

arrInt = np.array([1,2,3,4])
arrString = np.array(["ab", "b", "c"])
arrFloat = np.array([3.2, 6.7, 3.3])
arrBoolean = np.array([True, False, True])
arrMix = np.array(["a", 1, True])

print(arrInt.dtype)
print(arrString.dtype)
print(arrFloat.dtype)
print(arrBoolean.dtype)
print(arrMix.dtype)

#posso creare un array di un determinato tipo
#dtype che controlla il tipo di dato
arr = np.array([3,5,6,7,9,2], dtype='S')
print(arr.dtype)
print(arr)

#esiste un modo per converire un array in un altro tipo di dati
arrInt = arr.astype('i')
print(arrInt)

#VIEW E COPY
#copiare il contenuto di un array in un altro
#la differenza è che copy crea un altro array, view fa una vista alternativa sullo stesso array
arr = np.array([1,2,3])
copia = arr.copy()
arr[0] = 10
print(arr)
print(copia)

arr1 = np.array([1,2,3])
view = arr1.view()
arr1[0] = 20
print(arr1)
print(view)

print(copia.base)
print(view.base)

#SHAPE E RESHAPE (FORMA)
#ci consentono di mutare la forma(dimensionionalità) di un array
#shape -> ci dice la forma
#reshape -> può riformare un array
arr2D = np.array([[1,2,3], [4,5,6]])
print(arr2D.shape)
print(arr2D)
print(arr2D.reshape(-1))

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#da questo array creiamo un array bidimensionale dove nella prima dimensione
#abbiamo 4 elementi e nella seconda 3
print(arr.reshape(4,3))
#occhio che non tutte le reshape sono fattibili
print(arr.reshape(6,2))
#print(arr.reshape(5,4)) questo non funziona perchè il prodotto delle dimensioni deve
#essere la size dell'originale
print(arr.reshape(2,3,2))

#metodo velcoe per spianare l'array , flattening
arr3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3D.flatten())

#ITERAZIONE DEGLI ARRAY
arrIter1 = np.array([1,2,3,4,5,6,7])
arrIter2 = np.array([[1,2,3], [4,5,6]])

for x in arrIter1:
    print(x)
    
for y in arrIter2:
    for z in y:
        print(z)

#metodo più semplice e veloce di numpy per iterare array di qualsiasi dimensione in un solo passaggio
arrIter3 = np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print("-------------------------------")
for x in np.nditer(arrIter3):
    print(x)
    
#nditer si possono anche cambiare i tipi di dati di tutti gli elementi
print("-------------------------------")
for x in np.nditer(arrIter3, flags=['buffered'], op_dtypes='S'):
    print(x)
    
#iterare a step(slicing), vogliamo solo i dispari
for x in np.nditer(arrIter3[:,:,::2]):
    print(x)

#possiamo anche prendere tutti gli indice degli elementi ed elencarli
for index, x in np.ndenumerate(arrIter3):
    print(index, x)
    
#JOINING DEGLI ARRAY DI NUMPY (unione degli array)
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arrJoin = np.concatenate((arr1,arr2))
print(arrJoin)

#concatenazione 2D
arr3 = np.array([[1,2], [3,4]])
arr4 = np.array([[5,6], [7,8]])
arrJoin2 = np.concatenate((arr3,arr4), axis=1)
#con axis=0 da 2 array con dimensione (2,2) e (2,2) ha generato un array di (4,2)
#con axis=1 da 2 array con dimensione (2,2) e (2,2) ha generato un array di (2,4)
print(arrJoin2)

#DIVIDERE GLI ARRAY DI NUMPY
arr = np.array([1,2,3,4,5,6])
arrSplit = np.array_split(arr, 2)
print(arrSplit)
arrSplit = np.array_split(arr, 3)
print(arrSplit)
arrSplit = np.array_split(arr, 4)
print(arrSplit)

#test con array 2D
arr2D = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
#dimensione è (6,2)
#ha creato 3 array di dimensione (2,2)
arrSplit = np.array_split(arr2D,3)
print(arrSplit)

#RICERCHE, ORDINAMENTI, E FILTRAGGI CON ARRAY NUMPY
arrTest = np.array([1,4,7,56,21,78,23,12,67,89,34,67,21,22,78,90,23])
#voglio vedere dove si trova il numero 23
posizione23 = np.where(arrTest == 23)
print("Il numero 23 si trova al posto: ", posizione23)
#voglio sapere le posizioni dei numeri pari
postiPari = np.where(arrTest%2 == 0)
print("Le posizioni dei numeri pari sono: ", postiPari)

#ordiniamo l'array in ordine crescente
arrOrdinato = np.sort(arrTest)
#per ordinamento decrescente mettere dopo [::-1]
print(arrOrdinato)
print(arrTest)

arrNomi = np.array(["anna", "luca", "paolo", "Luca"])
arrOrd = np.sort(arrNomi)
print(arrOrd)

#ordinamento di array bidimensionali
#ordina nelle singola dimensioni
arrTest2D = np.array([[2,1,6,3], [8,4,2,5]])
arrOrd2D = np.sort(arrTest2D)
print(arrOrd2D)

#filtraggi su array
arrTestF = np.array([3,9,2,6,7,77,21,76,34,30])
filtro = (arrTestF%3 == 0)
arrFiltrato = arrTestF[filtro]
print(arrFiltrato)

