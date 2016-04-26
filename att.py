#!/usr/bin/python
# -*- coding: utf-8 -*-
from Conexion import DbPrecio_Sector
Sectores ={	
	"Sector_A":{
		"N":["Condado del Rey","Los Andes N° 1", "Pan de Azucar","9 de Enero","Fátima","El Martillo","El Cristo"]
		,"S":["Santa Clara","Villa Lucre","Colonia Las Lomas","La Pulida","Punta Fresca"] 
		  },
	"Sector_B":{
		"N":["Nuevo Veranillo","San José"]
		,"S":["El Crisol","El Sitio","Llano Bonito","Urb el Bosque del Hipodromo"]
		},
	"Sector_C":{ 
		"N":["Centro Comercial Los Andes N°2","Don Bosco","Los Andes N°2","Samaria"]
		,"S":["Altos del Hipódromo","Dorasol","Residencial Alta Vista","Residencial Altos de San Pedro","San Fernando","San Pedro","Santa Pera","Villa Venus"]
		},
	"Sector_D":{ 
		"N":["Cerro Batea","San Isidro","Tinajita"]
		},
	"Sector_E":{ 
		"N":[ "Colinas de Cerro Batea","Santa Librada","Templo Bahai","Valle de San Isidro"]
		,"S":["Altos de Cerro Viento","Cerro Viento","Cerro Viento Rural","El Chimborazo (Juan diaz)","Las Trancas","Los Pueblos","Santa Ines"]
		},
	"Sector_F":{
		"N":["Cerro Cocobolo","Chivo Chivo","Mano de Piedra","Santa Marta","Sonsonate","Torrijos Carter","Valle de Urracá"]
		,"S":["Brisas del Golf","Ciudad Radial","El Guayabito","La Concepción","Nueva California","Pedregalito","San Antonio"]
		},
	"Sector_G":{
		"S":["Altos de las Acacias","Don Bosco","Naranjal","Pedregal Anasal","Rana de Oro","San Joaquin","Teremar Plaza Tocumen","Villa Catalina"]
		},
	"Sector_H":{
		"N":["Cipreses","Colonia Infantil","Versalles Campestre","Villa Zaita"]
		,"S":["Villalobos (Hasta el Naranjal)"]
		},
	"Sector_I":{
		"N":["La Cabima","Las Cumbres","Las Lajas","Lucha Franco","Nueva Libia despues del puente"]
		,"S":["Club del Golf","La Bandera","Villa Adelina"]
		},
	"Sector_J":{
		"N":["Alcalde Diaz","Ciudad Bolivar"]
		,"S":["Barriada Tocumen","Ciudad Belén","Ciudad Jardin las Mañanitas","Hotel Holiday Inn","La Doña","La Siesta","Las Mañanitas","Monte Rico","Morelos"]
		},
	"Sector_K":{
		"S":["24 de Diciembre","Altos de Tocumen","Cabuyita","Ruben Dario Paredes","Urb Dos Rios","Vista Hermosa"]
		},
	"Sector_L":{
		"N":["Agua Buena","El Tecal","La Esmeralda","La Unión","Quebrada Ancha","San Vicente","Villa Grecia"]
		}
}

def Sector_Origen(lugar):
	dato = []	
	for area in Sectores:
		# print (x)
		for coordenada in Sectores[area]:
			if  lugar in Sectores[area][coordenada]:
				dato.append(coordenada)
				dato.append(area)
	return dato
def Sector_Destino(lugar):
	datos =Sector_Origen(lugar)
	return datos
# cuando no estan la misma coordenada se usa zona o otra cosa
# Sector_Origen(lugar)
# Sector_Destino("El Tecal")
# lugar ="El Tecal"
# lugar2 ="24 de Diciembre" 
# Sector_Origen  = Sector_Origen(lugar)
# Sector_Destino = Sector_Destino(lugar2) 
# camino = [Sector_Origen[1],Sector_Destino[1]]

# print lugar,Sector_Origen
# print lugar2,Sector_Destino
# if Sector_Origen[0] == Sector_Destino[0]:
# 	pass
# 	print "Precio ==> "+str(DbPrecio_Sector(Sector_Origen[0],camino))
# else:
# 	print "Esa Ruta no 'esta Disponible"
# for area in Sectores:
# 	for coordenada in Sectores[area]:
# 		for x in Sectores[area][coordenada]:
# 			print "\""+x+"\""
# 			# print "ActionButton:"
# 			# print 		"\ttext: \'"+x+"\'"