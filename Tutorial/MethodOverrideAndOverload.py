#---------------------------------------------------------------
#                   Method Overriding
#---------------------------------------------------------------
# Es cuando un objeto hijo reimplementa una función del padre.
# Es tan simple como reescribirlo en el hijo.
# https://www.geeksforgeeks.org/method-overriding-in-python/

#Ejemplo
class parent:
    def __init__(self): #Constructor
        print("parent class constructed")

    def saySomething():
        print("i want to speak but i cant")

#Children Class
class children (parent):
    def __init__(self, message):
        super().__init__()
        self.message = message
    
    def saySomething(self): #This is Overriding
        print(self.message)

# if __name__=='__main__':
#     childObject = children("Hello nigga")
#     childObject.saySomething()
# This is a execution test
# childOBject = children("Hello beasts")
# childOBject.saySomething()



#---------------------------------------------------------------
#                       Method Overloading
#---------------------------------------------------------------
# Esto es algo que nos permite tener un solo nombre para una función, pero multiples implementaciones para
# Distintas cantidades y tipos de parámetros.
# https://www.educba.com/function-overloading-in-python/

#Primer Ejemplo
# def sumNumbers(a,b):
#     return a +  b

# def sumNumbers(a,b,c): #Esta definición sobreescribe la primera.
#     return a + b + c

# def printResult():
#     # result = sumNumbers(1,2,3)
#     result = sumNumbers(1,2)
#     print(result)

# printResult() #Esto da error: TypeError: sumNumbers() missing 1 required positional argument: 'c'

#Una solución es usar arguments.
# def add(datatype, *args):
#     if datatype =='int':
#         answer = 0
    
#     if datatype =='str':
#         answer =''

#     for x in args:
#         answer = answer + x
    
#     print(answer)

# #Integer
# add('int', 5, 6)
# #String
# add('str','HI','Mark')
#En el ejemplo de arriba, utilizamos strings y args, pero no es muy eficiente.

#Utilizar MultipleDispatch con Pip3
#pip3 es para python lo que npm es para Javascript
#Mas info aquí: https://monsterhost.com/what-is-pip-and-how-to-install-pip3/
#Comando es: pip3 install multipledispatch

# from multipledipatch import dispatch #Esto requiere tener instalado multipledispatch

# #pasar un parámetro
# @dispatch(int, int)
# def product(first,second):
#     result = first*second
#     print(result)    

# #Dos parámetros
# @dispatch(int,int,int)
# def product(first, second, third):
#     result = first*second*third
#     print(result)

# #Cualquier tipo de dato es válido
# @dispatch(float,float,float)
# def product(first, second, third):
#     result = first*second*third
#     print(result)

# product(2,3,2)
# product(2.2,3.4,2.3)
#source: https://www.geeksforgeeks.org/python-method-overloading/

#Otra forma mas es utilizar una clase y valores pre-definidos.
# class Compute:
#     def area(self, x=None, y=None):
#         if x!=None and y !=None:
#             return x*y
#         elif x!=None:
#             return x*x
#         else:
#             return 0

# obj = Compute()
# print(obj.area())
# print(obj.area(6))
# print(obj.area(2,8))
#Source: https://www.educba.com/function-overloading-in-python/

#Finalmente la ultima cosa que podemos hacer es usar el patrón decorator.
# Pero esto es complicadete, hay cosas que no entiendo...
# https://medium.com/practo-engineering/function-overloading-in-python-94a8b10d1e08