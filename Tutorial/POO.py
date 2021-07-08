# Objects are an encapsulation of variables and functions into a single entity.
# Objects get their variables and functions from classes.
# Classes are essentially a template to create your objects.

#Class Definition Example
class dog:
    patas = 4
    def ladrar(self):
        print("Wauf Wauf")

#Object Creation
jackoso = dog()

#memeber variable Accesing
print(jackoso.patas) #prints 4

#function calling
jackoso.ladrar() #prints wauf wauf

#https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/