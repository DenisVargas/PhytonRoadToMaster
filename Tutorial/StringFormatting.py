#Python utiliza un estilo C para formatear texto...

name = "john"
print("Hello %s!" % name)

#para especificar multiples, usamos tuplas
age = 20
print("%s is %d years old." % (name, age))

#El operador %s tambien se puede usar para otros objetos que no sean strings
#Especificadores básicos.
# %s - String (soporta auto formateo)
# %d - Integers
# %f - floats
# %.<numero de dígitos>f - floats con un límite de decimales
# %x/%X - Integers in hex (lowerCase o UpperCase)

#Basic String Operations
#usa len(string) para obtener el tamaño de un string.
#usa .index(char) sobre un string para obtener el índice de la primera aparición de la letra o
#usa .count(char) para contar cuantas veces aparece un caractér en un string determinado
#usa [startIndex:finishIndex] para consumir una porción de un string
#Si dejas un solo índice, obtienes el caracter en ese índice.
#Si dejas los dos puntos e ignoras el segundo, obtienes el resto del string partiendo del primer indice
#Si dejas los dos puntos e ignoras el primero, obtienes todas las letras del string hasta [finishIndex]
#Es válido utilizar numeros negativos. Es una forma de empezar al final y no al principio.
#Extended Slice Syntax -> [start:stop:step]
#Permite obtener todas los caracteres desde un indice inicial hasta un final, saltando un número de caracteres en el medio
#Para revertir un string podemos usar [::-1]
#Usa .upper() y .lower() para convertir a mayúsculas o minúsculas respectivamente.
# .startswith() y endswith() retornan verdadero o falso, dependiendo del caso
# .slipt(char) permite dividir un string en una lista utilizando un caracter como separador.