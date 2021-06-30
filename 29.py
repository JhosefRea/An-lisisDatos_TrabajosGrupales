#Create a 5x5 matrix with row values ranging from 0 to 4
import numpy as np
row=[0,1,2,3,4]
pila=[]
for i in range (5):
    pila.append(row)
matrix=np.reshape(pila,(5,5))


print(matrix)
