#Los diccionarios son un tipo de dato similar a los arreglos pero trabaja con claves en vez de indices.
#Cada valor se accede utilizando una clave que puede ser de cualquier tipo de dato.

#Examples of Dictionaries
phonebook = {} #Declaracion
phonebook["John"] = 938477566 #Asignación
phonebook["Jack"] = 938377264 #Asignación
phonebook["Jill"] = 947662781 #Asignación
print(phonebook) #Prints {'Jill': 947662781, 'John': 938477566, 'Jack': 938377264}

#Alternativa de declaracion y asignación
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook) #prints {'Jill': 947662781, 'John': 938477566, 'Jack': 938377264}

#Para acceder a un objeto usamos la clave
print(phonebook["Jill"])

#Para remover elementos usamos la palabra clave "del" o la funcion miembro .pop(key)
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}

del phonebook["John"]
phonebook.pop("Jill")
print(phonebook)

#Iterar sobre un diccionario
phonebook2 = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook2.items():
    print("Phone number of %s is %d" % (name, number))