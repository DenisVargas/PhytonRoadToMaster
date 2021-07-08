#Son una alternativa a las Listas
#They are fast. Can perform calculations across entire arrays.

import numpy as np

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#Convertimos los array a NumpyArrays 
np_height = np.array(height)
np_weight = np.array(weight)

#Cálculos basados en elementos (?)
bmi = np_height / np_weight ** 2 #Esto debería ser bastante eficiente
#Básicamente cualquier operación sobre un numPyArray se realiza sobre todos los elementos.

print(bmi)

#For a boolean response
bmi > 23

#Only those who are above 23
bmi[bmi > 23]
