#Usa el interprete para testear comandos sin escribir un programa completo.
#Python es object oriented. no hace falta declarar el tipo ni declararlos por adelantado.
#Toda variable es un objeto.
#Variable types: number - integers and floating points

myint = 20
myfloat = 10.23
myExpresoFloat = float(20)
mystring = 'Can Use "" also'
mysecondstring = "Puedes usar estos para añadir let's estas"

#operaciones: + - * / **
suma = myint + myfloat
resta = myint - myfloat
mulAndDivide = (myint * myExpresoFloat) / myfloat
stringChaining = mystring + " " + mysecondstring
#El operador % (módulo) retorna el resto de una división
#Dos * hacen una potenciación

#Strings
#Se pueden concatenar usando el oprador +
helloworld = 'hello' + " "  + "world"
#Se pueden multiplicar para formar un string con una secuencia repetida.
hellos = 'hello' * 10


#Las asignaciones se pueden hacer en mas de uno a la vez
a, b = 1, 2 #No creo que sea buena idea usar esto.


#mezclar operaciones entre numeros y strings da error. typeError


#Listas!
myList = []
myList.append(1)
myList.append(2)
myList.append(3)
# print(myList[0])
#Se pueden combinar usando el operador +
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all = odd_numbers + even_numbers
#Igual que con strings, puedes usar el operador * para generar una secuencia repetida.
# print([1,2,3] * 10)


multiList = ['first','Second']

for i in myList:
    # print("Selected number is: " + i)
    print(i)
#Acceder a un indice que no sea válido nos dará un error
#IndexError: list index out of range


x = 1
if x == 1:
    #this is a comment
    print("This is hellow world madafakas.")