from datetime import date
""" 
FUNCIONAL! 1.0.0f
	Notas: Principales problemas a la hora de escribir este codigo es la conversión de unidades, tener especial cuidado en la sumatoria de strings.
	Declarar las variables al principio, en caso de querer declararlas sin valor, escribir "", despues solo reemplazar el valor por cualquier clase de variable.
"""
_day = ""
_month = ""
_Year = ""
monthList = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
print("\nINICIO DEL PROGRAMA\n Este programa separa la fecha en 3 componentes básicos separados.")
variableDia=str(date.today()) #Este paso es vital, convertir el dato obtenido en string para luego separar sus elementos teniendo en cuenta el índice de tal string. 
#Esta parte es solo para comprobar que se haya hecho la conversión y que el resultado se pueda recorrer por su índice mediante un bucle for.
#print("\n La fecha actual es: " + variableDia) # printeamos todo el resultado.
#print("\n El largo del string es: " + str(len(variableDia))) # Comprobamos el length del string.
#print("\n El 3er valor de la fecha recibida es: " + variableDia[3]) # Sacamos el 3er valor del string.
cont =0 #ya que content guarda el objeto actual de la lista(si se recorre un string, en realidad se recorre su length)(Para valores numericos usar Range()) se necesita una variable fuera del bucle que pueda ser accedido, en este caso <cont> para saber en cuantas veces se ha ejecutado, seria como el valor i.
for content in variableDia:
	cont +=1 #Cont lo usamos para corroborar cuantas veces iteramos!!
	if cont < 5: #5 es el valor del string que corresponde a la separación entre el año y el mes.
		_Year += content
		pass
	elif cont > 5 and cont < 8: #8 es el valor del string que corresponde a la separación entre el mes y el dia.
		_month += content
		pass  
	if cont > 8:
		_day += content # content = variabledia[i] (recordando siempre que <i> va a ser <cont-1>)
		pass	
	"""print("El contador es: " + str(cont) + ". Y el contenido es: " + content + "\n")"""
cont2 = 0
_month = int(_month) #El anterior resultado es un string, lo comvertimos en int para para poder igualarlo a un número.
for x in monthList:	
	if cont2 == _month:
		_month = monthList[cont2]
		pass
	cont2 += 1
	pass
print("		El dia corriente es: " + _day)
print("		El mes corriente es: " + _month)
print("		El Año corriente es: " + _Year)
print("\n  -----------------------------FIN DEL PROGRAMA-------------------------------")