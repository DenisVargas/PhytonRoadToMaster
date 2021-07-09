#Los generadores son utilizados para retornar un set de objetos iterables
#de a uno a la vez de una manera especial.
#Cuando utilizamos un for sobre un set de items el generador es activado. 
#Al alcanzarse una sentencia yield, la ejecución del generador es detenida y el control es devuelto 
# al loop, retornando un valor. La función generadora puede generar valores infinitos .

import random

def lottery():
    #retorna 6 numeros entre 1 y 40
    for i in range(6):
        yield random.randint(1,40)

    #returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print("And the next number is... %d!" %(random_number))


#Example of fibonacci series generator:

# # fill in this function
# def fib():
#     pass #this is a null statement which does nothing when executed, useful as a placeholder.
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, (a + b)
#Looks like python suports a way of attribute swap

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
#Podemos usar for para iterar sobre un generador, o una colección.