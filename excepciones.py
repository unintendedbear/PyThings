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


