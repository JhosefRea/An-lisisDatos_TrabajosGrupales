#58, 50, 45, 38, 99
import numpy as np;
print("Ejercicio 38\n Crear una matriz inmutable\n")
Z = np.zeros(10)
print (Z)
Z.flags.writeable = False
#Z[0]=1 presenta un error, es una matriz inmutable
print("Ejercicio 45 \n Cambiar de flotante de 32bits a Entero de 32bits\n")
A = np.arange(10, dtype=np.int32)
print("Arreglo entero")
print(A)
A= A.astype(np.float32, copy=False)
print("Arreglo flotante")
print(A)
print("\nEjercicio 50\nRestar la media de cada fila\n")
X = np.random.rand(5, 4)
print("Matriz original\n", X)
# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)
print("Matriz con la resta del promedio de cada fila\n", Y)
print("\nEjercicio 58\n Suma de ultimos ejes de una matriz 4*4\n")
B = np.random.randint(0,10,(3,4,3,4))
sum = B.reshape(B.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)

print("\nEjercicio 99\n Filas con numeros enteros \n")
X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                [2.0, 0.0, 1.0, 1.0],
                [1.5, 2.5, 1.0, 0.0]])
n = 4
M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
M &= (X.sum(axis=-1) == n)
print(X[M])