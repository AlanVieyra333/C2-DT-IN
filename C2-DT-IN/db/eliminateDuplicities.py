#!usr/bin/environ
#-*- coding: utf-8 -*-

#Se importa la librería
from BDReference import BDReferencia

#Se declará una instancia para la BD de Mensajes
msgReference = BDReferencia('cdtDBMSGReference.csv')
#Se declará una instancia para la BD de Reglas de Negocio
brReference = BDReferencia('cdtDBBRReference.csv')

#Se abren los archivos
msgReference.abrirArchivo()
brReference.abrirArchivo()

#Se eliminan las duplicidades
msgReference.eliminarDuplicidades()
brReference.eliminarDuplicidades()

#Se sobreescriben los archivos
msgReference.sobrescribirArchivo()
brReference.sobrescribirArchivo()