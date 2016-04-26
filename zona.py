#!/usr/bin/python
# -*- coding: utf-8 -*-
Zona = {
	"Zona_1":["La Boca","Calzada de Amador"],
	"Zona_2":["San Felipe","Chorrillo","Santa Ana","Ancón"],
	"Zona_3":["Calidonia","San Miguel","Albrook","Altos de Diablo"],
	"Zona_4":["Punta Paitilla","Bella Vista","Universidad"] ,
	"Zona_5":["Punta Pacífica","El Dorado","Las Sabanas","Bethania"] ,
	"Zona_6":["Panamá Viejo","Río Abajo","Villa de las Fuentes","Los Libertadores"] ,
	"Zona_7":["Costa del Este","Chanis","Auto Motor"] 
}

def zona(lugar):
	datos =[]
	for zon in Zona:
		# for x in Zona[zon]:
		if lugar in Zona[zon]:			
			datos.append("zona")
			datos.append(zon) 
	return datos

# lugar = "Auto Motor"
# zona(lugar)
