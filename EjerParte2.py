#60,62,32,80
#Ejer 60
import numpy as np
from numpy import random as rd

matriz = rd.randint(0,3,(2,2))
matriz2 = rd.randint(0,3,(2,2))
mulDiagonal = np.diag(np.dot(matriz, matriz2))

A = np.arange(10, dtype=np.int32)
ejer = "Ejercicio 60"

print('-'*len(ejer), ejer, '-'*len(ejer))
print("\nLa matriz A es:\n",matriz)
print("\nLa matriz B es:\n", matriz2)
print("\nLa diagonal de secundaria de la matriz resultante es:", mulDiagonal)

#Ejer 62
ejer = "Ejercicio 62"
D = np.random.randint(0,10,(5,5,3))
E = np.random.randint(0,10,(5,5))

print('-'*len(ejer), ejer, '-'*len(ejer))
print("\nLa matriz A es:\n",D)
print("La matriz B es:\n", E)
print("La matriz resultante es: \n", D*E[:,:,None])

#Ejer 32
ejer = "Ejercicio 32"
F = np.random.randint(0,5,(10))

print('-'*len(ejer), ejer, '-'*len(ejer))
print("\nEl vector generado es: \n",F)
F.sort()
print("\nEl vector ordenado es:\n",F)

#Ejer 80
ejer = "Ejercicio 80"
mayores = []

Z = np.arange(100)
print(Z) 
np.random.shuffle(Z) 
print(Z)
n = 5 

mayores = Z[np.argpartition(-Z,n)[:n]] 

print('-'*len(ejer), ejer, '-'*len(ejer))
print("\nEl array es: \n", Z)
print("Vector con elementos ḿayores: ", mayores)







