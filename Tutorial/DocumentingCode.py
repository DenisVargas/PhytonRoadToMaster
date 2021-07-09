#Documentar código en python no es muy complicado
#Python no necesita de programas externos para generar documentacion
#En vez de ello trabaja con comentarios. 
#Podemos ver el resultado directamente desde la consola de comandos
#Utilizando la función Help(módulo)
#Para salir de la documentación usamos q

#Mas info en https://codigofacilito.com/articulos/documentar_modulos_python

#Ejemplo de módulo documentado: utilizamos docstrings """

"""Documentación del módulo.
Esta es una anotación la cual debe de encontrarse
en la parte superior de nuestro script.
Esta anotación tiene cómo objetivo describir el módulo"""

__author__ = "Eduardo Ismael García Pérez"
__copyright__ = "Copyright 2017, CodigoFacilito"
__credits__ = ["CodigoFacilito", "Rafael Alvarez", "Luis Enrique"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Team CodigoFacilito"
__email__ = "eduardo @ codigofacilito.com"
__status__ = "Production"

def funcion_a():
  """Cómo sabemos podemos documentar una función de esta manera."""
  pass

def funcion_b():
  """Podemos
    colocar
    saltos de línea
  """
  pass

def funcion_c(a=0, b=0):
  """Podemos dar más detalles de los parámetro
    a -- parámetro (default 0)
    b -- parámetro (default 0)
  """
  pass

class MyModulo:
  """Documentación de nuestra clase"""

  def metodo(self):
    """Documentación de nuestro método"""
    pass