#!/usr/bin kivy
#*-* coding:utf-8 *-*
#Aplicación creada por Diego Alberto Parra Garzón
#Licencia GPL3 
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.config import Config 
from commands import getoutput
import time
import os
import ast
Config.set("graphics", 'width', "650")
Config.set("graphics", 'height', "400")

class LoginScreen(RelativeLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
	self.posicion_botones()
	self.estado_ante = None
	self.VAR1 =None
	self.VAR2 = None
	self.Restaurar()
	self.Punto()
	self.Igual()
        self.Boton0()
  	self.Boton1()
	self.Boton2()
	self.Boton3()
	self.Boton4()
	self.Boton5()
	self.Boton6()
	self.Boton7()
	self.Boton8()
	self.Boton9()
        self.label2()
	self.Boton_suma()
	self.Boton_resta()
	self.Boton_multi()
	self.Boton_divi()

    

    def posicion_botones(self):
	self.posX = 200
	self.posY = 0

    def Restaurar(self):
        self.reset = Button(text =' Reset ')
        self.reset.font_size = 20
        self.reset.multiline = False
        self.reset.size_hint = 0.1, 0.1
        self.reset.pos = self.posX + 370, self.posY + 240
        self.reset.bind(on_press=self.ac_Reset)
        self.add_widget(self.reset)   

    def Igual(self):
        self.igual = Button(text =' = ')
        self.igual.font_size = 20
        self.igual.multiline = False
        self.igual.size_hint = 0.1, 0.1
        self.igual.pos = self.posX + 190, self.posY + 30
#        self.Punto.bind(on_press=self.ac_Igual)
        self.add_widget(self.igual)    

    def Igual1(self):
        self.igual1 = Button(text =' = ')
        self.igual1.font_size = 20
        self.igual1.multiline = False
        self.igual1.size_hint = 0.1, 0.1
        self.igual1.pos = self.posX + 190, self.posY + 30
        self.igual1.bind(on_press=self.ac_Igual1)
        self.add_widget(self.igual1)   

    def Igual2(self):
        self.igual2 = Button(text =' = ')
        self.igual2.font_size = 20
        self.igual2.multiline = False
        self.igual2.size_hint = 0.1, 0.1
        self.igual2.pos = self.posX + 190, self.posY + 30
        self.igual2.bind(on_press=self.ac_Igual2)
        self.add_widget(self.igual2)  

    def Igual3(self):
        self.igual3 = Button(text =' = ')
        self.igual3.font_size = 20
        self.igual3.multiline = False
        self.igual3.size_hint = 0.1, 0.1
        self.igual3.pos = self.posX + 190, self.posY + 30
        self.igual3.bind(on_press=self.ac_Igual3)
        self.add_widget(self.igual3) 

    def Igual4(self):
        self.igual4 = Button(text =' = ')
        self.igual4.font_size = 20
        self.igual4.multiline = False
        self.igual4.size_hint = 0.1, 0.1
        self.igual4.pos = self.posX + 190, self.posY + 30
        self.igual4.bind(on_press=self.ac_Igual4)
        self.add_widget(self.igual4)

    def Punto(self):
        self.Punto = Button(text =' . ')
        self.Punto.font_size = 20
        self.Punto.multiline = False
        self.Punto.size_hint = 0.1, 0.1
        self.Punto.pos = self.posX + 100, self.posY + 30
        self.Punto.bind(on_press=self.ac_Punto)
        self.add_widget(self.Punto)

    def Boton0(self):
        self.btn0 = Button(text =' 0 ')
        self.btn0.font_size = 20
        self.btn0.multiline = False
        self.btn0.size_hint = 0.1, 0.1
        self.btn0.pos = self.posX + 10, self.posY + 30
        self.btn0.bind(on_press=self.ac_Btn0)
        self.add_widget(self.btn0)

    def Boton1(self):
        self.btn1 = Button(text =' 1 ')
        self.btn1.font_size = 20
        self.btn1.multiline = False
        self.btn1.size_hint = 0.1, 0.1
        self.btn1.pos = self.posX + 10, self.posY + 100
        self.btn1.bind(on_press=self.ac_Btn1)
        self.add_widget(self.btn1)

    def Boton2(self):
        self.btn2 = Button(text =' 2 ')
        self.btn2.font_size = 20
        self.btn2.multiline = False
        self.btn2.size_hint = 0.1, 0.1
        self.btn2.pos = self.posX + 100,  self.posY + 100
        self.btn2.bind(on_press=self.ac_Btn2)
        self.add_widget(self.btn2)

    def Boton3(self):
        self.btn3 = Button(text =' 3 ')
        self.btn3.font_size = 20
        self.btn3.multiline = False
        self.btn3.size_hint = 0.1, 0.1
        self.btn3.pos = self.posX + 190,  self.posY + 100
        self.btn3.bind(on_press=self.ac_Btn3)
        self.add_widget(self.btn3)

    def Boton4(self):
        self.btn4 = Button(text =' 4 ')
        self.btn4.font_size = 20
        self.btn4.multiline = False
        self.btn4.size_hint = 0.1, 0.1
        self.btn4.pos = self.posX + 10,  self.posY + 170
        self.btn4.bind(on_press=self.ac_Btn4)
        self.add_widget(self.btn4)

    def Boton5(self):
        self.btn5 = Button(text =' 5 ')
        self.btn5.font_size = 20
        self.btn5.multiline = False
        self.btn5.size_hint = 0.1, 0.1
        self.btn5.pos = self.posX + 100,  self.posY + 170
        self.btn5.bind(on_press=self.ac_Btn5)
        self.add_widget(self.btn5)

    def Boton6(self):
        self.btn6 = Button(text =' 6 ')
        self.btn6.font_size = 20
        self.btn6.multiline = False
        self.btn6.size_hint = 0.1, 0.1
        self.btn6.pos = self.posX + 190,  self.posY + 170
        self.btn6.bind(on_press=self.ac_Btn6)
        self.add_widget(self.btn6)

    def Boton7(self):
        self.btn7 = Button(text =' 7 ')
        self.btn7.font_size = 20
        self.btn7.multiline = False
        self.btn7.size_hint = 0.1, 0.1
        self.btn7.pos = self.posX + 10,  self.posY + 240
        self.btn7.bind(on_press=self.ac_Btn7)
        self.add_widget(self.btn7)

    def Boton8(self):
        self.btn8 = Button(text =' 8 ')
        self.btn8.font_size = 20
        self.btn8.multiline = False
        self.btn8.size_hint = 0.1, 0.1
        self.btn8.pos = self.posX + 100,  self.posY + 240
        self.btn8.bind(on_press=self.ac_Btn8)
        self.add_widget(self.btn8)

    def Boton9(self):
        self.btn9 = Button(text =' 9 ')
        self.btn9.font_size = 20
        self.btn9.multiline = False
        self.btn9.size_hint = 0.1, 0.1
        self.btn9.pos = self.posX + 190,  self.posY + 240
        self.btn9.bind(on_press=self.ac_Btn9)
        self.add_widget(self.btn9)

    def Boton_suma(self):
	self.Boton_suma = Button(text =' + ')
        self.Boton_suma.font_size = 20
        self.Boton_suma.multiline = False
        self.Boton_suma.size_hint = 0.1, 0.1
        self.Boton_suma.pos = self.posX + 280,  self.posY + 240
        self.Boton_suma.bind(on_press=self.ac_Boton_suma)
        self.add_widget(self.Boton_suma)

    def Boton_resta(self):
	self.Boton_resta = Button(text =' - ')
        self.Boton_resta.font_size = 20
        self.Boton_resta.multiline = False
        self.Boton_resta.size_hint = 0.1, 0.1
        self.Boton_resta.pos = self.posX + 280,  self.posY + 170
        self.Boton_resta.bind(on_press=self.ac_Boton_resta)
        self.add_widget(self.Boton_resta)

    def Boton_multi(self):
	self.Boton_multi = Button(text =' * ')
        self.Boton_multi.font_size = 20
        self.Boton_multi.multiline = False
        self.Boton_multi.size_hint = 0.1, 0.1
        self.Boton_multi.pos = self.posX + 280,  self.posY + 100
        self.Boton_multi.bind(on_press=self.ac_Boton_multi)
        self.add_widget(self.Boton_multi)

    def Boton_divi(self):
	self.Boton_divi = Button(text =' / ')
        self.Boton_divi.font_size = 20
        self.Boton_divi.multiline = False
        self.Boton_divi.size_hint = 0.1, 0.1
        self.Boton_divi.pos = self.posX + 280,  self.posY + 30
        self.Boton_divi.bind(on_press=self.ac_Boton_divi)
        self.add_widget(self.Boton_divi)

    def label2(self):
        self.Label2 = Label(color = [1,1,0,1])
        self.Label2.size_hint= 0.1, 0.1
        self.Label2.font_size= 50
        self.Label2.pos= 340, 320
        self.add_widget(self.Label2)

    def ac_Punto(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = str(".")
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = str(".")
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn0(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 0
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 0
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn1(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 1
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 1
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn2(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
		self.estado = 2
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 2
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn3(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	        self.estado = 3
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 3
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn4(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
		self.estado = 4
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 4
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn5(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 5
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 5
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn6(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 6
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 6
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta
	

    def ac_Btn7(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 7
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 7
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn8(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
	    	self.estado = 8
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 8
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta

    def ac_Btn9(self, *args):
	if self.estado_ante is not None:
	    longi = str(self.estado_ante)
	    longitud = longi[:]
	    if longitud > longi[0:11]:
	 	print "paso"
	
	    else:
	    	print "Esta es: ", longitud[0:12]
		self.estado = 9
	    	self.nuevo_esta = str(self.estado_ante) + str(self.estado)
	    	self.Label2.text = str(self.nuevo_esta)
	    	self.estado_ante=self.nuevo_esta	
	
	if self.estado_ante is None:
	    self.estado = 9
	    self.nuevo_esta = str(self.estado)
	    self.Label2.text = str(self.nuevo_esta)
	    self.estado_ante=self.nuevo_esta	    

    def ac_Boton_suma(self, *args):
	if self.VAR1 is not None:
	    self.Igual1()
	    pass

	if self.VAR1 is None:
	  #  Var = self.estado_ante[0:11]
	    self.VAR1 = self.estado_ante
	    print self.VAR1, self.VAR2
	    self.no_se()
	    self.Igual1()	
	    pass
	
	if self.VAR1 is  None and self.estado_ante is  None:
	    print "ya oprimio este boton"
	
	else: 
	    print "No se que paso"
	
	    

    def Cual(self, *arg):
	if self.VAR1 is not None and self.estado_ante is not None:
 	    self.VAR2 = self.estado_ante
	    var1 = self.VAR1
            nodo1 = ast.parse(var1, mode='eval')
	    self.VAR1_ = eval(compile(nodo1, '<string>', mode='eval'))
	    var2 = self.VAR2
	    nodo2 = ast.parse(var2, mode='eval')
	    self.VAR2_ = eval(compile(nodo2, '<string>', mode='eval'))

	    self.suma = str(self.VAR1_ + self.VAR2_)	    
	    self.Label2.text = str(self.suma) 
	    print self.VAR1_," + ", self.VAR2_, " = ", self.suma
	    self.estado_ante = str(self.suma)
	    self.VAR2 = None
	    self.VAR1 = None
	    print "voy aca"



    def ac_Igual1(self, *args):
	self.Cual()
	self.igual.text = " = " 
	print "aca estoy sa"


    def ac_Boton_resta(self, *args):
	if self.VAR1 is not None:
	    self.Igual2()
	    pass


	if self.VAR1 is None:
	  #  Var = self.estado_ante[0:11]
	    self.VAR1 = self.estado_ante
	    print self.VAR1, self.VAR2
	    self.no_se()
	    self.Igual2()	
	    pass
	
	if self.VAR1 is  None and self.estado_ante is  None:
	    print "ya oprimio este boton"	
	    

	else: 
	    print "No se que paso"

    def Cual1(self, *arg):
	if self.VAR1 is not None and self.estado_ante is not None:
 	    self.VAR2 = self.estado_ante
	    var1 = self.VAR1
            nodo1 = ast.parse(var1, mode='eval')
	    self.VAR1_ = eval(compile(nodo1, '<string>', mode='eval'))
	    var2 = self.VAR2
	    nodo2 = ast.parse(var2, mode='eval')
	    self.VAR2_ = eval(compile(nodo2, '<string>', mode='eval'))

	    self.resta = str(self.VAR1_ - self.VAR2_)	    
	    self.Label2.text = str(self.resta) 
	    print self.VAR1_," + ", self.VAR2_, " = ", self.resta
	    self.estado_ante = str(self.resta)
	    self.VAR2 = None
	    self.VAR1 = None
	    print "voy aca"



    def ac_Igual2(self, *args):
	self.Cual1()
	self.igual.text = " = " 
	print "aca estoy sa"



    def ac_Boton_multi(self, *args):
	if self.VAR1 is not None:
	    self.Igual3()
	    pass


	if self.VAR1 is None:
	  #  Var = self.estado_ante[0:11]
	    self.VAR1 = self.estado_ante
	    print self.VAR1, self.VAR2
	    self.no_se()
	    self.Igual3()	
	    pass
	
	if self.VAR1 is  None and self.estado_ante is  None:
	    print "ya oprimio este boton"	
	    

	else: 
	    print "No se que paso"

    def Cual2(self, *arg):
	if self.VAR1 is not None and self.estado_ante is not None:
 	    self.VAR2 = self.estado_ante
	    var1 = self.VAR1
            nodo1 = ast.parse(var1, mode='eval')
	    self.VAR1_ = eval(compile(nodo1, '<string>', mode='eval'))
	    var2 = self.VAR2
	    nodo2 = ast.parse(var2, mode='eval')
	    self.VAR2_ = eval(compile(nodo2, '<string>', mode='eval'))

	    self.multi = str(self.VAR1_ * self.VAR2_)	    
	    self.Label2.text = str(self.multi) 
	    print self.VAR1_," + ", self.VAR2_, " = ", self.multi
	    self.estado_ante = str(self.multi)
	    self.VAR2 = None
	    self.VAR1 = None
	    print "voy aca"



    def ac_Igual3(self, *args):
	self.Cual2()
	self.igual.text = " = " 
	print "aca estoy sa"


    def ac_Boton_divi(self, *args):
	if self.VAR1 is not None:
	   self.Igual4()
	   pass


	if self.VAR1 is None:
	  #  Var = self.estado_ante[0:11]
	    self.VAR1 = self.estado_ante
	    print self.VAR1, self.VAR2
	    self.no_se()
	    self.Igual4()	
	    pass
	
	if self.VAR1 is  None and self.estado_ante is  None:
	    print "ya oprimio este boton"	
	    

	else: 
	    print "No se que paso"

    def Cual3(self, *arg):
	if self.VAR1 is not None and self.estado_ante is not None:
 	    self.VAR2 = self.estado_ante
	    var1 = self.VAR1
            nodo1 = ast.parse(var1, mode='eval')
	    self.VAR1_ = eval(compile(nodo1, '<string>', mode='eval'))
	    var2 = self.VAR2
	    nodo2 = ast.parse(var2, mode='eval')
	    self.VAR2_ = eval(compile(nodo2, '<string>', mode='eval'))
	    if self.VAR2_ == 0:
		print "Baboso no existe tal cosa"
		self.Label2.text = " ERROR MATH "
		self.estado_ante = None
		self.VAR1 =None
		self.VAR2 = None

	    else:
	        self.divi = str(float(self.VAR1_) / float(self.VAR2_))	    
	    	self.Label2.text = str(self.divi) 
	    	print self.VAR1_," / ", self.VAR2_, " = ", self.divi
	    	self.VAR1 = str(self.divi)
	    	self.VAR2 = None
	    	self.estado_ante = None
	    	print "voy aca"


    def ac_Igual4(self, *args):
	self.Cual3()
	self.igual.text = " = " 
	print "aca estoy sa"

    def ac_Reset(self, *args):
	self.Label2.text = " 0 "
	self.estado_ante = None
	self.VAR1 =None
	self.VAR2 = None
	print "Voy aca"

	
    def no_se(self): 
	self.estado_ante = None
	pass
	
class arduinoApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    arduinoApp().run()

