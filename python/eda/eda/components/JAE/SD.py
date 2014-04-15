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


	
		
		
class MICRO_SD_package(package):
	def __init__(self, name="MICROSD", libname="jae",description="MICROSD socket"):
		package.__init__(self, name, libname,description)
		self.smt = True
		# make pins
		# all units milimeters mm, always use center of the pin pad
		pin1_X = mm2pcb(-11.55)
		pin1_Y = mm2pcb(3.85)
		off_X  = 0
		off_Y  = mm2pcb(-1.1)
	
		# pin.thickness will set in set_pin_pad_from_size
		Thickness = mm2pcb(1.0) 
		# size of pads
		padsizex = mm2pcb(1.8)
		padsizey = mm2pcb(0.8)
		#print "padsizex ", padsizex
		#print "padsizey ", padsizey
    	
		# Add 8 identical pins
		for i in range(1,9):
			#print " i ", i
			x = pin1_X + (i-1) * off_X
			y = pin1_Y + (i-1) * off_Y
			pin = CPin('"'+str(i)+'"',i, x, y )	# stupid should be done automatically
			pin.pad = CPad(padsizex, padsizey, "S")
			pin.set_pin_pad_from_size(padsizex, padsizey)
			self.pins[pin.num]=pin
		
		# pads 9-12 are grounds GND_1 to GND_4
		# GND_1 and GND_2
		padsizex = mm2pcb(1.2)
		padsizey = mm2pcb(1.8)
		pin = CPin('"9"',9, 0, mm2pcb(3.3) )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
		
		pin = CPin('"10"',10, 0, mm2pcb(-4.05) )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
	
		# GND_3 and GND_4
		padsizex = mm2pcb(1.4)
		padsizey = mm2pcb(1.8)
		pin = CPin('"11"',11, mm2pcb(-13.55), mm2pcb(3.25) )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
		
		pin = CPin('"12"',12, mm2pcb(-13.55), mm2pcb(-3.25) )
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
	
		# Geometry
		# Outline is 16.3 mm by 13.6 mm
		# lower left corner
		X1 = mm2pcb(-16.3) + mm2pcb(1.2)
		Y1 = 0 - mm2pcb(13.6 / 2)
		
		# Upper right corner
		X2 = mm2pcb(1.2)
		Y2 = 0 + mm2pcb(13.6 / 2)
		
		dx = mm2pcb(16.3)
		dy = mm2pcb(13.6)
		
		Thickness = 1000
		
		self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))
		
		
		self.pcbbody = ''



class ST1W008S4E(Component):
    "ST1W008S4E class "
    "JAE microSD connector ST1 series"
    def __init__(self, refid, val, name="ST1W008S4E", libname="jae", symbolname="MICROSD", packagename="MICROSD"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.datasheet="http://jae-connector.com/en/pdf/SJ107022.pdf"
		self.drawing="http://media.digikey.com/PDF/Catalog%20Drawings/Connectors/ST1%20SERIES.jpg"
		self.package = MICRO_SD_package()
		self.parsePackage()
		self.addPin( CPin("DAT2",  	1    ))
		self.addPin( CPin("CD/DAT3",    2    ))
		self.addPin( CPin("CMD",    	3    ))
		self.addPin( CPin("VDD",    	4    ))
		self.addPin( CPin("CLK",   	5    ))
		self.addPin( CPin("VSS",	6    ))
		self.addPin( CPin("DAT0",	7    ))
		self.addPin( CPin("DAT1",	8    ))
		self.addPin( CPin("GND_1",	9    ))
		self.addPin( CPin("GND_2",	10   ))
		self.addPin( CPin("GND_3",	11   ))
		self.addPin( CPin("GND_4",	12   ))
	

# Some tests
if __name__ == "__main__":
	st1w008s4e = ST1W008S4E("CON1","","ST1W008S4E")
	print st1w008s4e

