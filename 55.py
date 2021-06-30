# Consider a given vector, how to add 1 to each element indexed by a second
#vector (be careful with repeated indices)?
import numpy as np
a = np.ones(20)
print("Primer vector",a)
b = np.random.randint(1,len(a),30)
print("Segundo vector",b)
np.add.at(a, b, 1)
print("Vector final",a)
