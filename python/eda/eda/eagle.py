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


import copy

from edautils import *
from eda import *

CRLF = "\n"

EaglePredefinedLayers = """
Predefined EAGLE Layers Layout  
1   Top	Tracks, top side
2   Route2		Inner layer (signal or supply)
3   Route3		Inner layer (signal or supply)
4   Route4		Inner layer (signal or supply)
5   Route5		Inner layer (signal or supply)
6   Route6		Inner layer (signal or supply)
7   Route7		Inner layer (signal or supply)
8   Route8		Inner layer (signal or supply)
9   Route9		Inner layer (signal or supply)
10  Route10		Inner layer (signal or supply)
11  Route11		Inner layer (signal or supply)
12  Route12		Inner layer (signal or supply)

13  Route13		Inner layer (signal or supply)
14  Route14		Inner layer (signal or supply)
15  Route15		Inner layer (signal or supply)
16  Bottom		Tracks, bottom side
17  Pads		Pads (through-hole)
18  Vias		Vias (through-hole)
19  Unrouted	Airwires (rubberbands)
20  Dimension	Board outlines (circles for holes)
21  tPlace		Silk screen, top side
22  bPlace		Silk screen, bottom side
23  tOrigins	Origins, top side
24  bOrigins	Origins, bottom side
25  tNames		Service print, top side
26  bNames		Service print, bottom side
27  tValues		Component VALUE, top side
28  bValues		Component VALUE, bottom side
29  tStop		Solder stop mask, top side
30  bStop		Solder stop mask, bottom side
31  tCream		Solder cream, top side
32  bCream		Solder cream, bottom side
33  tFinish		Finish, top side
34  bFinish		Finish, bottom side
35  tGlue		Glue mask, top side
36  bGlue		Glue mask, bottom side
37  tTest		Test and adjustment inf., top side
38  bTest		Test and adjustment inf. bottom side
39  tKeepout	Nogo areas for components, top side
40  bKeepout	Nogo areas for components, bottom side
41  tRestrict	Nogo areas for tracks, top side
42  bRestrict	Nogo areas for tracks, bottom side
43  vRestrict	Nogo areas for via-holes
44  Drills		Conducting through-holes
45  Holes		Non-conducting holes
46  Milling		Milling
47  Measures	Measures
48  Document	General documentation
49  Reference	Reference marks
51  tDocu		Part documentation, top side
52  bDocu		Part documentation, bottom side

Schematic 

91  Nets		Nets
92  Busses		Buses
93  Pins		Connection points for component symbolswith additional information
94  Symbols		Shapes of component symbols
95  Names		Names of component symbols
96  Values		Values/component types
"""



#layerTOP = 1
#layerBOTTOM = 2
#layerGND = 3
#layerVCC = 3
#layerBLOCKTOP = 5
#layerBLOCKBOTTOM = 6
#layerSIGNAL3 = 7
#layerSIGNAL4 = 8
#layerSILK = 9
#layerRATS = 10
#layerPINPADS = 11
#layerVIAS = 12
#layerSOLDERMASK = 13

class CEagle:
	" Eagle class "
	def __init__(self, sch=None,brd=None):
		self.name=""
		self.sch=sch
		self.brd=brd
		self.origin = Point(0,0)
		self.script_path="F:/usr/local/hobby-robotics/src/hbbrbasic/hardware/ulp/hbbr"
		self.layerTop = 1
		self.layerBottom = 16
		self.layerVias = 18
		self.layerUnrouted = 19
		self.layerDimension = 20
		self.layer_tStop = 29
		self.layer_bStop = 31
		self.layer_tRestrict = 41
		self.layer_bRestrict = 42
		self.layer_tDocu = 51
		self.layer_bDocu = 52
		
	def normalizeSize(self,size):
		return size * 0.00001

	def normalizePoint(self, pt):
		offy = self.brd.bbox.sizeY()
		pt._y = offy - pt._y
		pt.scale(0.00001)
		pt.offset(self.origin._x, self.origin._y)
		
	def normalizeRelativePoint(self, pt=Point(0, 0)):
		pt._y = 0 - pt._y
		pt.scale(0.00001)
		
	def normalizeLine(self, line):
		for ptt in line.points:
			pt = Point(ptt._x, ptt._y)
			self.normalizePoint(pt)
		line.calcBBox()
				
	def normalizeRelativeLine(self, line):
		for ptt in line.points:
			pt = Point(ptt._x, ptt._y)
			self.normalizeRelativePoint(pt)
		line.calcBBox()
		
	def normalizeRectangle(self, rect):
		rect.normalize()
		self.normalizePoint(rect.ll)
		self.normalizePoint(rect.ur)
		
	def normalizeRelativeRectangle(self, rect):
		rect.normalize()
		self.normalizeRelativePoint(rect.ll)
		self.normalizeRelativePoint(rect.ur)
		
	def normalizePolygon(self, poly):
		self.normalizeLine(poly)
		
	def normalizeRelativePolygon(self, poly):
		self.normalizeRelativeLine(poly)
		
	def normalizeText(self, text):
		self.normalizePoint(text)

	def normalizeRelativeText(self, text):
		self.normalizeRelativeLine(text)
		
	def normalizeAngle(self, angle):
		return angle
			
	def normalizeArc(self, arc):
		self.normalizePoint(arc)
		arc.width     = self.normalizeSize(arc.width)
		arc.height    = self.normalizeSize(arc.height)
		arc.sangle    = self.normalizeAngle(arc.sangle)
		arc.dangle    = self.normalizeAngle(arc.dangle)
		arc.thickness = self.normalizeSize(arc.thickness)
		
		
	def normalizeRelativeArc(self, arc):
		self.normalizeRelativePoint(arc)
		arc.width     = self.normalizeSize(arc.width)
		arc.height    = self.normalizeSize(arc.height)
		arc.sangle    = self.normalizeAngle(arc.sangle)
		arc.dangle    = self.normalizeAngle(arc.dangle)
		arc.thickness = self.normalizeSize(arc.thickness)
		
	def mapLayer(self, layer):
		
		if layer == 0:	# to Unrouted
				layer = self.layerUnrouted
				
		if layer == layerTOP:				# 1  to TOP
				layer = self.layerTop
				
		if layer == layerBOTTOM:			# 2 to BOTTOM
				layer = self.layerBottom
				
		if layer == layerBLOCKTOP:			# 5  to TOP
				layer = self.layer_tRestrict
				
		if layer == layerBLOCKBOTTOM:		# 6 to BOTTOM
				layer = self.layer_bRestrict
				
		if layer == layerSILK:				# 7 to tDocu
				layer = self.layer_tDocu
				
		if layer == layerRATS:				# 10 to Unrouted
				layer = self.layerUnrouted
				
		if layer == layerSOLDERMASK:		# 13 to Unrouted
				layer = self.layer_tStop
				
		return layer
	
	def genGeom(self,geom):
		ns = ''			
		layer = self.mapLayer(geom.layernum)
			
		if isinstance(geom, Rectangle) :
			rect = copy.copy(geom)					# shallow copy
			self.normalizeRectangle(rect)
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "RECT (" + str(rect.ll._x) + " " + str(rect.ll._y) + ") (" + str(rect.ur._x) + " " + str(rect.ur._y) + ");" + CRLF

		if isinstance(geom, Line) :
			line =  copy.copy(geom)					# shallow copy
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "SET WIRE_BEND 2;"  + CRLF				# straight connection
	
			prevpt  = Point(0,0)
			first = True
			for ptt in line.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizePoint(pt)
				thickness = self.normalizeSize(line.thickness) #
				if first:
					first = False	
					prevpt = Point(pt._x, pt._y)
				else:
					ns += "WIRE " + str(thickness) + " (" + str(prevpt) +") (" + str(pt) +");" + CRLF
					prevpt = Point(pt._x, pt._y)
					

		if isinstance(geom, Polygon) :
			poly =  copy.copy(geom)					# shallow copy
					
			thickness = self.normalizeSize(poly.thickness)
			
			# needs to check for existance of netname
			netname = ''
			
			ns += "SET WIRE_BEND 2;" + CRLF
			ns += "LAYER " + str(layer) + ";" + CRLF
			
			ns += "POLY '" + netname + "' " +  str(thickness)
			for ptt in poly.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizePoint(pt)
				ns += " (" + str(pt) +") "
			ns += ";" + CRLF

		# Unfinished
		if isinstance(geom, Arc) :
			arc =  copy.copy(geom)					# shallow copy
			self.normalizeArc(arc)
			
			# needs to check for existance of netname
			netname = ''
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			
			# ARC or CIRCLE
			if arc.sangle <= 0 and arc.dangle >= 360:
				circumference  = ( arc.width + arc.height) / 2	# for now but should be changed
				thickness = arc.thickness
				# CIRCLE
				#CIRCLE (0 0) (1 0);
				pt = Point(arc._x, arc._y)
				pt2 = Point(pt._x + circumference, pt._y)
				ns += "CIRCLE (" + str(pt) +") " + "(" + str(pt2) + ");" + CRLF
				ns += "CHANGE WIDTH " +  str(thickness) + " (" + str(pt) +");"  + CRLF	# 0 thickness - filled cicle
			else:
				# ARC ['signal_name'] [CW | CCW] [ROUND | FLAT] [width]
				# ARC CW (0 1) (0 -1) (1 0);		
				ns += "ARC '" + netname + "' " +  str(thickness)
				ns += ";" + CRLF
			
			
			
		if isinstance(geom, Text) :
			text = copy.copy(geom)					# shallow copy
			pt = Point(text._x, text._y)
			self.normalizePoint(pt)
				
			if layer == self.layerBottom :
				mirror = "M"
			else:
				mirror = ""
				
			size = self.normalizeSize(text.size)
			thickness = self.normalizeSize(text.thickness)
			ratio = int(thickness / size * 100)
			if ratio > 31:									# Maximum ratio according to help
				ratio = 31
		
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "TEXT '" + text.text +  "' " + mirror + "R" + str(text.orientation) + " (" + str(pt) + ");" + CRLF
			ns += "CHANGE SIZE "  + str(size)  + " ("  + str(pt) + ");" + CRLF
			ns += "CHANGE RATIO " + str(ratio) + " ("  + str(pt) + ");" + CRLF
					
		return ns
	
	# gen sch layers scr"
	def genSchLayersScr(self):
		ns = ''
		ns += "GRID INCH 0.001" + CRLF
		ns += "LAYER 1 Top;" + CRLF
		ns += "LAYER 16 Bottom;" + CRLF	# default
		ns += "LAYER 17 Pads;" + CRLF
		ns += "LAYER 18 Vias;" + CRLF
		ns += "LAYER 19 Unrouted;" + CRLF
		ns += "LAYER 20 Dimension;" + CRLF
		ns += "LAYER 21 tPlace;" + CRLF
		ns += "LAYER 22 bPlace;" + CRLF
		ns += "LAYER 23 tOrigins;" + CRLF
		ns += "LAYER 24 bOrigins;" + CRLF
		ns += "LAYER 25 tNames;" + CRLF
		ns += "LAYER 26 bNames;" + CRLF
		ns += "LAYER 27 tValues;" + CRLF
		ns += "LAYER 28 bValues;" + CRLF
		ns += "LAYER 29 tStop;" + CRLF
		ns += "LAYER 30 bStop;" + CRLF
		ns += "LAYER 31 tCream;" + CRLF
		ns += "LAYER 32 bCream;" + CRLF
		ns += "LAYER 33 tFinish;" + CRLF
		ns += "LAYER 34 bFinish;" + CRLF
		ns += "LAYER 35 tGlue;" + CRLF
		ns += "LAYER 36 bGlue;" + CRLF
		ns += "LAYER 37 tTest;" + CRLF
		ns += "LAYER 38 bTest;" + CRLF
		ns += "LAYER 39 tKeepout;" + CRLF
		ns += "LAYER 40 bKeepout;" + CRLF
		ns += "LAYER 41 tRestrict;" + CRLF
		ns += "LAYER 42 bRestrict;" + CRLF
		ns += "LAYER 43 vRestrict;" + CRLF
		ns += "LAYER 44 Drills;" + CRLF
		ns += "LAYER 45 Holes;" + CRLF
		ns += "LAYER 46 Milling;" + CRLF
		ns += "LAYER 47 Measures;" + CRLF
		ns += "LAYER 48 Document;" + CRLF
		ns += "LAYER 49 Reference;" + CRLF
		ns += "LAYER 50 dxf;" + CRLF
		ns += "LAYER 51 tDocu;" + CRLF
		ns += "LAYER 52 bDocu;" + CRLF
		ns += "LAYER 100 DocFrame;" + CRLF
		ns += "LAYER 250 Descript;" + CRLF
		ns += "LAYER 251 SMDround;" + CRLF
		return ns;



#ADD 'C1' 'G$1' POLARISED_CASE_H@ipc-7351-capacitor R0.000 (-0.300 3.300);
#ADD 'Q1' 'G$1' -PNP-SOT23-EBC@transistor R0.000 (1.600 3.300);
#ADD 'Q5' 'G$1' MMBT2222ALT1-NPN-SOT23-BEC@transistor R0.000 (0.900 2.800);
#ADD 'V1' 'GND' GND@supply2 R0.000 (0.600 0.100);
#ADD 'V2' 'G$1' VCC@supply2 R0.000 (5.600 4.200);

	# gen sch add scr"
	def genSchAddScr(self):
		ns = ''
		ns += "GRID INCH 0.005" + CRLF
		ns += "LAYER 91 Nets;" + CRLF
		ns += "LAYER 92 Busses;" + CRLF
		ns += "LAYER 93 Pins;" + CRLF
		ns += "LAYER 94 Symbols;" + CRLF
		ns += "LAYER 95 Names;" + CRLF
		ns += "LAYER 96 Values;" + CRLF
		ns += "LAYER 250 Descript;" + CRLF
		ns += "LAYER 251 SMDround;" + CRLF
		ns += "DISPLAY -PINS" + CRLF
		ns += CRLF
		ns += "EDIT .S1" + CRLF
		ns += "SET WIRE_BEND 2;" + CRLF
		ns += "CHANGE STYLE 'Continuous'" + CRLF
		
		#for dev in self.sch.devices:
		for devname in self.sch.devices:
			dev = self.sch.devices[devname]
			position = Point(dev.position._x,dev.position._y)
			position.scale(0.00001)
			#position._y = 0 - position._y
			#ns += "ADD '" + str(dev.refid) + "' 'G$1' " + str(dev.name) + "@" + str(dev.libname) + " " + dev.orientation + "R%.3f"% (dev.rotation) +" (" + str(dev.position) + ");" + CRLF   
			ns += "ADD '" + str(dev.refid) + "' " + str(dev.name) + "@" + str(dev.libname) + " " + dev.orientation + "R%.3f"% (dev.rotation) +" (" + str(position) + ");" + CRLF   
		ns += "GRID LAST" + CRLF
		
		return ns
		
	# gen cmd sch net-connect"
	# this relies on external script, not a good idea
	def genSchNetConnectScr(self):
		ns = ''
		runcmd="run " + self.script_path + "/cmd-sch-net-connect.ulp"
		
		for netname in self.sch.nets:
			net = self.sch.nets[netname]	
			prevdev=""
			prevpin=""
			l = ""
			first = 1
			for node in net.nodes:
				if first:
					first = 0
					prevdev=node.dev
					prevpin=node.pin
				else:
					l = runcmd +  " '" + net.name + "' '" + prevdev.refid + "' " + str(prevpin.num) + " '" + node.dev.refid + "' " + str(node.pin.num) + ";" + CRLF
					ns += l	
					prevdev=node.dev
					prevpin=node.pin
					
		# string function
		return ns
	

	# generate netlist for schematic
	# straight connections between pins
	def generateSchematicNetlist(self):
		ns = ''
				
		for netname in self.sch.nets:
			net = self.sch.nets[netname]	
			prevdev=""
			prevpin=""
			l = ""
			first = True
			for node in net.nodes:
				if first:
					first = False
					prevdev=node.dev
					prevpin=node.pin
				else:
					prevpos = prevpin.pos
					prevpos.scale(0.00001)
					pos = node.pin.pos
					pos.scale(0.00001)
					ns += "NET '" + netname + "' (" + " %5.3f"%(prevpos._x) + " %5.3f"%(prevpos._y) + ") (" + " %5.3f"%(pos._x) +  " %5.3f"%(pos._x) + ");\n"
					prevdev=node.dev
					prevpin=node.pin		
		# string function
		return ns
	
	
	
	# gen sch netlist listing
	def genSchNetlistLst(self):
		ns = ''
		CRLF = "\n"
		ns = "Netlist" + CRLF
		ns += CRLF
		ns += "Exported" + CRLF
		ns += CRLF
		ns += "EAGLE Version 4.11" + CRLF
		ns += CRLF
		ns += expandtab("Net\tPart\tPad\tPin\tSheet",8) + CRLF
		for netname in self.sch.nets:
			net = self.sch.nets[netname]
			ns += CRLF
			ns += "Change Class 0;" + CRLF
			l = net.name + " "
			first = 1
			for node in net.nodes:
				if first:
					first = 0
					l += "\t"
				else:
					l += "\t"
				
				# use node.pin.name as pin
				l += str(node.dev.refid) +  "\t" + str(node.pin.name) + "\t" + str(node.pin.name) + "\t1" + CRLF
				#l += str(node.dev.refid) +  "\t" + str(node.pin.num) + "\t" + str(node.pin) + "\t1" + CRLF
					
			ns += expandtab(str(l),8)
		# string function
		return ns
	
	# gen sch netlist script
	def genSchNetlistScr(self):
		ns = ''
		CRLF = "\n"
		ns = "# Netlist script" + CRLF
		ns += "# EAGLE Version 4.11" + CRLF
		ns += "# Copyright Hobby-Robotics" + CRLF
		ns += expandtab("#Net\tPart\tPad",12) + CRLF
		ns += CRLF
		for netname in self.sch.nets:
			net = self.sch.nets[netname]
			ns += CRLF
			ns += "Change Class 0;" + CRLF
			l = "Signal " + " '" + net.name + "'"
			first = 1
			for node in net.nodes:
				if first:
					first = 0
					l += "\t'"
				else:
					l += "\t\t'"
				
				# By pin name	
				#l += node.dev.refid + "'\t'" + node.pin.name + "' \\" + CRLF
				# By pin number
				l += node.dev.refid + "'\t " + str(node.pin.num) + " \\" + CRLF
					
			ns += expandtab(str(l),12)
			ns += "\t\t\t;" + CRLF
		# string function
		return ns
		
		
	def generateNetConnections(self,net):		
		ns = ''
		
		offy = self.brd.bbox.sizeY()
		
		for line in net.route:
			
			layer = 91 #line.layernum
			
			if layer == 0:		# unrouted
				continue
							
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "SET WIRE_BEND 2;"  + CRLF				# straight connection
	
			prevpt  = Point(0,0)
			firstpt = Point(0,0)
			first = True
			for ptt in line.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizePoint(pt)
				thickness = 0.01 # line.thickness * 0.00001
				if first:
					first = False	
					firstpt = Point(pt._x, pt._y)
					prevpt = Point(pt._x, pt._y)
				else:
					ns += "WIRE " + str(thickness) + " (" + str(prevpt) +") (" + str(pt) +");" + CRLF
					prevpt = Point(pt._x, pt._y)
									
		return ns
	
	def generateConnections(self):
		# here go all of the layer elements
		ns = ''
		for net in self.sch.nets.values():
			ns += self.generateNetConnections(net)
		return ns
	
	
# Package geometry
	def genPacGeom(self,geom):
		ns = ''			
		#default is 51 tDocu
		
###		print  "geom.layernum " + str(geom.layernum)
		if geom.layernum == 0:
			layer = 51
		else:
			layer = self.mapLayer(geom.layernum)
		
###		print  "mapped layer " + str(layer)
		
		if isinstance(geom, Rectangle) :
			rect = copy.copy(geom)					# shallow copy
			self.normalizeRelativeRectangle(rect)
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "RECT (" + str(rect.ll._x) + " " + str(rect.ll._y) + ") (" + str(rect.ur._x) + " " + str(rect.ur._y) + ");" + CRLF

		if isinstance(geom, Line) :
			line =  copy.copy(geom)					# shallow copy
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "SET WIRE_BEND 2;"  + CRLF				# straight connection
	
			prevpt  = Point(0,0)
			first = True
			for ptt in line.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizeRelativePoint(pt)
				thickness = self.normalizeSize(line.thickness) #
				if first:
					first = False	
					prevpt = Point(pt._x, pt._y)
				else:
					ns += "WIRE " + str(thickness) + " (" + str(prevpt) +") (" + str(pt) +");" + CRLF
					prevpt = Point(pt._x, pt._y)
					

		if isinstance(geom, Polygon) :
			poly =  copy.copy(geom)					# shallow copy
					
			thickness = self.normalizeSize(poly.thickness)
			
			# needs to check for existance of netname
			netname = ''
			
			ns += "SET WIRE_BEND 2;" + CRLF
			ns += "LAYER " + str(layer) + ";" + CRLF
			
			ns += "POLY '" + netname + "' " +  str(thickness)
			for ptt in poly.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizeRelativePoint(pt)
				ns += " (" + str(pt) +") "
			ns += ";" + CRLF

		# Unfinished
		if isinstance(geom, Arc) :
			arc =  copy.copy(geom)					# shallow copy
			self.normalizeRelativeArc(arc)
			
			# needs to check for existance of netname
			netname = ''
			
			ns += "LAYER " + str(layer) + ";" + CRLF
			
			# ARC or CIRCLE
			if arc.sangle <= 0 and arc.dangle >= 360:
				circumference  = ( arc.width + arc.height) / 2	# for now but should be changed
				thickness = arc.thickness
				# CIRCLE
				#CIRCLE (0 0) (1 0);
				pt = Point(arc._x, arc._y)
				pt2 = Point(pt._x + circumference, pt._y)
				ns += "CIRCLE (" + str(pt) +") " + "(" + str(pt2) + ");" + CRLF
				ns += "CHANGE WIDTH " +  str(thickness) + " (" + str(pt) +");"  + CRLF	# 0 thickness - filled cicle
			else:
				# ARC ['signal_name'] [CW | CCW] [ROUND | FLAT] [width]
				# ARC CW (0 1) (0 -1) (1 0);		
				thickness = arc.thickness
				ns += "ARC " +  str(thickness)
				ns += ";" + CRLF
			
			
			
		if isinstance(geom, Text) :
			text = copy.copy(geom)					# shallow copy
			pt = Point(text._x, text._y)
			self.normalizeRelativePoint(pt)
				
			if layer == self.layerBottom :
				mirror = "M"
			else:
				mirror = ""
				
			size = self.normalizeSize(text.size)
			thickness = self.normalizeSize(text.thickness)
			ratio = int(thickness / size * 100)
			if ratio > 31:									# Maximum ratio according to help
				ratio = 31
		
			ns += "LAYER " + str(layer) + ";" + CRLF
			ns += "TEXT '" + text.text +  "' " + mirror + "R" + str(text.orientation) + " (" + str(pt) + ");" + CRLF
			ns += "CHANGE SIZE "  + str(size)  + " ("  + str(pt) + ");" + CRLF
			ns += "CHANGE RATIO " + str(ratio) + " ("  + str(pt) + ");" + CRLF
					
		return ns
		
			
#Edit LQFP64.pac;
#Description '<b>L-Quad Flat Package, 64 leads <p>';
#Grid mm;
#Layer 1;
#Smd '1' 0.20 0.75 -0 R0 (-3.75 -5.75);

# SMD [x_width y_width] [-roundness] [orientation] [flags] ['name'] ...
# 
# Need to set the drill size before PAD
# CHANGE DRILL [drill size];
# PAD [diameter] [shape] [orientation] [flags] ['name'] ...
# [shape]
# Square	
# Round	
# Octagon	octagonal
# Long	elongated
# Offset	elongated with offset
	def generatePackage(self,package):
		ns = ''
		
		if package.tag ==1:
			return ns
		package.tag = 1
	
		ns += "Edit " + package.name + ".pac;" + CRLF
		ns += "Description '" + package.description + "';" + CRLF
		ns += "GRID INCH 0.001;" + CRLF
		ns += "Layer 1;" + CRLF
		ns += "" + CRLF
		
		terminals = len(package.pins)
		for num in range(terminals):
			pin = package.pins[num+1]
			pt = Point(pin.pos._x, pin.pos._y)
			self.normalizeRelativePoint(pt)
			#pt.scale(0.00001)
			#pt._y = 0 - pt._y
			sizex = self.normalizeSize(pin.pad.sizex) # * 0.00001
			sizey = self.normalizeSize(pin.pad.sizey) # * 0.00001
			drill = self.normalizeSize(pin.pad.drill) # * 0.00001
			if pin.smt:
				ns += "SMD '" + str(num+1) + "' " + str(sizex) + " " + str(sizey) + " -0 R0 (" + str(pt) +");" + CRLF
			else:
				ns += "CHANGE DRILL " + str(drill) + ";" + CRLF
			
				shape = "ROUND"			# default is ROUND
				# might not have shape defined
				try:
###					print "pin.shape " + pin.shape
					
					if pin.shape == "square":
						shape = "SQUARE"
					else:
						shape = "ROUND"
				except:
					pass
			
###				print "shape " + shape
						
				ns += "PAD '" + str(num+1) + "' " + shape + "  " + str(sizex) + " R0 (" + str(pt) +");" + CRLF
				pass
			
		# Board geometry
		for geom in package.geometry:
			ns += self.genPacGeom(geom)
		return ns
	
	def generatePackages(self):
		ns = ''
		CRLF = "\n"
		ns += "" + CRLF
		
		for packagename in self.brd.packages:
			ns += self.generatePackage(self.brd.packages[packagename])
		return ns
	
	
#Edit LPC2148.sym;
#grid mm;
#Pin 'P1.16/TRACEPKT0'             I/O None Short R0 Both 0 (-30.48 48.26);
	
	def generateSymbol(self,symbol):		
		ns = ''
		
		if symbol.tag == 1:
			return ns
		symbol.tag = 1
		
		CRLF = "\n"
		
###		print " symbol " + symbol.name
		
		ns += "" + CRLF
		ns += "Edit " + symbol.name + ".sym" + CRLF
		ns += "GRID INCH 0.001" + CRLF
			
		terminals = len(symbol.ports)
		for num in range(terminals):
			port = symbol.ports[num+1]
			pt = Point(port.pos._x, port.pos._y)
			self.normalizeRelativePoint(pt)
			#pt.scale(0.00001)
			#pt._y = 0 - pt._y
			orientation = port.orientation
			ns += "Pin '"  + port.name + "'  I/O None Short " +  "R" + str(orientation) +  " Both 0 (" + str(pt) +");" + CRLF
			
		ns += "" + CRLF
		return ns
	
	def generateDevice(self,dev):
		ns = ''
		
		if dev.tag ==1:
			return ns
		dev.tag = 1
		
		ns += "" + CRLF
		ns += "Edit " + dev.name + ".dev" + CRLF
		ns += "Description '" + str(dev.val) + "';" + CRLF
		ns += "GRID INCH 0.001" + CRLF
		ns += "Value On;"  + CRLF
		ns += "Add " + dev.symbolname + " '1' Next 0 (0 0); "  + CRLF
		ns += "Package '" + dev.package.name + "' '''''';"   + CRLF
		ns += "Technology '';"  + CRLF
		
		terminals = len(dev.pins)
		for num in range(terminals):
			pin = dev.pins[num+1]
			ns += "Connect '"  + pin.name + "' '" + str(num+1) + "'" + CRLF
			
		ns += "" + CRLF
		return ns
		
	def generateDevices(self):
		ns = ''
		CRLF = "\n"
		ns += "" + CRLF
		for devname in self.brd.devices:
			device = self.brd.devices[devname]
			#print device
			symbol = self.sch.symbols[device.symbolname]
			ns += self.generateSymbol(symbol)
			ns += self.generateDevice(device)
		
		ns += "" + CRLF
		return ns
	
	
	
	def generateNetRoutes(self,net):		
		ns = ''
		CRLF = "\n"
###		print "out net " + net.name
		
		offy = self.brd.bbox.sizeY()
		
		for line in net.route:
			ns += self.genGeom(line)
		return ns
	
	def generateRoutes(self):
		# here go all of the layer elements
		ns = ''
		for net in self.brd.nets.values():
			ns += self.generateNetRoutes(net)
		return ns
	
	def generateVias(self):
		ns = ''
		CRLF = "\n"
###		print " board vias " + str(len(self.brd.vias))
		offy = self.brd.bbox.sizeY()
		for via in self.brd.vias:
###			print "VIA " + via.name
			pt = Point(via.pos._x,via.pos._y)
			self.normalizePoint(pt)
			#pt._y = offy - pt._y
			#pt.scale(0.00001)
			ns += "VIA '" + via.netname + "' 0.020 Round 1-16 STOP (" + str(pt) + ")" + CRLF
		return ns;
	
#GRID INCH 0.001
#LAYER Dimension
#WIRE 0.000 (-0.019 -0.025) (3.919 -0.025);
#WIRE 0.000 (3.919 -0.025) (3.919 3.125);
#WIRE 0.000 (3.919 3.125) (-0.019 3.125);
#WIRE 0.000 (-0.019 3.125) (-0.019 -0.025);

	# gen brd board scr"
	def genBrdBoardScr(self):
		ns = ''
		CRLF = "\n"
		ns += "GRID INCH 0.001;" + CRLF
		ns += CRLF
		ns += "LAYER Dimension;" + CRLF
		offy = self.brd.bbox.sizeY()
		prevpt  = Point(0,0)
		prevpt.scale(0.00001)
		firstpt = Point(0,offy)
		firstpt.scale(0.00001)
		first = True
		for ptt in self.brd.outline:
			pt = Point(ptt._x, ptt._y)
			self.normalizePoint(pt)
			#pt._y = offy - pt._y		
			#pt.scale(0.00001)
			if first:
				first = False	
				firstpt == pt
				prevpt = pt
			else:
				ns += "WIRE 0.000 (" + str(prevpt) +") (" + str(pt) +");" + CRLF
				prevpt = pt
		# last one
		ns += "WIRE 0.000 (" + str(prevpt) +") (" + str(firstpt) +");" + CRLF
		return ns



		
#LAYER 1;
#RECT (0.490 1.890) (0.610 1.980);
	def generatePour(self):
		ns = ''
		prevpt = Point(0,0)
		first = True
		ptcnt = 0	

		geomcnt = 0
		for net in self.brd.nets.values():
			
			for geom in net.geometry:
				geomcnt += 1
				# Handle rectangle
				#if type(geom) is Rectangle :
				if isinstance(geom, Rectangle) :
					ns += self.genGeom(geom)
					
		for pour in self.brd.pours:
			#map layers
			layer = pour.layernum
			if layer == 0:		# unrouted
				continue		
			layer = self.mapLayer(pour.layernum)
			thickness = self.normalizeSize(pour.poly.thickness)
			isolate = self.normalizeSize(pour.isolate)
			ns += "SET WIRE_BEND 2;" + CRLF
			ns += "LAYER " + str(layer) + ";" + CRLF
			
			ns += "POLY '" + pour.netname + "' " +  str(thickness)
			for ptt in pour.poly.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizePoint(pt)
				ns += " (" + str(pt) +") "
			ns += ";" + CRLF
			
			pt = Point(pour.poly.points[0]._x, pour.poly.points[0]._y)
			self.normalizePoint(pt)
			ns += "CHANGE ISOLATE " + str(isolate) + " (" + str(pt) + ");" + CRLF
			
			#pour.fill= 0				# fill 0 - solid 1 - hatch
			if pour.thermals:
				ns += "CHANGE THERMALS ON  (" + str(pt) + ");" + CRLF
			else:
				ns += "CHANGE THERMALS OFF (" + str(pt) + ");" + CRLF
				
			if pour.orphans:
				ns += "CHANGE ORPHANS ON  (" + str(pt) + ");" + CRLF
			else:
				ns += "CHANGE ORPHANS OFF (" + str(pt) + ");" + CRLF
							
		# Board geometry
		for geom in self.brd.geometry:
			ns += self.genGeom(geom)
							
		ns += CRLF
		return ns
	
	

#ADD 'C1' CAPAE1350X1350N@ipc-7351-capacitor R0.000 (-0.950 0.350);	
	# gen brd place scr"
	def genBrdPlaceScr(self):
		ns = ''
		CRLF = "\n"
		offy = self.brd.bbox.sizeY()

		for devname in self.brd.devices:
			dev = self.brd.devices[devname]
			libname = dev.libname
			#libname = "stm32dip40"
			orientation = dev.orientation				
			rotation = dev.rotation
			pt = Point(dev.position._x, dev.position._y)
			self.normalizePoint(pt)
			#pt = dev.position
			#pt._y = offy - pt._y
			#pt.scale(0.00001)
			# By package, works but no pins and nets?
			name = dev.packagename
			# By device name does not work
			#name = dev.name
			
			if dev.bottom:							# placed on bottom 
				orientation = "M" + orientation
				# Eagle mirrors by mirroring in horizontal axis so if origin is not in the center
				# X offset for position has to be calculated from the span in X between pins on opposite sides
				maxX, minX = dev.maxXminX()
				# Y offset for position has to be calculated from the span in Y between pins on opposite sides
				maxY, minY = dev.maxYminY()
				# does it depend on roation?
				
				if rotation == 0:
					pt._x = pt._x + self.normalizeSize(maxX)
					pt._y = pt._y + self.normalizeSize(maxY)
				elif rotation == 90:
					pt._x = pt._x + self.normalizeSize(maxX)
					pt._y = pt._y + self.normalizeSize(maxY)
				elif rotation == 180:
					pt._x = pt._x + self.normalizeSize(maxX)
					pt._y = pt._y + self.normalizeSize(maxY)
				elif rotation == 270:
					#pt._x = pt._x + self.normalizeSize(maxX)
					#pt._y = pt._y + self.normalizeSize(maxY)
					pass
				else:
###					print "devices on the bottom, rotation case not implemented ! " + str(rotation)
					exit(-1)
				
			ns += "ADD '" + str(dev.refid) + "' " + str(name) + "@" + str(libname) + " " + orientation + "R%.3f"% (rotation) +" (" + str(pt) + ");" + CRLF   
			
		return ns
	
	
	def Cmd(self,cmds):
		gen = 0
		sch = 0
		brd = 0
		add = 0
		layers = 0
		net_connect = 0
		netlist = 0
		board = 0
		place = 0
		route = 0
		scr = 0
		lst = 0
		
		if cmds[0:1] == ['gen']:
			gen = 1
		
		if cmds[1:2] == ['sch']:
			sch = 1

		if cmds[1:2] == ['brd']:
			brd = 1
			
		if cmds[2:3] == ['add']:
			add = 1
			
		if cmds[2:3] == ['layers']:
			layers = 1
			
		if cmds[2:3] == ['net-connect']:
			net_connect = 1
			
		if cmds[2:3] == ['netlist']:
			netlist = 1
			
		if cmds[2:3] == ['board']:
			board = 1
		
		if cmds[2:3] == ['place']:
			place = 1
			
		if cmds[2:3] == ['route']:
			route = 1

			
		if cmds[3:4] == ['scr']:
			scr = 1
			
		if cmds[3:4] == ['lst']:
			lst = 1

		if gen:
			if sch:
				if add:
					if scr:
						s = self.genSchAddScr()
						return s
						
				if layers:
					if scr:
						s = self.genSchLayersScr()
						return s
					
				if net_connect:
					pass
					
				if netlist:
					pass
		
			if brd:
				if board:
					if scr:
						s = self.genBrdBoardScr()
						return s
				if place:
					if scr:
						s = self.genBrdPlaceScr()
						return s
					
				if route:
					pass
		
					
		return ""
					
			
	def test(self):
		
		ic1 = CDev("U1","","IC1")
		ic1.add( CPin("GND",1) )
		ic1.add( CPin("VCC",2) )
		self.sch.addDev(ic1)
	
		net1 = CNet("GND")
		net1.add(CNode(ic1,"GND"))
		self.sch.addNet(net1)
	
		net2 = CNet("VCC")
		net2.add(CNode(ic1,"VCC"))
		self.sch.addNet(net2)
		
		print "gen sch add scr"
		s = self.genSchAddScr()
		print s
		print "gen sch net-connect scr"
		s = self.genSchNetConnectScr()
		print s
		print "gen sch netlist lst"
		s = self.genSchNetlistLst()
		print s
		print "gen sch netlist scr"
		s = self.genSchNetlistScr()
		print s
	
# Some tests
if __name__ == "__main__":
	import sys
	#import string
	import re
	schem = CSchematic()
	board = CBoard(schem)
	board.addFromSchematic()

	eagle = CEagle(schem,board)
	
	# open input file
	if sys.argv[1:] == ['test']:
		eagle.test()

