#Consider a 16x16 array, how to get the block­sum (block size is 4x4)?
import numpy as np
Z = np.ones((16,16))
print("Vector original (16x16)",Z)
k = 4
S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                                       np.arange(0, Z.shape[1], k), axis=1)
print("Vector final",S)
