#!/user/bin/python
# -*- coding: utf-8 -*-
"""excepciones.py"""

dividendo = 3
divisor = 0

# En try lo intenta en un entorno controlado

try:
	resultado = dividendo/divisor
	print "Resultado: "+str(resultado)

# Si lo de antes falla, hace lo que pongamos en except

except:
	print "No se puede hacer"

# De otra manera:

dividendo2 = "A"
divisor2 = 2

try:
	resultado2 = dividendo2/divisor2

except ZeroDivisionError:
	if divisor == 0:
		print "No se puede hacer"

except TypeError:
	print "Eso no es un numero"

else: # Se ejecuta si no ha habido error en el try
	print "Resultado2: "+str(resultado2)
