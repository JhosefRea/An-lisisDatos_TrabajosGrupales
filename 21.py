#Create a custom dtype that describes a color as four unisgned bytes (RGBA)
import numpy as np

color= np.dtype([('R','u1'), ('G','u1'), ('B','u1'), ('A','u1')])
print(color)
