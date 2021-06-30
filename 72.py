#Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an
#array R = [[1,2,3,4], [2,3,4,5], [3,4,5,6], ..., [11,12,13,14]]?
import numpy as np
Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print("Arreglo de entrada",Z)
mat=np.empty(0)
for i in range(len(Z)-3):
    aux=Z[i:i+4]
    mat=np.concatenate((mat,aux), axis=0)
matriz=np.reshape(mat,(11,4))
print("Arreglo de salida\n",matriz)
