# -*- coding: utf-8 -*-
#
# Copyright (c) 2014, Paweł Wodnicki
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the 32bitmicro nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL Paweł Wodnicki BE LIABLE FOR ANY
#DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from eda import *
from eda.components import *


		
# 2 pin JST 2 mm battery connector
# origin is in the center, first pin in lower left corner
# real pads 1 are 2 are connected
# pads 3 and 4 are just for mounting

class JST_2x2_package(package):
    def __init__(self, name="JST_2x2", libname="jst",description="JST 2 pin 2 mm package"):
		package.__init__(self, name, libname,description)
		self.smt = True
		# all dims in mm
		# horizontal orientation with pins 1 and 2 on the left
		# origin is on the left side of the pins X and in the middle between pins Y
		# pins 3 and 4 are for soldering only can be connected to GND
		 
		padsizex = mm2pcb(3.50)
		padsizey = mm2pcb(1.00)
		pad_X = mm2pcb(3.50/2)
		pad_Y = mm2pcb(1.0)

		# pin 1 bottom
		p_X = pad_X
		p_Y = pad_Y
		
		pin = CPin('"1"', 1, p_X, p_Y )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
		
		# pin 2 top
		p_X = pad_X
		p_Y = -pad_Y
		pin = CPin('"2"', 2, p_X, p_Y )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		padsizex = mm2pcb(3.40)
		padsizey = mm2pcb(1.50)
		pad_X = mm2pcb(7.30)			# 9 -  padsizex / 2
		pad_Y = mm2pcb(3.35)
		
		# pin 3
		p_X = pad_X
		p_Y = -pad_Y
		pin = CPin('"3"', 3, p_X, p_Y )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
		
		# pin 
		p_X = pad_X
		p_Y = pad_Y
		pin = CPin('"4"', 4, p_X, p_Y )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		# Geometry
		# Outline is 7.90 mm by 6.0 mm 
		# lower left corner
		X1 = mm2pcb(3.00)         + mil2pcb(+40)
		Y1 = mm2pcb(7.90/2)       + mil2pcb(+20)

		# Upper right corner
		X2 = mm2pcb(9.00)         + mil2pcb(+15)
		Y2 = mm2pcb(-7.90/2)      + mil2pcb(-20)
		Thickness = 1000

		# outline
		self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))

class JST_2(Component):
    "JST 2 pin 2mm side entry connector class"
    def __init__(self, refid, val, name="JST_2", libname="header", symbolname="JST_2", packagename="JST_2"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = JST_2x2_package(packagename, libname, "JST 2 pin 2mm side entry")
		self.parsePackage()
		self.addPin( CPin('1',		1    ))
		self.addPin( CPin('2',		2    ))
		self.addPin( CPin('GND_1',	3    ))
		self.addPin( CPin('GND_2',	4    ))


# Some tests
if __name__ == "__main__":
	componnet = JST_2("CON1","","JST_2")
	print componnet

