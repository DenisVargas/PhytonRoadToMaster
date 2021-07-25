#Para usar expresiones regulares, utilizamos:
import re

pattern = re.compile(r"\[(on|off)\]") #Ejemplo de patrón

print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

#Si guardamos el resultado en un objeto, podemos hacer cosillas con esto:
#TODO explorar más opciones de operaciones con el resultado de los matches.

#Serializacion+
#Python tiene un módulo de codificación y decodificación nativa de JSON
import json

#Básicamente hay 2 formas de tratar con JSON, usando un string, o usando una datastructure
#La datastructure son listas y diccionarios nativos de python que pueden ser utilizados para
#modificar dicha estructura. 
#El string es utilizado generalemente para comunicarse con otros programas.

#Para cargar data en forma de string a un objeto json utilizamos la funcion load()
json_string = "imagine this is a json string parsed from a file in disk"
json.loads(json_string)

#Para codificar una estructura de datos a JSON usamos la funcion "dumps"
json.dumps([1,2,3,"a","b","3"])

#Python también tiene métodos para serializar objetos Python de forma nativa
#Estas funciones son pickle y cPicke (siendo esta ultima, una alternativa mas rápida).

import pickle

resultString = pickle.dumps([1,2,3,"a","b","c"])

print(resultString) #Funciona de la misma manera que con JSON
