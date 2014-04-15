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


	
		
# 3M 2900 series microSD	
class MICRO_SD_package(package):
    def __init__(self, name="MICROSD", libname="3m",description="MICROSD socket"):
		package.__init__(self, name, libname,description)
		self.smt = True
		# Horizontal orientation, origin on the left side of pad 1 in X and center o pad 1 in Y
		# make pins
		# all units milimeters mm, always use center of the pin pad
		
		# outline is 15.50 x 14.3
		X1 = mm2pcb(-4.05)
		Y1 = mm2pcb(+5.36)

		X2 = mm2pcb(11.45)
		Y2 = mm2pcb(-8.94)
		
		# origin is not in the center of the pin in X so we need offset which is half the pin size in X
		pin1_X = mm2pcb(0.75)
		pin1_Y = mm2pcb(0)
		off_X  = 0
		off_Y  = mm2pcb(-1.10) # pitch 

		# pin.thickness will set in set_pin_pad_from_size
		Thickness = mm2pcb(1.0) 
		# size of pads
		padsizex = mm2pcb(1.5)
		padsizey = mm2pcb(0.8)
		#print "padsizex ", padsizex
		#print "padsizey ", padsizey

		# X offsets per pad
		offsetsX=[0,0.40,0,-0.20,0,-0.20,0,0]

		# Add 8 identical pins
		for i in range(1,9):
			#print " i ", i
			x = pin1_X + mm2pcb(offsetsX[i-1])
			y = pin1_Y + (i-1) * off_Y
			pin = CPin('"'+str(i)+'"',i, x, y )	# stupid should be done automatically
			pin.pad = CPad(padsizex, padsizey, "S")
			pin.set_pin_pad_from_size(padsizex, padsizey)
			self.pins[pin.num]=pin
			
		# pads 9-12 are grounds GND_1 to GND_4
		# GND_1 left below pad 1
		_X = mm2pcb(-3.10)
		_Y = mm2pcb(+4.66)
		padsizex = mm2pcb(1.9)
		padsizey = mm2pcb(1.4)
		pin = CPin('"9"',9, _X, _Y)
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		# GND_2 right just above pad 1
		_X = mm2pcb(11.05)
		_Y = mm2pcb(-1.19)
		padsizex = mm2pcb(1.4)
		padsizey = mm2pcb(1.8)
		pin = CPin('"10"',10,  _X, _Y)
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		# GND_3 right  above pad 1
		_X = mm2pcb(11.05)
		_Y = mm2pcb(-6.89)
		padsizex = mm2pcb(1.4)
		padsizey = mm2pcb(1.8)
		pin = CPin('"11"',11, _X, _Y)
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		# GND_4 left above pad 1
		_X = mm2pcb(-2.10)
		_Y = mm2pcb(-8.40)
		padsizex = mm2pcb(1.9)
		padsizey = mm2pcb(1.4)
		pin = CPin('"12"',12, _X, _Y)
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin

		# Geometry
		# Outline needs to grow by 20 mils except right side by 25
		# lower left corner
		X1 = mm2pcb(-4.05) + mil2pcb(-20)
		Y1 = mm2pcb(+5.36) + mil2pcb(+30)
		

		# Upper right corner
		X2 = mm2pcb(11.45) + mil2pcb(+25)
		Y2 = mm2pcb(-8.94) + mil2pcb(-30)

		Thickness = 1000

		self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
		self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))

		# add origin lines for debuging only
		# self.geometry.append(Line([Point(mm2pcb(-5.00),mm2pcb(0)),Point(mm2pcb(12.00),mm2pcb(0))], int(Thickness)))
		# self.geometry.append(Line([Point(mm2pcb(0),mm2pcb(-9.00)),Point(mm2pcb(0),mm2pcb(6.00))], int(Thickness)))
		
		self.pcbbody = ''


#  3M SD series SD-RSMT
class SD_1_package(package):
    def __init__(self, name="SD_RSMT", libname="3m",description="SD-RSMT socket"):
        package.__init__(self, name, libname,description)
        self.smt = True
       	# all units milimeters mm, always use center of the pin pad
	# origin in the middle of height, on the left side where right edge of pins are
	# pins  9 to 7 uniform spacing, pin 8 same shape as 9-7 but closer, CD and WP narrow and close together
	# 9
	# 1
	# 2
	# 3
	# 4
	# 5
	# 6
	# 7
	# 8
	# 10 Card Detect
	# 11 Write Protect
	# 12 GND 1
	# 13 GND 2
	# 14 Hole 1
	# 15 Hole 2
	# use pin 9 center as reference
	# pin 1 to 9 size is sizeX = 1.50 mm sizey = 1.00 mm
       	pin9_X = mm2pcb(-0.75)
	pin9_Y = mm2pcb(-9.38)
	off_X  = 0
	off_Y  = mm2pcb(2.5) # stepping down
	pin1_X = pin9_X
	pin1_Y = pin9_Y + off_Y
	
	# pin.thickness will set in set_pin_pad_from_size
	Thickness = mm2pcb(1.00) 
	# size of pads
	padsizex = mm2pcb(1.50)
	padsizey = mm2pcb(1.00)
	#print "padsizex ", padsizex
	#print "padsizey ", padsizey
    	
	# Add 6 identical pins 1 to 6
	for i in range(1,7):
		#print " i ", i
		x = pin1_X + (i-1) * off_X
		y = pin1_Y + (i-1) * off_Y
		pin = CPin('"'+str(i)+'"',i, x, y )	# stupid should be done automatically
		pin.pad = CPad(padsizex, padsizey, "S")
		pin.set_pin_pad_from_size(padsizex, padsizey)
		self.pins[pin.num]=pin
		
	# add pin 7 offset from pin 6 is 2.43 mm
	pin7_X = pin1_X
	pin7_Y = pin1_Y + (6 - 1) * off_Y +  mm2pcb(2.43)
	pin = CPin('"'+str(7)+'"',7, pin7_X, pin7_Y )	# stupid should be done automatically
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin

	# add pin 8 offset from pin 7 is 1.70 mm
	pin8_X = pin7_X
	pin8_Y = pin7_Y +  mm2pcb(1.70)
	pin = CPin('"'+str(8)+'"',8, pin8_X, pin8_Y )	# stupid should be done automatically
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin

	# add pin 9 offset from pin 1 -2.50
	pin = CPin('"'+str(9)+'"',9, pin9_X, pin9_Y )	# stupid should be done automatically
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	
	# add pins 10 and 11
	# size of pads
	padsizex = mm2pcb(1.50)
	padsizey = mm2pcb(0.70)
	off_X  = 0
	off_Y  = mm2pcb(0.7) # stepping down
	# add pin 10 offset from pin 8 is 1.30 mm
	pin10_X = pin8_X
	pin10_Y = pin8_Y + mm2pcb(1.30)
	pin = CPin('"'+str(10)+'"',10, pin10_X, pin10_Y )	# stupid should be done automatically
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	# add pin 11 offset from pin 10 is 1.20 mm
	pin11_X = pin10_X
	pin11_Y = pin10_Y + mm2pcb(1.20)
	pin = CPin('"'+str(11)+'"',11, pin11_X, pin11_Y )	# stupid should be done automatically
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	# add pin 12,13 two grounds GND_1 and GND_2
	padsizex = mm2pcb(3.00)
	padsizey = mm2pcb(2.00)
	# lower side
	pin = CPin('"12"',12, mm2pcb(27.00), mm2pcb(15.05) )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	# upper side
	pin = CPin('"13"',13, mm2pcb(27.00), mm2pcb(-15.05) )
	pin.pad = CPad(padsizex, padsizey, "S")
	pin.set_pin_pad_from_size(padsizex, padsizey)
	self.pins[pin.num]=pin
	
	# Holes as pins 14 an 15
	
	# D 1.10 mm x = 2.05 y = 11.50 mm lower side smaller
	Thickness = mm2pcb(0)		# Metalization around the hole
	Clearance = mm2pcb(0)		# Clearance separation
	Mask      = mm2pcb(0)		# Mask diameter
	Drill     = mm2pcb(1.10)	# Drill size
	d  = mm2pcb(1.30)
	X1 = mm2pcb(2.05)
	Y1 = mm2pcb(11.50)
	self.geometry.append(Circle(int(X1), int(Y1),int(d),int(1000)))
	
	# Hole  1 pin 14
	pin = CPin('"14"',14,int(X1),int(Y1))
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
	
	
	# D 1.60 mm x = 2.05 y = -9.50 mm upper side bigger
	Thickness = mm2pcb(0)		# Metalization around the hole
	Clearance = mm2pcb(0)		# Clearance separation
	Mask      = mm2pcb(0)		# Mask diameter
	Drill     = mm2pcb(1.60)	# Drill size
	d  = mm2pcb(1.80)
	X1 = mm2pcb(2.05)
	Y1 = mm2pcb(-9.50)
	self.geometry.append(Circle(int(X1), int(Y1),int(d),int(1000)))
	# Hole  2 pin 15
	pin = CPin('"15"',15,int(X1),int(Y1))
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
	# Outline is 16.3 mm by 13.6 mm
	# shrink in Y to avoid covering pads
	# lower left corner
	X1 = mm2pcb(1.00)
	Y1 = mm2pcb(-14.05) + mil2pcb(+10)
	
	# Upper right corner
	X2 = mm2pcb(30.50)	# might 1 mm too much see X1
	Y2 = mm2pcb(14.05) + mil2pcb(-10)

	Thickness = 1000

	self.geometry.append(Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y1))], int(Thickness)))
	self.geometry.append(Line([Point(int(X2),int(Y1)),Point(int(X1),int(Y1))], int(Thickness)))


	self.pcbbody = ''



class SD_2908(Component):
    "SD_2908 class "
    "3M microSD connector 2908 series"
    def __init__(self, refid, val, name="SD_2908", libname="3m", symbolname="MICROSD", packagename="MICROSD"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.datasheet=""
		self.drawing=""
		self.package = MICRO_SD_package()
		self.parsePackage()
		self.addPin( CPin("DAT2",  		1    ))
		self.addPin( CPin("CD/DAT3",    2    ))
		self.addPin( CPin("CMD",    	3    ))
		self.addPin( CPin("VDD",    	4    ))
		self.addPin( CPin("CLK",   		5    ))
		self.addPin( CPin("VSS2",		6    ))
		self.addPin( CPin("DAT0",		7    ))
		self.addPin( CPin("DAT1",		8    ))
		self.addPin( CPin("GND_1",		9    ))
		self.addPin( CPin("GND_2",		10   ))
		self.addPin( CPin("GND_3",		11   ))
		self.addPin( CPin("GND_4",		12   ))
	
class SD_RSMT(Component):
    "SD_RSMT class "
    "3M SD-RSMT connector SD series"
    def __init__(self, refid, val, name="SD_RSMT", libname="3m", symbolname="SD_RSMT", packagename="SD_RSMT"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.datasheet=""
		self.drawing=""
		self.package = SD_1_package()
		self.parsePackage()
		self.addPin( CPin("CD/DAT3",	1    ))
		self.addPin( CPin("CMD",		2    ))
		self.addPin( CPin("VSS1",		3    ))
		self.addPin( CPin("VDD",		4    ))
		self.addPin( CPin("CLK",   		5    ))
		self.addPin( CPin("VSS2",		6    ))
		self.addPin( CPin("DAT0",		7    ))
		self.addPin( CPin("DAT1",		8    ))
		self.addPin( CPin("DAT2",		9    ))
		self.addPin( CPin("CD",			10   ))
		self.addPin( CPin("WP",			11   ))
		self.addPin( CPin("GND_1",		12   ))
		self.addPin( CPin("GND_2",		13   ))
		self.addPin( CPin("HOLE_1",		14   ))
		self.addPin( CPin("HOLE_2",		15   ))

# Some tests
if __name__ == "__main__":
	sd_2908 = SD_2908("CON1","","SD_2908")
	print sd_2908

