#!/user/bin/python
# -*- coding: utf-8 -*-
"""osica_bruja.py"""

# Condicionales

peso = 50
peso_de_un_ganso = 5

if peso < peso_de_un_ganso:
	print "¡Es una bruja!" # NO HAY llaves, la indentación implica que está dentro de la función

elif peso > peso_de_un_ganso: # No "elsif"
	print "Ah, pues no lo es"

else:
	print "Pues a mí me convirtió en grillo... y mejoré"

# While

frase = "Romani ite domus"

i = 0

while i < 100:
	print frase
	i += 1

# Hay break, continue y pass (no hagas nada)

# Iterador for
# Es como el foreach de Perl

platos = ("plato1", "plato2", "plato3", "plato4", "plato5", "plato6", "postre") # Utilizamos una tupla, no una lista

for plato in platos:
	if plato != "postre":
		print "Monsieur se come el: "+plato
	else:
		print "BOOM"
