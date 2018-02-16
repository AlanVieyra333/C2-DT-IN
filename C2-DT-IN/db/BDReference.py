#!usr/bin/environ
#-*- coding: utf-8 -*-
import csv

class BDReferencia:

	def __init__(self, archivo):
		"""
			Este método sirve para inicializar un objeto de tipo BDReferencia

			Parámetros
			------------
			archivo : str
					Es el nombre del archivo del cual se desea analizar los datos
		"""
		self.lista = []
		self.analizados = []
		self.archivo = archivo

	def eliminarDuplicidades(self):
		"""
		 	Este método genera una nueva lista y analiza si sus elementos se encuentran duplicados

		 	Parámetros
		 	--------------
		 	lista : [] 

		 		Es una lista en el que están almacenados todos
		 		los elementos de una Base de Datos

			Regresa
			--------------

			[]

				Es una lista que almacena todos los elementos de una lista principal
				sin duplicidades
		"""
		self.analizados = []
		for key in self.lista:
			if key not in self.analizados:
				self.analizados.append(key)

	def abrirArchivo(self):
		"""
			Este método tiene como propósito abrir un archivo y generar una lista con todos los
			elementos de la base de datos de referencias


			Parámetros
			---------------

			archivo :  str
					Es el nombre del archivo que se desea abrir.
					TODO: Realizar una validación para verificar que se trate de una base de datos de CDT

			Regresa
			--------------

			[]

					Es una lista que contiene todos los elementos de la Base de Datos de Referencia
		"""
		with open(self.archivo, 'r+') as bdReference:
			reader = csv.reader(bdReference)
			reader.next()
			for referencia in reader:
				self.lista = self.lista + [referencia]

	def sobrescribirArchivo(self):
		"""
			Este método tiene como propósito sobrescribir un archivo de csv a partir de una lista con  el formato de 
			BD de CDT

			Parámetros
			-----------------
			referenciasSinDuplicidad : []

									Es una lista que contiene los elementos que se guardarán en el archivo
			archivo : str

					Es una cadena que tiene el nombre del archivo que se desea sobrescribir
		"""
		with open(self.archivo, 'w+') as archivoNuevo:
			archivoNuevo.write('idElemento,idElementoRef\n')
			for referencia in self.analizados:
				archivoNuevo.write('%s,%s\n' % (referencia[0], referencia[1]))

