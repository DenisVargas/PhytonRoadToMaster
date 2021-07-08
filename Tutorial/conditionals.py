# Básicamente boolanos
# if [condition] :
# Utiliza operadores para construir expresiones mas complejas.
# los operadores comunes son and, or, in, is, not

#Ejemplo.
x = 10 
if x != 3 and x > 5:
    print("This is an example")

#Ejemplo Completo:
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

#Empty objects:
# empty string --> ""
# empty list --> []
# number zero --> 0
# false

#IN operator
# utilizado para chequear que un objeto específico existe dentro de un contenedor iterable
name = 'john'
if name in ["John","Rick"]:
    print("Your name is either John or Rick")

#IS operator
# a diferencia del operador == (equals) el operador is compara las instancias en sí. vs el valor en el caso de el operador equals.
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#NOT operator
# invierte la expresión.