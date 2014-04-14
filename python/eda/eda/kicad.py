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

import sys
import re
 
from edautils import *
from eda import *



template= """
PCBNEW-BOARD Version 0 date 5/1/2005-14:45:23
$DESCRIPTION
some data
...
$endDESCRIPTION
Example:
$GENERAL
Ly 1FFF8001
Links 66
NoConn 0
Di 24940 20675 73708 40323
Ndraw 16
Ntrack 267
Nzone 1929
Nmodule 29
Nnets 26
$EndGENERAL
$SHEETDESCR
Sheet A4 11700 8267
Title ""
Date "23 feb 2004"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndSHEETDESCR

"""


Layers= """
Tracks and other items (texts, drawings ...) use one layer.
Pads and vias use several layers.
There are 16 copper layers and 12 technical layers.
The layer parametre used in descriptions has the value:
value 
layer name 
"Copper" layers  
0  			Copper layer 
1 to 14 	Inner layers 
15 			Component layer 
16 			Copper side adhesive layer 

Technical layers 
17 			Component side adhesive layer 
18 			Copper side Solder paste layer 
19 			Component Solder paste layer 
20 			Copper side Silk screen layer 
21			Component Silk screen layer 
22 			Copper side Solder mask layer 
23 			Component Solder mask layer 
24 			Draw layer (Used for general drawings) 
25 			Comment layer (Other layer used for general drawings) 
26 			ECO1 layer (Other layer used for general drawings) 
26 			ECO2 layer (Other layer used for general drawings) 
27 			Edge layer. Items on Edge layer are seen on all layers 
"""

CRLF = "\n"

class CKICAD:
	" KICAD class "
	def __init__(self, sch=None,brd=None):
		self.name=""
		self.sch=sch
		self.brd=brd
		self.origin = Point(30000,20000)
		self.shapeLine = 0
		self.shapeVia = 3
		
	def normalizeSize(self,size):
		return size * 0.01

	def normalizePoint(self, pt):
		offy = self.brd.bbox.sizeY()
		pt._y = offy - pt._y
		pt.scale(0.1)
		pt.offset(self.origin._x, self.origin._y)
		
	def normalizeRotation(self, rotation):
		return int(rotation * 10)
	
	# Po[sition] sx sy ex ey width layer	
	def genPo(self, shape, pts, pte, width):
		ns = "Po " + "%d "% (shape)
		ns += "%d "% (pts._x) + "%d "% (pts._y)
		ns += "%d "% (pte._x) + "%d "% (pte._y)
		ns += "%d "% (width)
		return ns
	# De[scription] layer type angle timestamp status 
	def genDe(self, layer, type, angle, timestamp, status):
		ns = "De " + "%d "% (layer) + "%d "% (type)+ "%d "% (angle)+ "%d "% (timestamp)+ "%d "% (status)
		return ns

	def genDrawSegment(self, pts, pte, width, layer):
		ns  = "$DRAWSEGMENT" + CRLF
		ns += self.genPo(self.shapeLine, pts, pte, width) + CRLF
		ns += self.genDe(layer, 0, 900, 0, 0) + CRLF
		ns += "$EndDRAWSEGMENT" + CRLF
		return ns

	def generateBegin(self):
		ns = 'PCBNEW-BOARD Version 1 date 24/11/2007-18:15:03' + CRLF
		return ns
	
	def generateFinish(self):
		ns = '$EndBOARD' + CRLF
		return ns
	
	def generateLayers(self):
		ns = ''
		return ns
	
	def generateBoard(self):
		
		ns = """
$GENERAL
LayerCount 2
Ly 1FFF8001
Links 0
NoConn 0
Di 32924 14924 49576 50576
Ndraw 5
Ntrack 0
Nzone 0
Nmodule 0
Nnets 0
$EndGENERAL

$SHEETDESCR
Sheet A4 11700 8267
Title ""
Date "24 nov 2007"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndSHEETDESCR

$SETUP
InternalUnit 0.000100 INCH
GridSize 500 500
UserGridSize 0.010000 0.010000 mm
ZoneGridSize 250
Layers 2
TrackWidth 170
TrackWidthHistory 170
TrackClearence 60
ZoneClearence 150
DrawSegmWidth 150
EdgeSegmWidth 150
ViaSize 450
ViaDrill 200
ViaSizeHistory 450
TextPcbWidth 120
TextPcbSize 600 800
EdgeModWidth 150
TextModSize 600 600
TextModWidth 120
PadSize 600 600
PadDrill 320
"""
		ns += "AuxiliaryAxisOrg " + "%d "% (self.origin._x) + "%d "% (self.origin._y) + CRLF
		ns += """
$EndSETUP
"""

		# determine board size, aka outline for rectangular ones only
		# all coordinates are in mil * 100
		minx = 0
		miny = 0 
		maxx = 0
		maxy = 0
		prevpt = Point(0,0)
		first = True
		ptcnt = 0	
		for pt in self.brd.outline:
			ptcnt += 1		
			if first:
				minx = pt._x# in mils
				miny = pt._y
				maxx = pt._x
				maxy = pt._y
				first = False
				prevpt = pt
			else:
				if minx > pt._x:
					minx = pt._x
				if miny > pt._y:
					miny = pt._y
				if maxx < pt._x:
					maxx = pt._x
				if maxy < pt._y:
					maxy = pt._y
				prevpt = pt

		# reflection
		offy = self.brd.bbox.sizeY()
		maxy = offy - maxy
		miny = offy - miny
		# scale to mils
		maxx /= 100
		minx /= 100
		maxy /= 100
		miny /= 100
		
		xsize = (maxx - minx)
		ysize = (maxy - miny)


#$DRAWSEGMENT
#Po 0 40500 4500 40500 6500 150
#De 28 0 900 0 0
#$EndDRAWSEGMENT		
		# Line
		## Po[sition] shape Xstart Ystart Xend Yend width 
		#Po 0 40500 4500 40500 6500 150
		## Description layer type angle timestamp status 
		# De 28 0 900 0 0 
		
		# board outline?
		#ns += "DRW      BOARD " +    "%d "% (minx) +  "%d "% (miny) + " 1   0" + CRLF
		#ns += "DRW      BOARD " +    "%d "% (0) +  "%d "% (0) + " 1   0" + CRLF
		
		first = True
		firstpt= Point(0,0)
		prevpt = Point(0,0)
		for pt in self.brd.outline:
			self.normalizePoint(pt)
###			print str(pt) + " " + str(prevpt)
			if first:
				first = False
				firstpt = Point(pt._x, pt._y)
				prevpt = pt
				continue
			
			ns += self.genDrawSegment(prevpt, pt, 150, 28)
			prevpt = Point(pt._x, pt._y)
				
		ns += self.genDrawSegment( pt, firstpt, 150, 28)
		ns += "" + CRLF
		return ns
		
	

	def genNetlist(self):
		ns = ''
		CRLF = "\n"
				
		ns += "*CONNECTION*  "  + CRLF
		ns += ""  + CRLF
				
		for netname in self.sch.nets:
			net = self.sch.nets[netname]
			prevdev=""
			prevpin=""
			first = 1
			
			ns += "*SIGNAL*  "  + net.name +  " 0 -2 " +  CRLF
			
			for node in net.nodes:
				if first:
					first = 0
					prevdev=str(node.dev.refid)
					prevpin=node.pin
				else:
					ns += "*REMARK* " + prevdev + "." + str(prevpin.name) + "     " + str(node.dev.refid) + "." + str(node.pin.name) + CRLF	
					ns += prevdev + "." + str(prevpin.num) + "     " + str(node.dev.refid) + "." + str(node.pin.num) + CRLF	
					prevdev=str(node.dev.refid)
					prevpin=node.pin
					
			ns += "" + CRLF
					
		# string function
		return ns
	

# KiCAD does not read zones?		
	def generatePour(self):
		ns = ''
		CRLF = "\n"
	
		prevpt = Point(0,0)
		first = True
		ptcnt = 0	

		# reflection
		offy = self.brd.bbox.sizeY()
		geomcnt = 0
		for net in self.brd.nets.values():
			
			for geom in net.geometry:
				geomcnt += 1
###				print " found geom in " + net.name  + " type " + str(type(geom)) + CRLF
				# Handle rectangle
				#if type(geom) is Rectangle :
				if isinstance(geom, Rectangle) :
###					print " found Rectangle" + CRLF
					
					rect = Rectangle(geom.ll._x, geom.ll._y, geom.ur._x, geom.ur._y, geom.layernum )
					rect.normalize()						# normalize just in case
					rect.ll._y = offy - rect.ll._y		# reflect
					rect.ur._y = offy - rect.ur._y
					rect.normalize()						# normalize again
					rect.scale(0.01)
					# name COPPER origin_x origin_y  pieces flags=1 solid fill net
					# pieces is what follow, use COPCLS for filled polygon
					# origin will be lower left
					#ns += "DRW"+ "%d "% geomcnt + " COPPER " +    "%d "% (rect.ll._x) +  "%d "% (rect.ll._y) + " 1 0 " + net.name + CRLF
					# nummcoord line_width level
					# needs to be closed with the last one
					ns += "COPCLS " + str(5) + " 10 " + str(rect.layernum) + CRLF	# 10 for width looks ok but shall we use less? NO 1 is making a hatch
					ns += "%d "% ( 0 ) +  "%d "% ( 0 )  + CRLF
					ns += "%d "% ( rect.ur._x - rect.ll._x) +  "%d "% ( 0 )  + CRLF
					ns += "%d "% ( rect.ur._x - rect.ll._x) +  "%d "% ( rect.ur._y - rect.ll._y ) + CRLF
					ns += "%d "% ( 0 ) +  "%d "% ( rect.ur._y - rect.ll._y )  + CRLF
					ns += "%d "% ( 0 ) +  "%d "% ( 0 ) + CRLF											# close do we need it?
					ns += "" + CRLF
					
#					# name COPPER origin_x origin_y  pieces flags=1 solid fill net
#					# pieces is what follow, use 1 CLOSED
#					ns += "DRW      BOARD " +    "%d "% (0) +  "%d "% (0) + " 1   0" + CRLF
#					# nummcoord line_width level
#					# needs to be closed with the last one
#					ns += "CLOSED " + str(ptcnt+1) + " 10 0" + CRLF
#			
#					for pt in self.brd.outline:
#						ns += "%d "% (pt._x / 100) +  "%d "% ( (offy - pt._y) / 100) + CRLF
#						prevpt = pt
#					ns += "%d "% (self.brd.outline.points[0]._x / 100) +  "%d "% ( (offy - self.brd.outline.points[0]._y) / 100) + CRLF
							
							
		ns += "" + CRLF
		ns += "" + CRLF
		

		return ns
	


	def genPackage(self, package):		
		ns = ''
		# geometry
		
		terminals = len(package.pins)
		for num in range(terminals):
			pin = package.pins[num+1]
			pt = Point(pin.pos._x, pin.pos._y)
			self.normalizePoint(pt)
			padsizex = self.normalizeSize(pin.pad.sizex)
			padsizey = self.normalizeSize(pin.pad.sizey)
			if pin.pad.type == "S":
				shape = 'R'
			elif pin.pad.type == "R":
				shape = 'C'
			ns += "$PAD" + CRLF
			#Shape: <pad name> shape Xsize Ysize Xdelta Ydelta Orientation 
			ns += 'Sh "' + str(num+1) + '" ' + shape + ' ' + "%d "% (padsizex) + "%d "% (padsizey) + ' 0 0' + ' 0' + CRLF
			
			if package.smt:
				ns += "At SMD N 00888000" + CRLF
				ns += "Dr 0 0 0" + CRLF
			else:
				ns += "At STD N 00E0FFFF" + CRLF
				ns += "Dr " + "%d "% (pin.pad.drill) + " 0 0" + CRLF
			
			ns += "Po " + "%d "% (pt._x) + "%d "% (pt._y) + CRLF
			
			ns += "$EndPAD"  + CRLF

		return ns
	

	# gen componnent packages - for all componnents on the board
	def genPackages(self):
		ns = ''
		CRLF = "\n"
		ns += "" + CRLF
		
		for packagename in self.brd.packages:
			ns += self.genPackage(self.brd.packages[packagename])			
		return ns
	
	def gen3D(self, dev):
		ns = ''
		return ns
		
	def genModule(self, dev):		
		ns = ''
		# name - can not have spaces
		name = str(dev.name)
		name = name.replace( " ", "_") 
		
		pt = Point(dev.position._x , dev.position._y)
		self.normalizePoint(pt)
		if dev.bottom:
			layer = 0
		else:
			layer = 15
			
		rotation = self.normalizeRotation(dev.rotation)
		
		# $MODULE <module lib name> 
		ns += '$MODULE ' + name + CRLF
		#Po Xpos Ypos Orientation(0.1deg) Layer TimeStamp Attribut1 Attribut2
		#Attribut1 = ~or 'F' for autoplace (F = Fixed, ~= moveable)
		#Attribut2 = ~or 'P' for autoplace (P = autoplaced)
		#Po 54500 18000 900 15 444612A3 4748F959 ~~
		ns += "Po "
		ns += "%d "% (pt._x) + "%d "% (pt._y)
		ns += "%d "% (rotation)
		ns += "%d "% (layer)
		ns += " 42806E04 4748F998"						# Time stamp
		ns += " ~~" + CRLF								# Attributes
		ns += "Li " + name + CRLF
		ns += "Cd " + dev.val + CRLF
		ns += "Op 0 0 0" + CRLF							# Rotation cost
		#At SMD 
		if dev.package.smt:
			ns += "At SMD" + CRLF						# surface mount
		ns += "T0 0 0 250 250 0 50 N V 21 " + dev.refid + CRLF	# refrence ID
		ns += "T1 0 0 250 250 0 50 N V 21 " + dev.val + CRLF	# value
		ns += self.genPackage(dev.package)
		ns += self.gen3D(dev)
		ns += '$EndMODULE ' + name + CRLF
		ns += CRLF
			
		return ns
	
	# gen device - for all componnents on the board
	def genDevices(self):
		ns = ''
		CRLF = "\n"

		ns += "*PARTTYPE*   ITEMS" + CRLF
		ns += "" + CRLF
		for devname in self.brd.devices:
			ns += self.genModule(self.brd.devices[devname])
		
		ns += "" + CRLF
		return ns
	
	
	def genDevicePlacement(self, dev):
	
		ns = ''
		ns += self.genModule(dev)
		return ns
		
 	# gen device placemnent - for all componnents on the board
	def generatePlacement(self):
		ns = ''
		ns += "" + CRLF
		for devname in self.brd.devices:
			ns += self.genDevicePlacement(self.brd.devices[devname])
		
		ns += "" + CRLF
		return ns
	
	
# Vias are tricky, should be outout with the route but that is not easy
	def generateNetVias(self,net):
		ns = ''
		for via in self.brd.vias:
			if via.netname != net.name:
				continue
			pts = Point(via.pos._x,via.pos._y)
			self.normalizePoint(pts)
			pte = Point(via.pos._x,via.pos._y)
			self.normalizePoint(pte)
			thickness = 300 # needs to be set 
			#thickness = 650 # needs to be set 
			pte.offset(thickness, thickness)		# offset to size
			ns += self.genPo(self.shapeVia, pts, pte, thickness) +  " -1" + CRLF
			ns += self.genDe(15, 1, 0, 0, 0) + CRLF						# layers 15 through 1
		return ns;
	
	def generateNetRoutes(self,net):			
		#Po 0 42500 31500 44500 31500 170 -1
		#De 0 0 0 0 0
		ns = ''
		
		for line in net.route:
						
			layer = line.layernum
			
			if layer == 0:		# unrouted
				continue
			
			#map layers
			if layer == 1:	# TOP
				layer = 0	# Copper
				
			if layer == 2:	# BOTTOM
				layer = 15	# Componnent
						
			prevpt  = Point(0,0)
			firstpt = Point(0,0)
			first = True
			for ptt in line.points:
				pt = Point(ptt._x, ptt._y)
				self.normalizePoint(pt)
				thickness = line.thickness * 0.1
				if first:
					first = False	
					firstpt = Point(pt._x, pt._y)
					prevpt  = Point(pt._x, pt._y)
				else:
					ns += self.genPo(self.shapeLine, prevpt, pt, thickness) + " -1" +  CRLF
					ns += self.genDe(layer, 0, 0, 0, 0) + CRLF
					prevpt = Point(pt._x, pt._y)
									
		return ns

	def generateRoutes(self):
		ns = '$TRACK' + CRLF
		ns += ""  + CRLF
		for net in self.brd.nets.values():
			ns += self.generateNetRoutes(net)
			ns += self.generateNetVias(net)
		ns += '$EndTRACK' + CRLF
		return ns

# This will ouput VIAs shapes
# the VIA placement is in route generation
	def generateVias(self):
		ns = ''
		CRLF = "\n"
		return ns;
	
	
	# gen brd place scr"
	def genBrdPlaceScr(self):
		ns = ''
		CRLF = "\n"
#ADD 'C1' CAPAE1350X1350N@ipc-7351-capacitor R0.000 (-0.950 0.350);	
		for dev in self.brd.devices:
			ns += "ADD '" + str(dev.refid) + "' " + str(dev.packagename) + "@" + str(dev.libname) + " " + dev.orientation + "R%.3f"% (dev.rotation) +" (" + str(dev.position) + ");" + CRLF   
		return ns
	
	
	def importdesign(self,filename):
###		print "import design " + filename
		f = open(filename)
		r = f.readlines()
		f.close()
		
		offy = self.brd.bbox.sizeY()
		
		net = None
		routesegment = Line()
		inroute = False
		insignal = False
		relline = 0
		signal =""
		pin1 = ""
		pin2 = ""
		firstpoint = True
		prevX = 0
		prevY = 0
		prevLayer = 0
		prevSegwidth = 0
		prevFlags = 0
		
			
		re_TAG   = re.compile("^(\*\w+\*)*")
		#re_TAG   = re.compile("^(\*ROUTE\*)*")
		for l in r:
			s = l.rstrip()
# detect headers
			#print s
			match = re_TAG.search(s)
			
			if (match.group(1) is not None):
###				print " Tag " + match.group(1)
				
				if ( match.group(1) == "*REMARK*" ) :
					continue
				#print str(match.group(1))
				if ( match.group(1) == "*ROUTE*" ) :
###					print " Route \n"
					sys.stdout.write(s)
					inroute = True
					continue

# *SIGNAL* signame SIGFLAG color viatype
# SIGFLAG default 0 signal visibility, bit 10 should be set
# color -2 15, default -2 no specific color
# viatype specific via type				
				if ( match.group(1) == "*SIGNAL*" ) :
					re_SIGNAL = re.compile("^(\*SIGNAL\*)\s*([\w\#]+)*")
					match = re_SIGNAL.match(s)
					signal =  match.group(2)
					#net = self.brd.nets[signal]
					net = self.brd.getNet(signal)
					if net == None:
						print "could not find Net " + signal
						exit(-1)
						
					print " Signal " + signal
					insignal = True
					relline = 0
					routesegment=Line([])
					#sys.stdout.write(s + "\n")
					inroute = True
					continue
			
			
# end all sections			
				#print " ending current section"
				insignal = False		# Terminate current section if another detected
				
			if insignal :
				print " insignal " + " relline " + str(relline)
				
				if len(s) <= 0:				# skip all empty line
					continue
				
				# count only non empty lines
				relline += 1
				
				re_PIN1PIN2 = re.compile("^(\w+\.\w+)\s*(\w+\.\w+)*")
				if relline == 1:		# pin1 pin2
					match = re_PIN1PIN2.match(s)
					pin1 =  match.group(1)
					pin2 =  match.group(2)
###					print " Pin1 " + str(pin1) + " Pin2 " + str(pin2)
					#pin1, pin2 = string.split(filename)
					#sys.stdout.write(s + "\n")
					firstpoint = True
					routesegment = Line([])
					continue
				
# now the route segment
# x y layer segwidth FLAGS ARCDIR 
# x and y are coordinates, first set is the starting point
# layer
# Layer on which the route starts, ends, or changes layer. For partial routes, the unrouted portion 
# takes on a layer number 0. A layer value of 31 (rather 65?) indicates the end of the route/connection 
# at a component pin.
# FLAGS
# Router conditions flag. Integer field with valid values ranging from 0 to 32767, These values 
# represent router conditions that exist at the x and y coordinate location.
# Flag bit 6, if set together with a via name in the track corner or assigned to the first or 
# last corner of a track, defines the coordinate of a test point.
# 0x00080 Route protected flag
# 0x00100 Plane thermal
# 0x00200 Teardrop prohibit flag (Left) 0x00400  Teardrop prohibit flag (Right)
# 0x01000 Arc center flag 0x00800 Glued via flag
# 0x0e000 Miter bits: 1 - arc miter, 2 - line miter
# 0x10000 Stitching via flag
# ARCDIR
# Specified for arc centers only when the arc begins on the previous corner and ends on the 
# following corner. 
# Valid values for ARCDIR: 
# CW  -- Clockwise
# CCW -- Counterclockwise
				
					
				#re_XYLS = re.compile("^(\d+)\s*(\d+)\s*(\d+)\s*(\d+)\s(\d+)\s*")
				re_XYLS = re.compile("^(\d+\.*\d*)\s*(\d+\.*\d*)\s*(\d+)\s*(\d+)\s(\d+)\s*(\w*)\s*(\w*)\s*")
				# print s
				match = re_XYLS.match(s)
				
				if match == None:			# check if we have a match
					print " no more matches \n"
					insignal = False
					continue
				
				if match.lastindex == None:		# check for no matches
					print " no more matches \n"
					insignal = False
					continue
				
				if match.lastindex < 5:			# check for minimum matches
					print " not enough matches \n"
					insignal = False
					continue
				
				# must be in mils
				# conver to 1/100 mil
				x = float(match.group(1)) * 100 
				y = offy - float(match.group(2)) * 100
										
				layer = int(match.group(3))
				segwidth = int(match.group(4)) * 100
				flags = int(match.group(5))
				vianame = ""
				thermal = ""
				# assign matches
				vianame = match.group(6)
				withvia = False
				thermal = match.group(7)
				withthermal = False
				
				# 
				if  vianame == "THERMAL":
					thermal = "THERMAL"
					vianame = ""
					withvia = False
					withthermal = True
				
				if len(thermal) & len(vianame)> 0:
					withvia = True
					withthermal = True
					
					
# lastindex does not work					
#					print "last index " + str(match.lastindex)
#					if match.lastindex == 6:
#						thermal = match.group(6)
					
#					if match.lastindex >= 7:
#						vianame = match.group(6)
#						thermal = match.group(7)


				
				line = 	" X " + str(x) + " Y " + str(y) + " Layer " + str(layer) + " segwidth " + str(segwidth) + " flags " + str(flags)
				if withvia:
					line += " via " + vianame 
					
				if withthermal:
					line +=  " thermal " + thermal
					
				#print line
				
				# check if first point and return
#					if firstpoint:
#						prevX = x
#						prevY = y
#						prevLayer = layer
#						prevSegwidth = segwidth
#						prevFlags = flags
#						firstpoint = False
#						continue
									
				print " layer " + str(layer)
				
				# Append current point
				routesegment.append(Point(x, y))
								
				# Generate route and or via
				if  not firstpoint and ( prevLayer != layer) :
					routesegment.layernum = prevLayer
					routesegment.thickness = segwidth
					print " adding route segment length " + str(routesegment)
					print " route segment layer " + str(routesegment.layernum)
					net.route.append(routesegment)
# something strange is going here, the __init__ in Line() does not set points to [] empty list,
# instead it seems to recycle points from previouse instance and points keep accumulating
# is this a Python bug?
					# Start new line from the end
					routesegment = Line([])				
					# Append current point
					routesegment.append(Point(x, y))
					print " new route segment length " + str(routesegment)
					

				
				# Do we have a via here?
				if withvia :
					via = CVia(vianame)
					via.pos = Point(x,y)
					via.netname = net.name
					self.brd.vias.append(via)
					
					
				# Check if we are at the and of the route layer 65
				if layer == 65 :
					relline = 0				# reset the counter
					pass
			
				prevX = x
				prevY = y
				prevLayer = layer
				prevSegwidth = segwidth
				prevFlags = flags
				
				firstpoint = False
					
					
		if ( inroute  ):
			sys.stdout.write(s)
##			filter(path+"/"+s) 
	
	
	
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
					
				if net-connect:
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

	pads = CPADS(schem,board)
	#print sys.argv[1]
	#print sys.argv[2]
	# import file
	if sys.argv[1] == 'import':
		pads.importdesign(sys.argv[2])
		
	# open input file
	if sys.argv[1:] == ['test']:
		pads.test()
    
