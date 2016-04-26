#!/usr/bin/python
# -*- coding: utf-8 -*-

from att import *
#from att import Sector_Destino
from zona import zona
from Conexion import *

# lugar = "Costa del Este"
# # lugar = "Altos del Hipódromo"
# # destino="El Tecal"
# # # lugar = "El Tecal"
# destino="Costa del Este"
lugar = "Albrook"
destino ="24 de Diciembre"
camino=[]
def Precio(lugar, destino):
	precio= ""
	_sector_Origen  = Sector_Origen(lugar)
	_sector_Destino = Sector_Destino(destino) 

	# Sino es un Sector Origen
	if not _sector_Origen:
		# print ("El Origen no es un sector")
		_sector_Origen = zona(lugar)
	# Sino es un Sector Destino
	if not _sector_Destino:
		# print ("El Destino no es un Sector")
		_sector_Destino = zona(destino)

	camino = [_sector_Origen[1],_sector_Destino[1]]

	print ("Ir de "+lugar+" A "+destino)

	if _sector_Origen[0] == _sector_Destino[0]:
		tabla =  _sector_Origen[0]
		precio = str(DbPrecio_Sector(tabla,camino))
		print ("CUESTA S==> "+precio)
	elif _sector_Origen[0] == "zona" and _sector_Destino[0] !="zona" or _sector_Origen[0] !="zona" and _sector_Destino[0] == "zona":
		tabla = "ZONA-SEC"
		precio = str(DbPrecio_Sector(tabla,camino))
		print ("CUESTA Z==> "+precio)
	else:
		precio ="null"
		print (precio)
	return precio
