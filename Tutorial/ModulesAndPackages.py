#En programación un módulo es una pieza de software que tiene una funcionalidad específica.
#Cada módulo es un archivo que puede ser editado por separado

#En python los módulos son archivos .py el nombre del módulo es el nombre del archivo.
#Puede tener un set de funciones, clases o variables definidas e implementadas.

#Para importar la funcionalidad de otros módulos, utilizamos la palabra clave import
#La palabra clave from nos permite buscar en un archivo específicado.
from functions import sum_numbers

def main():
    print("La suma es %i" %sum_numbers(10,4))
    print('This is ModulesTutorial')

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

""" 
La primera vez que se ejecuta código en un módulo tras su importación, se genera un archio .pyc
Esto es un archivo python precompilado. Siempre que haya uno se cargará primero en lugar del archivo .py

Si se usa solo la palabra clave import, cada vez que querramos utilizar una función específica de ese módulo
deberemos específicar el nombre del módulo seguido por el nombre de la función que queremos ejecutar
EJ: draw.draw_game()
"""
#También es posible importar todos los objetos de un módulo.
"""
from draw import *
En este caso también podemos utilizar todos los nombres directamente.
"""

#Custom import names and conditionals for import.
"""
if visual_mode:
    #import draw_visual as draw
else:
    #import draw_textual as draw
"""

#Module initialization
#La primera que un modulo es cargado en un script, es inicializado ejecutando el código dentro una vez.
#Si otro módulo en el código importa el mismo módulo otra vez, no se cargará una segunda vez.
#Las variables locales actúan como un Singleton ya que solo se inicializan una vez.

#Extendiendo el Module Path
#Es posible decirle al interpreter que queremos que para importar, busque módulos en directorios adicionales

"""
PYTHONPATH=/foo python game.py
Este comando permitiría que se cargara game.py y además que fuera posible cargar módulos desde el directorio foo
"""
#La segunda manera es ejecutando la función sys.path.append antes de ejecutar una llamada al comando import
"""
sys.path.append("/foo")
"""
#Build in modules - https://docs.python.org/3/library/
#Cuando estas explorando módulos en Python las funciones dir y help son muy útiles.
#Utilizamos import para incluir el módulo, y luego dir para obtener una lista de todo el contenido.
#Utilizamos help para obtener información respecto del paquete.

#Cada paquete en Python es un directorio que DEBE tener un archivo especial llamado __init__.py
#Este archivo puede estar vacío y indica que ese directorio contiene es un paquete Python y puede ser importado 
#de la misma manera que un módulo.
#Por lo tanto en un directorio siempre debe haber un archivo __init__.py

#El archivo __init__.py también puede decidir que modulos del paquete se pueden exportar como API, mientras mantiene otros
#módulos internos, mediante la sobreescritura de la variable __all__

"""
__init__.py:
    __all__ = ["aModule"]
"""
