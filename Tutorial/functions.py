#Python uses blocks, wich are formated area of code
# block_head:
#     1st blockLine
#     2nd blockLine
#     ...

#Para declarar una función utilizamos la palabra clave def
def my_function():
    print("This is a function example")

#Puede recibir argumentos y retornar un valor utilizando la palabra clave return.
#Nota que los argumentos solo requieren un nombre.
def sum_numbers(a, b):
    return a + b

#Calling a funtion
sum_numbers(2,6)

# PASS keyword.
# Es usado como placeholder para código futuro. Al ejecutarse no pasa nada, pero no te tiran error.
# El código vacío no es permitido en loops, definiciones de clase y de funciones, o en sentencias if
# https://www.w3schools.com/python/ref_keyword_pass.asp

#Hay una forma de crear funciones con una cantidad de parámetros no específicada usando la siguiente notación
def multiple_Parameter_Function(first, second, *everythingElse):
    print(list(everythingElse))
#Anteponiendo * al nombre de la variable podemos hacer un placeholder para una cantidad indefinida de parámetros.

#Es posible obtener los parámetros por clave
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))