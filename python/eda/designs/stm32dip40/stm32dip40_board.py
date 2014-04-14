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
from eda.xmlpickle import *

import stm32dip40_schematic

# gnosis xml unpickle is causing, why?
#  File "/usr/local/hobby-robotics/src/hbbrbasic/gen/eda/core.py", line 751, in a
#addFromSchematic
#    for dev in self.sch.devices.values():
#AttributeError: CDevices instance has no attribute 'values'


def import_schematic_pickle():
	pickle=CXMLPickle()
	f = open("stm32dip40/stm32dip40.schematic",'r+')
	pickle.unpickleSchematic(f)
	sch =  pickle.sch
	return sch

def import_schematic():
	sch = stm32dip40_schematic.make('stm32dip40', 'stm32dip40')
	return sch

def make(sch, dname="stm32dip40", lname="stm32dip40"):
 	# Board
	DesignName = dname
	LibName = lname

	###################################################################################################
	# Make board
	brd = CBoard(sch)
	brd.name = DesignName

	# transfer data from schematic
	brd.addFromSchematic(sch)
	sizex = 50+600+50 # 600 mils spacing between rows plus 50 mils on each side
	sizey = 100+50 + 19 * 100 + 50 # 100 mils for serial pins 20 pin dip plus 50 mils on top and bottom

	# Simple rectangle
	brd.outline.append(Point(0,0))
	brd.outline.append(Point(mil2pcb(sizex),0))
	brd.outline.append(Point(mil2pcb(sizex),mil2pcb(sizey)))
	brd.outline.append(Point(0,mil2pcb(sizey)))
	brd.bbox=Rectangle(0, 0, mil2pcb(sizex), mil2pcb(sizey)) # shoul be calculated automatically


	# Top layer
	toplayer=CLayer("TOP",1,False)
	brd.addLayer(toplayer)

	# Bottom layer
	bottomlayer=CLayer("BOTTOM",2,True)
	brd.addLayer(bottomlayer)


	# Pour on the bottom 
	GNDnet = brd.nets['GND']
	pour = CPour("GND_POUR_BOTTOM",GNDnet.name,1)
	pour.poly = Polygon([])                            # polygon
	pour.poly.thickness =  mil2pcb(10)
	pour.poly.append(Point(mil2pcb(100),          mil2pcb(10)))
	pour.poly.append(Point(mil2pcb(sizex-100),    mil2pcb(10)))
	pour.poly.append(Point(mil2pcb(sizex-100),    mil2pcb(sizey-100)))
	pour.poly.append(Point(mil2pcb(100),          mil2pcb(sizey-100)))
	pour.poly.append(Point(mil2pcb(100),          mil2pcb(10)))
	pour.layernum = bottomlayer.num
	pour.isolate = mil2pcb(10)                       # 10 mil isolation
	brd.pours.append(pour)

	# Place DIP 40 module in the lower left corner
	MOD1=brd.devices['MOD1']
	MOD1.setPos(mil2pcb(50) , mil2pcb(50))
	
	U3=brd.devices['U3']
	U3.setBottom(False)
	MOD1.setRotation(270)
	MOD1.setOrientation("")


	#Place U1
	U1X = 490
	U1Y = 1090
	U1=brd.devices['U1']
	U1.setPos(mil2pcb(490), mil2pcb(1090))
	U1.setBottom(False)
	U1.setRotation(180)
	U1.setOrientation("")


	# Fiducials
	U1X = 490 - 140
	U1Y = 1090 + 140
	# hardcoded for now
	#(x=0, y=0, width=0, height=0, sangle=0, dangle=0, thickness=1, layernum=0 ):
	brd.geometry.append(Arc(mil2pcb(U1X-170), mil2pcb(U1Y-170), mil2pcb(20), mil2pcb(20), 0, 360, 0, 1))
	brd.geometry.append(Arc(mil2pcb(U1X+170), mil2pcb(U1Y+170), mil2pcb(20), mil2pcb(20), 0, 360, 0, 1))


	#Place Q1
	Q1=brd.devices['Q1']
	Q1.setPos(mil2pcb(348), mil2pcb(860))
	Q1.setBottom(False)
	Q1.setRotation(270)
	Q1.setOrientation("")

	# Close to Q1 0805 is 80 mil high
	CQ1=brd.devices['CQ1']
	CQ1.setPos(mil2pcb(230), mil2pcb(845))
	CQ1.setBottom(False)
	CQ1.setRotation(90)
	CQ1.setOrientation("")

	# Close Q1
	CQ2=brd.devices['CQ2']
	CQ2.setPos(mil2pcb(470), mil2pcb(765))
	CQ2.setBottom(False)
	CQ2.setRotation(270)
	CQ2.setOrientation("")


	# LDO
	U2=brd.devices['U2']
	U2.setPos(mil2pcb(410), mil2pcb(230))
	U2.setBottom(False)
	U2.setRotation(90)
	U2.setOrientation("")
	#ldo.place_on_board(sch,U2,10,10)

	# C11
	C11=brd.devices['C11']
	C11.setPos(mil2pcb(550), mil2pcb(100))
	C11.setBottom(False)
	C11.setRotation(0)
	C11.setOrientation("")

	# not needed
	#C12.setPos(mil2pcb(380), mil2pcb(500))
	#C12.setBottom(False)
	#C12.setRotation(0)
	#C12.setOrientation("")

	C21=brd.devices['C21']
	C21.setPos(mil2pcb(370), mil2pcb(340))
	C21.setBottom(False)
	C21.setRotation(90)
	C21.setOrientation("")

	C22=brd.devices['C22']
	C22.setPos(mil2pcb(250), mil2pcb(340))
	C22.setBottom(False)
	C22.setRotation(180)
	C22.setOrientation("")


	# Place LED1 and R50 power indicator
	LED1=brd.devices['LED1']
	LED1.setPos(mil2pcb(490), mil2pcb(310))
	LED1.setBottom(False)
	LED1.setRotation(0)
	LED1.setOrientation("")

	R50=brd.devices['R50']
	R50.setPos(mil2pcb(570), mil2pcb(380))
	R50.setBottom(False)
	R50.setRotation(180)
	R50.setOrientation("")


	# LDO Routing and Geometry


	#LAYER 1;
	# GND Top layer
	#RECT (0.110 1.770) (0.205 1.890);
	GNDnet.geometry.append(Rectangle(mil2pcb(100.0), mil2pcb(330.0), mil2pcb(200.0), mil2pcb(210.0), 1))
	#RECT (0.105 2.005) (0.340 2.090);
	GNDnet.geometry.append(Rectangle(mil2pcb(100.0), mil2pcb(90.0), mil2pcb(340.0), mil2pcb(10.0), 1))
	#RECT (0.090 1.720) (0.215 1.780);
	GNDnet.geometry.append(Rectangle(mil2pcb(100.0), mil2pcb(380.0), mil2pcb(200.0), mil2pcb(320.0), 1))
	#RECT (0.345 1.840) (0.610 1.905);
	GNDnet.geometry.append(Rectangle(mil2pcb(345.0), mil2pcb(260.0), mil2pcb(610.0), mil2pcb(195.0), 1))
	#RECT (0.490 1.890) (0.610 1.980);
	GNDnet.geometry.append(Rectangle(mil2pcb(490.0), mil2pcb(210.0), mil2pcb(610.0), mil2pcb(110.0), 1))
	#RECT (0.390 1.700) (0.450 1.850);
	GNDnet.geometry.append(Rectangle(mil2pcb(390.0), mil2pcb(405.0), mil2pcb(450.0), mil2pcb(250.0), 1))
	# GND Bottom layer
	#RECT (0.235 1.915) (0.610 2.090);
	GNDnet.geometry.append(Rectangle(mil2pcb(235.0), mil2pcb(185.0), mil2pcb(610.0), mil2pcb(10.0), 2))
	#RECT (0.355 1.695) (0.475 1.920);
	GNDnet.geometry.append(Rectangle(mil2pcb(355.0), mil2pcb(405.0), mil2pcb(465.0), mil2pcb(180.0), 2))
	#RECT (0.355 1.840) (0.610 1.920);
	GNDnet.geometry.append(Rectangle(mil2pcb(355.0), mil2pcb(260.0), mil2pcb(610.0), mil2pcb(180.0), 2))
	# Stich GND Top and Bottom Layers
	# These two necessary
	via=CVia("STANDARDVIA",mil2pcb(260.0), mil2pcb(50.0),GNDnet.name,1)
	brd.vias.append(via)
	via=CVia("STANDARDVIA",mil2pcb(310.0), mil2pcb(50.0),GNDnet.name,2)
	brd.vias.append(via)
	# These two are optional, there is connection through pin
	via=CVia("STANDARDVIA",mil2pcb(530.0), mil2pcb(230.0),GNDnet.name,1)
	brd.vias.append(via)
	via=CVia("STANDARDVIA",mil2pcb(580.0), mil2pcb(230.0),GNDnet.name,2)
	brd.vias.append(via)

	# Connect to pin
	pin = MOD1.pins[4]
	pos1 = Point(pin.pos._x, pin.pos._y)
	pos2 = Point(pin.pos._x, pin.pos._y)
	pos1.offset(mil2pcb(-30.0), mil2pcb(30.0))
	pos2.offset(mil2pcb(50.0), mil2pcb(-30.0))
	GNDnet.geometry.append(Rectangle(pos1._x, pos1._y, pos2._x, pos2._y, 1))

	pin = MOD1.pins[39]
	pos1 = Point(pin.pos._x, pin.pos._y)
	pos2 = Point(pin.pos._x, pin.pos._y)
	pos1.offset(mil2pcb(30.0), mil2pcb(30.0))
	pos2.offset(mil2pcb(-50.0), mil2pcb(-30.0))
	GNDnet.geometry.append(Rectangle(pos1._x, pos1._y, pos2._x, pos2._y, 1))


	# 12V Top Layer
	VDD12Vnet = brd.nets['12V']
	#RECT (0.350 2.015) (0.610 2.090);
	VDD12Vnet.geometry.append(Rectangle(mil2pcb(350.0), mil2pcb(90.0), mil2pcb(610.0), mil2pcb(10.0), 1))
	# Connect to pin
	pin = MOD1.pinsbyname['VIN']
	pos1 = Point(pin.pos._x, pin.pos._y)
	pos2 = Point(pin.pos._x, pin.pos._y)
	pos1.offset(mil2pcb(30.0), mil2pcb(30.0))
	pos2.offset(mil2pcb(-50.0), mil2pcb(-30.0))
	VDD12Vnet.geometry.append(Rectangle(pos1._x, pos1._y, pos2._x, pos2._y, 1))


	# 3V3 Top Layer
	VDD3V3net = brd.nets['3V3']
	#RECT (0.225 1.695) (0.290 1.780);
	VDD3V3net.geometry.append(Rectangle(mil2pcb(225.0), mil2pcb(380.0), mil2pcb(290.0), mil2pcb(300.0), 1))
	#RECT (0.245 1.695) (0.335 1.940);
	VDD3V3net.geometry.append(Rectangle(mil2pcb(235.0), mil2pcb(405.0), mil2pcb(335.0), mil2pcb(160.0), 1))
	#RECT (0.245 1.930) (0.480 1.995);
	VDD3V3net.geometry.append(Rectangle(mil2pcb(235.0), mil2pcb(170.0), mil2pcb(480.0), mil2pcb(110.0), 1))
	# 3V3 Bottom Layer
	#RECT (0.245 1.660) (0.335 1.905);
	VDD3V3net.geometry.append(Rectangle(mil2pcb(235.0), mil2pcb(405.0), mil2pcb(335.0), mil2pcb(200.0), 2))
	# Stich 3V3 Top and Bottom Layers
	via=CVia("STANDARDVIA",mil2pcb(260.0), mil2pcb(230.0),VDD3V3net.name,11)
	brd.vias.append(via)
	via=CVia("STANDARDVIA",mil2pcb(310.0), mil2pcb(230.0),VDD3V3net.name,12)
	brd.vias.append(via)


	# Two rectangles on the Bottom to run along the board 
	# VDD3V3
	VDD3V3net.geometry.append(Rectangle(mil2pcb(235.0), mil2pcb(1400.0), mil2pcb(310.0), mil2pcb(400.0), 2))

	# GND
	GNDnet.geometry.append(Rectangle(mil2pcb(390.0), mil2pcb(1400.0), mil2pcb(465.0), mil2pcb(400.0), 2))


	# Serial TxD and RxD
	U4=brd.devices['U4']
	U4.setPos(mil2pcb(260), mil2pcb(570))
	U4.setBottom(False)
	U4.setRotation(180)
	U4.setOrientation("")

	# Diodes
	U5=brd.devices['U5']
	U5.setPos(mil2pcb(260), mil2pcb(670))
	U5.setBottom(False)
	U5.setRotation(180)
	U5.setOrientation("")

	# Reset
	U6=brd.devices['U6']
	U6.setPos(mil2pcb(260), mil2pcb(465))
	U6.setBottom(False)
	U6.setRotation(0)
	U6.setOrientation("")

	# place reset cap and resitor
	C30=brd.devices['C30']
	C30.setPos(mil2pcb(560), mil2pcb(460))
	C30.setBottom(False)
	C30.setRotation(270)
	C30.setOrientation("")

	R30=brd.devices['R30']
	R30.setPos(mil2pcb(560), mil2pcb(665))
	R30.setBottom(False)
	R30.setRotation(270)
	R30.setOrientation("")

	C40=brd.devices['C40']
	C40.setPos(mil2pcb(490), mil2pcb(470))
	C40.setBottom(False)
	C40.setRotation(180)
	C40.setOrientation("")

	R40=brd.devices['R40']
	R40.setPos(mil2pcb(410), mil2pcb(570))
	R40.setBottom(False)
	R40.setRotation(0)
	R40.setOrientation("")

	R41=brd.devices['R41']
	R41.setPos(mil2pcb(410), mil2pcb(670))
	R41.setBottom(False)
	R41.setRotation(0)
	R41.setOrientation("")


	# place Single Wire Debug
	SWDCON=brd.devices['SWDCON']
	SWDCON.setPos(mil2pcb(445) , mil2pcb(1540))
	SWDCON.setRotation(270)
	SWDCON.setOrientation("")

	#Place U3, FLASH  origin in the center
	U3=brd.devices['U3']
	U3.setPos(mil2pcb(350), mil2pcb(1900))
	U3.setBottom(False)
	U3.setRotation(90)
	U3.setOrientation("")

	R60=brd.devices['R60']
	R60.setPos(mil2pcb(240), mil2pcb(1630))
	R60.setBottom(False)
	R60.setRotation(0)
	R60.setOrientation("")

	R61=brd.devices['R61']
	R61.setPos(mil2pcb(240), mil2pcb(1770))
	R61.setBottom(False)
	R61.setRotation(0)
	R61.setOrientation("")

	R62=brd.devices['R62']
	R62.setPos(mil2pcb(240), mil2pcb(1700))
	R62.setBottom(False)
	R62.setRotation(0)
	R62.setOrientation("")



	# place serial con on the bottom horizontally
	CON3=brd.devices['CON3']
	CON3.setPos(mil2pcb(600) , mil2pcb(2050))
	CON3.setBottom(False)
	CON3.setRotation(180)
	CON3.setOrientation("")

	# Jumper
	J1=brd.devices['J1']
	J1.setPos(mil2pcb(135) , mil2pcb(1875))
	J1.setBottom(False)
	J1.setRotation(270)
	J1.setOrientation("")


	# Texts
	text = Text("(c) Hobby-Robotics, LLC",mil2pcb(340) , mil2pcb(1300))
	text.layernum = bottomlayer.num
	text.size = mil2pcb(22)
	text.thickness = text.size * 0.15
	text.direction = 1
	text.orientation = 90.0
	text.scale = 1.0
	# too small, skip it
	#brd.geometry.append(text)


	text = Text("STM32DIP40",mil2pcb(370) , mil2pcb(1830))
	text.layernum = bottomlayer.num
	text.size = mil2pcb(22)
	text.thickness = text.size * 0.15
	text.direction = 1
	text.orientation = 180
	text.scale = 1.0
	# too small, skip it
	#brd.geometry.append(text)


	text = Text("(c)",mil2pcb(420) , mil2pcb(1785))
	text.layernum = bottomlayer.num
	text.size = mil2pcb(42)
	text.thickness = text.size * 0.25
	text.direction = 1
	text.orientation = 180
	text.scale = 1.0
	brd.geometry.append(text)

	text = Text("HBBR",mil2pcb(420) , mil2pcb(1835))
	text.layernum = bottomlayer.num
	text.size = mil2pcb(42)
	text.thickness = text.size * 0.25
	text.direction = 1
	text.orientation = 180
	text.scale = 1.0
	brd.geometry.append(text)

	text = Text("2007",mil2pcb(420) , mil2pcb(1885))
	text.layernum = bottomlayer.num
	text.size = mil2pcb(42)
	text.thickness = text.size * 0.25
	text.direction = 1
	text.orientation = 180
	text.scale = 1.0
	brd.geometry.append(text)

	return brd



if __name__ == "__main__":

	# import schematic
	sch = import_schematic()
	brd = make(sch, 'stm32dip40', 'stm32dip40')

