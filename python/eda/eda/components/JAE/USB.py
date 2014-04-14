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


class USB_B_package(package):
    def __init__(self, name="USB_B", libname="jae",description="USB B"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
   Pin[18800 59000 6600 2000 8600 4600 "" "1" 0x01]
   Pin[28600 59000 6600 2000 8600 4600 "" "2" 0x01]
   Pin[28600 51200 6600 2000 8600 4600 "" "3" 0x01]
   Pin[18800 51200 6600 2000 8600 4600 "" "4" 0x01]
   Pin[0 40500 13000 2000 13000 11000 "" "5" 0x01]
   Pin[47400 40500 13000 2000 13000 11000 "" "6" 0x01]
   ElementLine[0 34500 0 0 1000]
   ElementLine[0 0 47400 0 1000]
   ElementLine[47400 0 47400 34500 1000]
   ElementLine[0 46500 0 64000 1000]
   ElementLine[0 64000 47400 64000 1000]
   ElementLine[47400 64000 47400 46500 1000]
   
)
    '''
    
# pads 1 through 5 are USB pins
# pads 6 through 9 are shield soldering pads
class MINIUSB_B_PCB_package(package):
    def __init__(self, name="MINIUSB_B", libname="jae",description="MINIUSB B"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
   Pad[21062 -6299 27952 -6299 1968 2000 3968 "" "1" 0x0100]
   Pad[21062 -3149 27952 -3149 1968 2000 3968 "" "2" 0x0100]
   Pad[21062 0 27952 0 1968 2000 3968 "" "3" 0x0100]
   Pad[21062 3149 27952 3149 1968 2000 3968 "" "4" 0x0100]
   Pad[21062 6299 27952 6299 1968 2000 3968 "" "5" 0x0100]

   Pad[6535 -19389 11712 -19389 8070 2000 10070 "" "6" 0x0100]
   Pad[6535 19389 11712 19389 8070 2000 10070 "" "7" 0x0100]
   Pad[21751 -19389 27460 -19389 8070 2000 10070 "" "8" 0x0100]
   Pad[21751 19389 27460 19389 8070 2000 10070 "" "9" 0x0100]

   ElementLine[1000 -14854 -7374 -14854 1000]
   ElementLine[-7374 -14854 -7374 14854 1000]
   ElementLine[-7374 14854 1000 14854 1000]
   ElementLine[500 -14854 500 14854 1000]
   ElementLine[500 -11901 4618 -11901 1000]
   ElementLine[4618 -11901 4618 11901 1000]
   ElementLine[4618 11901 500 11901 1000]
   ElementLine[4618 -11901 500 -7783 1000]
   ElementLine[4618 -7140 500 -3022 1000]
   ElementLine[4618 -2061 500 2056 1000]
   ElementLine[4618 2699 500 6817 1000]
   ElementLine[4618 7459 500 11577 1000]
   ElementLine[27059 -13842 27059 -8783 1000]
   ElementLine[27059 13842 27059 8783 1000]
   ElementArc[15354 -8661 2500 2500 0 360 1000]
   ElementArc[15354 8661 2500 2500 0 360 1000]
   
)
    '''
# taken out because of problems more then 5 pins for this componnent

#   Pin[15354 -8661 4000 2000 6000 4000 "" "7" 0x09]
#   Pin[15354 8661 4000 2000 6000 4000 "" "7" 0x09]



# pads 1 through 5 are USB pins
# pads 6 through 9 are shield soldering pads
class MINIUSB_B_package(package):
    def __init__(self, name="MINIUSB_B", libname="jae",description="MINIUSB B"):
        package.__init__(self, name, libname,description)
	self.smt = True
	# make pins
       	# all units milimeters mm, always use center of the pin pad
       	pin1_X = mm2pcb(7.85)
	pin1_Y = mm2pcb(-1.6)
	off_X  = 0
	off_Y  = mm2pcb(0.8)
	
	# size of pads
	padsizex = mm2pcb(2.3)
	padsizey = mm2pcb(0.5)
	#print "padsizex ", padsizex
	#print "padsizey ", padsizey
    	
	# Add 5 identical pins for USB lines
	for i in range(1,6):
		#print " i ", i
		x = pin1_X + (i-1) * off_X
		y = pin1_Y + (i-1) * off_Y
		pin = CPin('"'+str(i)+'"',i, x, y )	# stupid should be done automatically
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
			
	# pads 6-9 are grounds GND_1 to GND_4
	# GND_1 and GND_2
	padsizex = mm2pcb(2.5)
	padsizey = mm2pcb(2.0)
	X1 = mm2pcb(2.25)
	Y1 = mm2pcb(4.45)
	X2 = mm2pcb(7.75)
	Y2 = mm2pcb(-4.45)
	pin = CPin('"6"',6, X1, Y1 )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin

	pin = CPin('"7"',7, X2, Y1 )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	
	pin = CPin('"8"',8,  X2, Y2 )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin

	pin = CPin('"9"',9,  X1, Y2 )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	
	# pins 10 and 11 are two holes, not connected anywhere
	
	# Holes as 2 pins
		
	Thickness = mm2pcb(0)		# Metalization around the hole
	Clearance = mm2pcb(0)		# Clearance separation
	Mask      = mm2pcb(0)		# Mask diameter
	Drill     = mm2pcb(0.9)		# Drill size
		
	# Hole  1 pin 10
	X1 = mm2pcb(+5.25)
	Y1 = mm2pcb(-4.40/2)	
	pin = CPin('"10"',10,int(X1),int(Y1))
	pin.smt         = False
	pin.thickness   = int(Thickness)
	pin.clearance   = int(Clearance)
	pin.mask        = int(Mask)
	pin.drill       = int(Drill)
	pin.sflags		= '0x0008'				# hole only
	sizex = Drill
	sizey = Drill
	pin.pad = CPad(sizex, sizey, "R", pin.drill )
	# make bbox covering pin with clearance, will be used for blockages    
	size = pin.thickness + pin.clearance
	x1 = int(pin.pos._x - size / 2)
	x2 = int(pin.pos._x + size / 2)
	y1 = int(pin.pos._y - size / 2)
	y2 = int(pin.pos._y + size / 2)
	pin.bbox = Rectangle(x1,y1,x2,y2,0)   
	self.pins[pin.num]=pin
	
	# Hole  2 pin 11
	X1 = mm2pcb(+5.25)
	Y1 = mm2pcb(+4.40/2)	
	pin = CPin('"11"',11,int(X1),int(Y1))
	pin.smt         = False
	pin.thickness   = int(Thickness)
	pin.clearance   = int(Clearance)
	pin.mask        = int(Mask)
	pin.drill       = int(Drill)
	pin.sflags		= '0x0008'				# hole only
	sizex = Drill
	sizey = Drill
	pin.pad = CPad(sizex, sizey, "R", pin.drill )
	# make bbox covering pin with clearance, will be used for blockages    
	size = pin.thickness + pin.clearance
	x1 = int(pin.pos._x - size / 2)
	x2 = int(pin.pos._x + size / 2)
	y1 = int(pin.pos._y - size / 2)
	y2 = int(pin.pos._y + size / 2)
	pin.bbox = Rectangle(x1,y1,x2,y2,0)   
	self.pins[pin.num]=pin
	
	# Geometry
	# Body thick line
	# lower left corner
	X1 = 0
	Y1 = mm2pcb(-3.85)
	# Upper right corner
	X2 = mm2pcb(9.2)
	Y2 = mm2pcb(3.85)

	Thickness = 1000

	self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))

	# outline - thin line
	X1 = 0
	Y1 = mm2pcb(-5.45)
	# Upper right corner
	X2 = mm2pcb(9.2)
	Y2 = mm2pcb(5.45)

	Thickness = 600
	
	self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))
	
	self.pcbbody = ''
	
    

 # will take package size as a parameter
class DX2R005HN2(Component):
    "DX2R005HN2 class "
    "JAE Mini USB B connector UX series"
    def __init__(self, refid, val, name="DX2R005HN2", libname="jae", symbolname="MINIUSB_B", packagename="MINIUSB_B"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.datasheet="http://www.jae-connector.com/en/pdf/SJ037525.pdf"
		self.drawing="http://media.digikey.com/pdf/catalog%20drawings/Connectors/DX2%20SERIES.jpg"
		self.package = MINIUSB_B_package()
		self.parsePackage()
		self.addPin( CPin("VBUS",  		1    ))
		self.addPin( CPin("D-",    		2    ))
		self.addPin( CPin("D+",    		3    ))
		self.addPin( CPin("ID",    		4    ))
		self.addPin( CPin("GND",   		5    ))
		self.addPin( CPin("SHIELD_1",	6    )) # shield 1
		self.addPin( CPin("SHIELD_2",	7    )) # shield 2
		self.addPin( CPin("SHIELD_3",	8    )) # shield 3
		self.addPin( CPin("SHIELD_4",	9    )) # shield 4
		self.addPin( CPin("HOLE_1",		10   )) # hole 1
		self.addPin( CPin("HOLE_2",		11   )) # hole 2

# Some tests
if __name__ == "__main__":
	dx2r005hn2 = DX2R005HN2("CON1","","DX2R005HN2")
	print dx2r005hn2

