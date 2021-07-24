#Nota: este archivo no esta pensado para ser ejecutado.

#File handling allows us to writte files in disk
#Hay 4 operaciones básicas que hay que tener en cuenta.
#Crear, Leer, Actualizar, Borrar archivos.

#La función mas importante es la funcion open()
#Toma 2 parámetros filename y mode

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

#Podemos específicar si el texto se debe tratar como binario o texto

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#La metodología es siempre la misma.
#1. Abrimos el archivo en el modo que nos sea mas conveniente utilizando la función open().
#2. Escribimos o leemos el archivo utilizando write, writelines, writelines / read, readline, readlines.
#3. Cerramos el archivo con la función close()

#Para que python lea un archivo, solo tenemos que especificar el nombre del archivo.
f = open("ReadText.txt") #Siempre y cuando el archivo este en el mismo directorio.
#El equivalente con todos los parámetros es el siguiente
# f = open("demofile.txt", "rt")
#la función open retorna un objeto file, que a su vez tiene una función read()
print(f.read()) #De esta forma podemos desplegar el contenido del texto.

#Ahora tenemos que tener en cuenta que pasa cuando el directorio es diferente de la carpeta raiz de python.
# f = open("D:\\myfiles\welcome.txt", "r") --> Donde la ruta debe ser específicada desde el directorio raiz.
# print(f.read())
#TODO: Ahondar esto en detalles.


#===========================================================================================================================
                                            #Reading Files
#===========================================================================================================================
#La función read puede recibir un parámetro que indica la cantidad de carácteres que queremos leer.
print(f.read(5))
#Si quieres leer una línea completa puedes utilizar la funcion readline()
print(f.readline())
#Llamar a la función varias veces, permite retornar una línea diferente en cada llamada.
file = open("demofile.txt", "r") #de esta forma puedes iterar a través del archivo hasta leer todas las líneas.
for line in file:
  print(line)
#Si queremos leer multiples lineas simultáneamente podemos utilizar la función readlines(números de líneas).

#Es una buena práctica cerrar los archivos cada vez que terminamos de hacer las operaciones en ellos.
f.close()

#===========================================================================================================================
                                            #Writting Files
#===========================================================================================================================
#Si lo que queremos es cambiar/crear un archivo, utilizamos la función Open utilizando los parámetros "a" o "w"
#Recordemos que "a" (append mode) añade el contenído al final de la página.
#Por otro lado "w" (write mode) sobreescribe todo el contenido del archivo.

f2 = open("demofile2.txt", "a")
f2.write("Now the file has more content!")
f2.close()

#open and read the file after the appending:
f2 = open("demofile2.txt", "r")
print(f2.read())

f2 = open("demofile3.txt", "w")
f2.write("Woops! I have deleted the content!")
f2.close()

#Las funciones write, writelines aceptan objetos iterables, así que podemos pasarle listas, tuplas, o sets de strings.
#Hay un par de cosas que hay que tener en cuenta cuando trabajamos con iterables.
#Primero que nada, si tratamos cada elemento como una línea debemos añadir el carácter de nueva línea
#Ejemplo:
lines = ["Esta es una primera línea","Esto debería ser una segunda línea"]
with open("Example.txt","w") as ftest:
    ftest.write('\n'.join(lines))


#open and read the file after the appending:
f2 = open("demofile3.txt", "r")
print(f.read())

#----------- Writting to UTF-8 ----------------
#Cuando los archivos que estamos abriendo tienen una codificación específica, por ejemplo. UTF-8
#debemos agregar un parametro encoding a la función open.
quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'
with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)

#===========================================================================================================================
                                        #Creating new files.
#===========================================================================================================================
#Si quieres crear nuevos archivos, seguimos usando la función open, sin embargo ahora podemos utilizar
#los modos "x", "a" o "w".
f3 = open("myfile.txt", "x") #Requerda que el modo create ("x") retorna un error si el archivo ya existe.

#===========================================================================================================================
                                        #Delete files
#===========================================================================================================================
#Para borrar archivos tenemos que trabajar con el módulo OS y utilizar su función os.remove()

import os
os.remove("demofile.txt")

#Ahora que savemos que existe el módulo OS, podemos contemplar otros casos.
#Como chequeamos si un archivo existe?
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#Si queremos eliminar la carpeta completa utilizamos os.rmdir()
#Ejemplo:
import os
os.rmdir("myfolder") #Solo es posible remover carpetas vacías ;D

#Aquí hay una sintaxis que es válida de utilizar 
with open('readme.txt', 'w') as f:
    f.write('readme')

#===========================================================================================================================
                                                #IO
#===========================================================================================================================
#IO allows us to ask for input from the user (input) and to display results.
import io
#It only works for standart IO (Command Line).
#Printing to the screen --> by using print()

#Keyboard input
#Para obtener data usamos dos funciones, input() o raw_input()
# str = raw_input("Escribe algo")
str = input("Please enter some data here")
print(str)
