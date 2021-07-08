# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.
#More about POO in general: https://www.wikiwand.com/es/Programaci%C3%B3n_orientada_a_objetos

#Class Definition Example
class dog:
    patas = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def ladrar(self):
        print("Wauf Wauf")

#Object Creation
jackoso = dog()

#memeber variable Accesing
print(jackoso.patas) #prints 4

#function calling
jackoso.ladrar() #prints wauf wauf

#https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/
#Python is multiparadigma, but everything is an object
#Clase es una entidad que define elementos de estado y comportamientos.
#Objeto es una concreción o instancia de una clase.
#A los """ se les llama Docstring
#Al constructor de la clase se lo construye utilizando def __init__(parámetros)
#Utilizamos self para referirse a la instancia misma (this)
#Al construir métodos siempre reserva el primer parámetro para la instancia misma.
#Es una convención Utilizar CamelCase para los nombres de clases. La primera palabra siempre esta en mayúsculas.

#Constructores.
# __init__(self...) es la función especial utilizada para los constructores.
#Solo se puede implementar un constructor.

#Atributos
#Solo tienen atributos o miembros que son parte del estado.
#Los atributos de datos no necesitan ser declarados previamente
#Un objeto los crea al asignarles un valor por primera vez

#Métodos
#Al llamar los métodos la referencia a la instancia correspondiente, se pasa automáticamente
#por lo que no es necesario indicarla a mano. La palabra clave self es una convención.
#Básicamente dentro de una clase, tenemos definida una función estática.
#Podemos llamar a la función desde la clase pasandole una referencia a una instancia específica
#O podemos llamar a la función desde una instancia ya inicializada.

#Atributos de clase vs Atributos de instancia
#Los atributos de clase son compartidos por todas las instancias de esa clase
#Los atributos de instancia son únicos para cada uno de los objetos de dicha clase
#Los atributos de clase se definen dentro del scope de la clase, pero fuera del constructor
#Para referenciar a un atributo de clase, se utiliza el nombre de la clase y la notación por .
#Al modificarse los cambios se reflejan en todas las instancias.
#Si modificamos un atributo de clase desde una instancia, lo que sucede, es que se crea una copia de dicho atributo
#dentro de la instancia!!

#Inheritance - Herencia
class flyingDog(dog): #Indicamos la clase de la que hereda utilizando ()
    alas = 2 #Atributo de clase (Estático)

    def __init__(self, name, color, isFlying): #Constructor
        super().__init__(name,color) #LLamada al constructor de la clase padre.
        self.isFlying = false

    def fly(self):
        self.isFlying = true

    def land(self):
        self.isFlying = false

#La función super() devuelve un objeto temporal que permite invocar los métodos de la clase padre.
#Recuerda que la clase hija puede referenciar a los atributos y métodos de la clase padre, pero no viceversa.
#Implícitamente todas las clases de Python heredan de la clase object

#isInstance() & isSubclass()
#Normalmente utilizamos type() para obtener el nombre de la clase a la que corresponde la referencia de un objeto.
#isInstance(objeto,clase) devuelve verdadero si un objeto es de una clase determinada o una de sus clases hijas.
#isSubclass(clase, claseinfo) comprueba la herencia de clases. Devuelve true en caso de que clase sea una subclase de claseinfo
#false en caso contrario. claseinfo puede ser una clase o una tupla de clases

#Herencia multiple
#Python soporta la herencia multiple :O
class A:
    def print_a(self):
        print('a')
class B:
    def print_b(self):
        print('b')

class C(A, B): #Aquí el objeto C hereda de A y B
    def print_c(self):
        print('c')
c = C()
c.print_a()
c.print_b()
c.print_c()

#Output
"""
a
b
c
"""

#Encapsulación
#En POO se refiere a reunir todos los elementos que forman parte de una misma entidad.
#Suele estar en conjunto con el principio de ocultación (atributos privados)

#Atributos Privados
#Por defecto todos los atributos son públicos.
#Para indicar que un atributo es privado, utilizamos la convención _name
#Un truco que se puede hacer es utilizar doble _
#Si intentamos acceder a una propiedad precedida por doble _ obtenemos un error
#Esto se debe a que Python substituye el nombre anteponiendo _nombreDeLaClase al nombre de la propiedad original.

#Polimorfismo
#Capacidad de una entidad de referenciar en tiempo de ejecución a instancias de diferentes clases.
class Perro:
    def sonido(self):
        print('Guauuuuu!!!')
class Gato:
    def sonido(self):
        print('Miaaauuuu!!!')
        
class Vaca:
    def sonido(self):
        print('Múuuuuuuu!!!')

def a_cantar(animales):
    for animal in animales:
        animal.sonido()
if __name__ == '__main__':
    perro = Perro()
    gato = Gato()
    gato_2 = Gato()
    vaca = Vaca()
    perro_2 = Perro()
    granja = [perro, gato, vaca, gato_2, perro_2]
    a_cantar(granja)

#Garbage Collection es parte del diseño OOP
#TODO: Investigar sobre el garbage Collector de Python
