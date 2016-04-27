#!/user/bin/python
# -*- coding: utf-8 -*-
"""osica_golondrina.py"""

class Osica:

	def __init__(self, velocidad, nombre): # Está reservado y SIEMPRE se hace así, sirve para iniciar la clase. La diferencia entre un método y una función es que el método lleva el self como primer argumento.

		self.nombre = nombre
		self.velocidad_max = float(velocidad)
		self.velocidad_actual = self.velocidad_max

	def andar(self, distancia):
		tiempo = str(distancia / self.velocidad_actual)
		print "La osica tarda "+tiempo+" horas"

	def coger_miel(self):
		print "La osica "+self.nombre+" coge miel"
		self.velocidad_actual = self.velocidad_max / 2

una_osica = Osica(2, "Paloma")  # El self se pasa de manera implícita

una_osica.andar(100)
una_osica.coger_miel()
una_osica.andar(100)

# Para heredar, hacemos Osica_Europea(Osica)
