#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from precios import Precio
from Conexion import getLugares
from kivy.uix.actionbar import ActionGroup
from kivy.uix.actionbar import ActionButton
class AddBoton(ActionGroup):
	def __init__(self, **kwargs):
            super(AddBoton,self).__init__(**kwargs)
            self.id= "tx"
            self.markup = True
            self.text = '[b][color=#E65F00]---ttyy---[/color][/b]'
            self.crear()
	def crear(self):
			for nom in getLugares():
				bt = ActionButton(text=nom)
				bt.bind(on_press=self.evt_origen)
				self.add_widget(bt)
	def evt_origen(self, obj):
            obj.text = obj.text
            print(self.ids)
            org = ""+obj.text
            print(org)
            Ventana.origen = org
class Ventana(Screen):
	precio = ObjectProperty
	origen=""
	destino=""
	def Origen(self, origen):
			self.origen = origen
			print (origen)
	def Destino(self, destino):
			self.destino = destino
			print (destino)	
	def CalcularPrecio(self):
            print(self.origen)
            if self.origen != "" and self.destino != "":
                                costo = ""+Precio(self.origen,self.destino)
                                if costo == "null":
                                        self.precio.text ="Costo Aun no Disponible... porque vas de S a N o N a S. Proximamente."
                                else:
                                        self.precio.text = "El Costo del Viaje sera de $ "+costo
            else:
                self.precio.text = "Aún no a Seleccionado las Ruta..."

class AplicacionApp(App): 
	def build(self):  
		return Ventana()
	def on_pause(self):
		return True



if __name__ == '__main__':
	AplicacionApp().run()
