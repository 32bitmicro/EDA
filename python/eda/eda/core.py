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



from collections import defaultdict
from odict import OrderedDict

class Point:
	def __init__(self, x=0.0, y=0.0, layernum=0, **kw):
		self._x = x
		self._y = y
		self.layernum=layernum

	def __str__(self):
		return "%.3f %.3f" % (self._x, self._y)
	
	def scale(self, scale):
		self._x = self._x * scale
		self._y = self._y * scale

	def offset(self, offx, offy):
		self._x = self._x + offx
		self._y = self._y + offy
# is this causing problem with xmlpickle?
# 
#    offy = self.brd.bbox.sizeY()
#AttributeError: Rectangle instance has no attribute 'sizeY'
#		
#	def __selfser__(self, lines):
#		lines.append('Point('+str(self._x)+','+str(self._y)+','+str(self.layernum)+')')
		
		
class Rectangle:
	def __init__(self, x1=0.0, y1=0.0, x2=0.0, y2=0.0, layernum=0, **kw):
		self.ll = Point(x1,y1,layernum)
		self.ur = Point(x2,y2,layernum)
		self.normalize()
		self.layernum=layernum
		
	def __str__(self):
		return str(self.ll) + " , " + str(self.ur)
    
	def normalize(self):
		x1 = self.ll._x
		y1 = self.ll._y
		x2 = self.ur._x
		y2 = self.ur._y
    	
		if x1 < x2:
			llx = x1
			urx = x2
		else:
			llx = x2
			urx = x1
			
		if y1 < y2:
			lly = y1
			ury = y2
		else:
			lly = y2
			ury = y1
		self.ll = Point(llx,lly,self.ll.layernum)
		self.ur = Point(urx,ury,self.ur.layernum)
    	    
	def sizeX(self):
		return self.ur._x - self.ll._x

	def sizeY(self):
		return self.ur._y - self.ll._y
	
	def scale(self, scal):
		self.ll.scale(scal)
		self.ur.scale(scal)
	
	def offset(self, offx, offy):
		self.ll.offset(offx, offy)
		self.ur.offset(offx, offy)
		
	def isInside(self,x,y):
		if x >= self.ll._x & x <= self.ur._x:
			if y >= self.ll._y & y <= self.ur._y:
				return True
		return False

# is this causing problem with xmlpickle?
# 
#    offy = self.brd.bbox.sizeY()
#AttributeError: Rectangle instance has no attribute 'sizeY'
#
#	def __selfser__(self, lines):
#		lines.append('Rectangle('+str(self.ll._x)+','+str(self.ll._y)+','+str(self.ll._x)+','+str(self.ll._y)+','+str(self.layernum)+')')
        
class Line:
	def __init__(self,points=[],thickness=1, layernum=0):
#		print "Line init points arg " + str(len(points))
		self.points=points
		self.thickness = thickness
		self.layernum = layernum
		self.index = 0
		self.bbox = Rectangle()
    	
	def __str__(self):
		s = "line "
		s += " num points " + str(len(self.points))
		for p in self.points:
#			s += str(p) + " " 
			pass
		return s
		
	def __iter__(self):
		self.index = 0
		return self
	
	def next(self):
		if self.index == len(self.points):
			raise StopIteration
		self.index = self.index + 1
		return self.points[self.index-1]
	
	def append(self,point):
		self.points.append(point)
	
	def calcBBox(self):	
	# determine bbox
		minx = 0
		miny = 0 
		maxx = 0
		maxy = 0
		prevpt = Point(0,0)
		first = True
		for pt in self.points:			
			print pt
			if first:
				minx = pt._x
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
		
		self.bbox=Rectangle(minx,miny,maxx,maxy)

# based on Line but has to be closed	
class Polygon(Line):
	def __init__(self,points=[],thickness=1, layernum=0 ):
		Line.__init__(self,points,thickness,layernum)
		# Check and close the polygon
		self.bbox = Rectangle()
	
	def __str__(self):
        	return "Polygon() points" + str(self.points)
		

# ElementArc [X Y Width Height StartAngle DeltaAngle Thickness]
class Arc(Point):
	def __init__(self, x=0, y=0, width=0, height=0, sangle=0, dangle=0, thickness=1, layernum=0 ):
		Point.__init__(self,x,y,layernum)
		self.width=width				# width
		self.height=height				# height
		self.sangle=sangle				# start angle
		self.dangle=dangle				# delta angle
		self.thickness = thickness		# thickness
		self.index = 0
		self.bbox = Rectangle()
    	
	def __str__(self):
		return "Arc() point" + "%.3f %.3f" % (self._x, self._y)

# Derived from Arc
class Circle(Arc):
	def __init__(self, x=0, y=0, diameter=0, thickness=1, layernum=0 ):
		Arc.__init__(self,x,y,diameter/2,diameter/2,0,360,thickness,layernum)
		self.bbox = Rectangle()
    	
	def __str__(self):
		"Circle() point" + "%.3f %.3f" % (self._x, self._y) + "diameter "
		
# Text [X Y Direction Scale "String" SFlags]
# X Y The location of the upper left corner of the text.
# Direction 0 means text is drawn left to right, 1 means up, 2 means right to left (i.e. upside down), and 3 means down. 
# Scale Size of the text, as a percentage of the default size of of the font (the default font is about 40 mils high). Default is 100 (40 mils).
# based on Point
class Text(Point):
	def __init__(self, text="", x=0, y=0, size=1, direction=0, orientation=0.0,scale=1.0, thickness=1, layernum=0):
			Point.__init__(self,x,y,layernum)
			self.text = text
			self.size = size
			self.direction = direction
			self.orientation=orientation
			self.scale = scale
			self.thickness = thickness
			self.bbox = Rectangle()
			
    
	def __str__(self):
        	self.text
        
# Pad class - throughole or smt
# Square - S
# Round  - R
# for Square size[xy] is length of the edge
# for Round size[xy] is the diameter in x or y direction, if x != y then oval?
class CPad:
	def __init__(self,sizex=0, sizey=0, type="S", drill=0):
		self.type=type					# square
		self.drill = drill
		self.sizex = sizex
		self.sizey = sizey
		self.bbox = Rectangle(-sizex/2,-sizey/2,sizex/2,sizey/2)
		if  type == "S":
			pass
		else:
			pass
		self.tag	= 0
	
	def __str__(self):
		return self.type + ' : drill ' + str(self.drill) + ' sizex ' + str(sizex) + ' sizey ' + str(sizey) + ' bbox ' + str(self.bbox)
	
	
# Pin class - throughole or smt
class CPin:
	def __init__(self,name="",num=-1, x=0, y=0, pad=None):
		self.name=name
		self.num=num
		self.pos = Point(x,y)			# position
		self.netname=""					# pin net name
		self.pad = pad					# pad
		self.smt = False				# smt pin aka pad
		self.thickness = 0				# th pin attr
		self.clearance = 0				# th pin attr
		self.mask      = 0				# th pin attr
		self.drill     = 0				# th pin attr
		self.bbox = Rectangle(x,y,x,y)	# just to have something
		self.tag	= 0

	
	def __str__(self):
		return self.name + ' : ' + str(self.num) + ' pos ' + str(self.pos) + ' bbox ' + str(self.bbox)

	# sets pin from SMT pad defined by pad size x and y
	# delta mask and delta clearance are 0.25mm and 0.5mm
	# dmask=mm2pcb(0.25)=984.25, dclearance=mm2pcb(0.5) = 1968.5
	def set_pin_pad_from_size(self, padsizex, padsizey, dmask=984.25, dclearance=1968.5 ):
		# set as in pcb
		if padsizex > padsizey:			# horizontal
			thickness =  padsizey
			rX1 = self.pos._x - (padsizex - thickness) / 2  
			rX2 = self.pos._x + (padsizex - thickness) / 2  
			rY1 = rY2 = self.pos._y
		else:					# vertical
			thickness =  padsizex
			rX1 = rX2 = self.pos._x
			rY1 = self.pos._y - (padsizey - thickness) / 2 
			rY2 = self.pos._y + (padsizey - thickness) / 2 
	
		self.smt         = True
		# set thickness, mask and clearance
		self.thickness 	= thickness
		self.mask        = self.thickness + dmask
		self.clearance   = self.thickness + dclearance
		self.drill       = 0
		
		# set pcb attributes
		self.rX1=rX1
		self.rY1=rY1
		self.rX2=rX2
		self.rY2=rY2
	
		size = self.thickness + self.clearance
	        # make bbox and normalize it
	        self.bbox = Rectangle(rX1,rY1,rX2,rY2,0)
	        # # make bbox covering pin with clearance, will be used for blockages
	        rX1=self.bbox.ll._x - size / 2
	        rY1=self.bbox.ll._y - size / 2
	        rX2=self.bbox.ur._x + size / 2
	        rY2=self.bbox.ur._y + size / 2
	        self.bbox = Rectangle(rX1,rY1,rX2,rY2,0)

		
# Schematic Port class
class CPort:
	def __init__(self,name="",num=-1, x=0.0, y=0.0, orientation=0.0, side=0):
		self.name=name
		self.num=num
		self.pos=Point(x,y)				# position
		self.orientation=orientation	# orientation
		self.side=side					# side
		self.netname=""					# port net name
		self.bbox = Rectangle(x,y,x,y)	# just to have something
		self.tag	= 0
	
	def __str__(self):
		return self.name + ' : ' + str(self.num) + ' pos ' + str(self.pos) + ' orientation ' + str(self.orientation) +' side ' + str(self.side) + ' bbox ' + str(self.bbox)
	
# Schematic Symbol
class CSymbol:
	def __init__(self, name="", libname="", description=""):
		self.name=name					# symbol name
		self.libname=libname			# library name
		self.description=description	# description
		self.numsides = 0				# number of sides, 0 - discrete devices, 1 and more is IC
		self.ports = {}					# Ports
		self.portsbyname = {}			# Ports
		self.geometry = []				# Geometry associated with the symbol Polygon,Rectangle,Text,Line,Arc
		self.bbox = Rectangle()
		self.tag=0
		
	def __str__(self):
		ns  = 'symbol name ' + self.name + "@"  + self.libname + ' description ' + self.description
		ns += 'sides ' + str(self.numsides)+ ' bbox ' + str(self.bbox) + '\n'	
		ns += 'pins by num \n'
		l = len(self.pins)
		for num in range(l):
			pin = self.pins[num+1]
			ns += str(pin) + '\n'
		return ns
	
	def	addPort(self, item):
		self.ports[item.num]=item
		self.portsbyname[item.name]=self.ports[item.num]
		
# Schematic Package
class CPackage:
	def __init__(self, name="", libname="",description=""):
		self.name=name					# packge name
		self.libname=libname			# library name
		self.description=description	# description
		self.smt = False
		self.pins = {}					# Pin or Pad
		self.geometry = []				# geometry associated with the package Pin,Pad,Text,Line,Arc
		self.bbox = Rectangle()
		self.tag=0
		
	def __str__(self):
		ns  = 'package name ' + self.name + "@"  + self.libname + ' description ' + self.description
		ns += 'smt ' + str(self.smt)+ ' bbox ' + str(self.bbox) + '\n'	
		ns += 'pins by num \n'
		l = len(self.pins)
		for num in range(l):
			pin = self.pins[num+1]
			ns += str(pin) + '\n'
		return ns
	
		
# IC Device class
class CDev:
	cnt = 0
	
	def __init__(self, refid="", val="", name="", libname="", symbolname="" , packagename=""):
		self.pins={}				# dictionary of pins
		self.pinsbyname={}			# dictionary of pins by name
		self.refid=refid
		self.val=val
		self.name=name
		self.num=-1
		self.libname=libname				# library name
		self.package = None					# package
		self.packagename=packagename		# package name
		self.layer=0						# layer
		self.symbol = None					# symbol
		self.symbolname=symbolname			# symbol name
		self.position = Point(0,0)			# schematic position
		self.rotation = 0					# schematic rotation
		self.orientation = ""				# schematic orientation "" or "M"
		self.bottom = False					# bottom placement flag
		self.bbox = Rectangle()
		self.tag=0
		CDev.cnt = CDev.cnt + 1
		self.scale = 100					# scale for coordinates
		
	
	def __str__(self):
		ns  = 'device  refid ' + self.refid + ' name ' + self.name + "@"  + self.libname + ' val ' + self.val + ' symbol ' + self.symbolname + ' package ' + self.packagename + '\n'
		ns += 'position ' + str(self.position) + '\n'
		ns += 'pins by name \n'
		for pinname in self.pinsbyname.keys():
			pin = self.pinsbyname[pinname]
			ns += str(pin) + '\n'
			
		ns += 'pins by num \n'
		l = len(self.pins)
		for num in range(l):
			pin = self.pins[num+1]
			ns += str(pin) + '\n'
		return ns
	
	def empty(self):
		if(len(self.pins)>0):
			return 0
		else:
			return 1

	def __len__(self):
		return len(self.pins)

	def count(self):
		return len(self.pins)

	def __getitem__(self, key) :
		pass


	def	addPin(self, item):
		# get coordinates from package
		ppin  = self.package.pins[item.num]
		# transfer info from packge 
		if ( ppin != None):
			item.pos = ppin.pos
			item.bbox = ppin.bbox
		
		self.pins[item.num]=item
		self.pinsbyname[item.name]=self.pins[item.num]
			
	def removePin(self):
		""" What is this?
		"""
		item=self.pins[0]
		self.pins=self.pins[1:]
		self.pinsbyname[item.name] = None
		return item
	
	def setPos(self,x,y):
		# update only device, rest is relative
		self.position = Point(x,y)
		# well, pin positions have to be recalculated
		self.calcCurrentPinPos()
	
	def rotatePoint(self,pt,x0,y0,angle):
					
		dX = pt._x - x0
		dY = pt._y - y0
			
		rX = pt._x
		rY = pt._y
		
		if angle == 90:
			rX = x0 + dY
			rY = y0 - dX
			
		if angle == 180:
			rX = x0 - dX
			rY = y0 - dY
		
		if angle == 270:
			rX = x0 - dY
			rY = y0 + dX
			
		return rX,rY
				
	def calcCurrentPinPos(self):
		for ppin in self.package.pins.values():
			pin = self.pins[ppin.num]
			# reset from package
			rX = ppin.pos._x
			rY = ppin.pos._y
			X1 = ppin.bbox.ll._x
			Y1 = ppin.bbox.ll._y
			X2 = ppin.bbox.ur._x
			Y2 = ppin.bbox.ur._y
			if self.bottom:
				rY = 0 - rY
				Y1 = 0 - Y1
				Y2 = 0 - Y2		
			# Do Rotation
			rX,rY = self.rotatePoint(Point(rX,rY),0,0,self.rotation)
			X1,Y1 = self.rotatePoint(Point(X1,Y1),0,0,self.rotation)
			X2,Y2 = self.rotatePoint(Point(X2,Y2),0,0,self.rotation)
			# Set new position and bbox
			pin.pos = Point(self.position._x + rX, self.position._y +rY)
			pin.bbox = Rectangle(X1,Y1,X2,Y2,pin.bbox.layernum)
			
					
	def setRotation(self,r):
		self.rotation = int(r)
		self.calcCurrentPinPos()
		
		
	def setOrientation(self,r):
		self.orientation = r
	
	
	# Set on the bottpm
		
	def setBottom(self,b):
		# assume that initialy package defined for top
		
		# Internaly all coordinates are as looking down through the board.
		# Coordinate system on the bottom is the same as on top	
		# This includes package, however packages are defined as placed 
		# on the top, so when device goes on the bottom package has to be mirrored
		# in horizontal direction.
		# The approach is to mirorr the package in X 
		# For tools like pcb which use top for package definitions, bottom packages 
		# will have to be mirrored again
		self.bottom = b
		self.calcCurrentPinPos()
		
			
	def isBottom(self):
		return self.bottom
		
	def maxXminX(self):
		first = True
		minX = 0
		maxX = 0
		for ppin in self.package.pins.values():
			pin = self.pins[ppin.num]
			if first:
				minX = ppin.pos._x
				maxX = ppin.pos._x
			
			if minX > ppin.pos._x:
				minX = ppin.pos._x
				
			if maxX < ppin.pos._x:
				maxX = ppin.pos._x

		return maxX, minX		
		
		
	def maxYminY(self):
		first = True
		minY = 0
		maxY = 0
		for ppin in self.package.pins.values():
			pin = self.pins[ppin.num]
			if first:
				minY = ppin.pos._y
				maxY = ppin.pos._y
			
			if minY > ppin.pos._y:
				minY = ppin.pos._y
				
			if maxY < ppin.pos._y:
				maxY = ppin.pos._y

		return maxY, minY
		
# Module class, composite of multiple devices	
class CModule(CDev):
	cnt = 0
	
	def __init__(self, refid="", val="", name="", libname="", symbolname="" , packagename=""):
		CDev.__init__(self, refid, val, name, libname, symbolname , packagename)
		self.bbox = Rectangle()
		self.tag=0
		CModule.cnt = CModule.cnt + 1
		
	
# Pin class
class CNode:
	cnt = 0
	
	def __init__(self, dev=None, pinname=''):
		self.name=""
		self.num=-1
		self.dev = dev		# ic chip
		self.devrefid = dev.refid
		self.pinname = pinname
		self.pin= dev.pinsbyname[pinname]		# pin name or num
		self.tag=0
		CNode.cnt = CNode.cnt + 1
		
# Net class 
class CNet:
	cnt = 0
	
	def __init__(self,name=""):
		self.name=name
		if self.name == "":
			self.name = '$N' + str(CNet.cnt)
		self.num=-1
		self.nodes=[]
		self.geometry = []				# geometry associated with the Net
		self.bbox = Rectangle()
		self.route =[]					# list of Lines making the net route
		self.tag=0
		CNet.cnt = CNet.cnt + 1

	def empty(self):
		if(len(self.nodes)>0):
			return 0
		else:
			return 1
		
	def count(self):
		return len(self.nodes)

	def add(self, item):
		item.pin.netname = self.name			# connect pin to net
		self.nodes.append(item)	

	def remove(self):
		item=self.nodes[0]
		self.nodes=self.nodes[1:]
		return item


# Library class
class CLibrary:
	def __init__(self,name="",path=""):
		self.name=path
		self.path=path
		self.num=-1
		self.parts=[]
		self.nets=[]
		self.refids=-1
	
	def addPart(self, item):
		self.parts.append(item)	

# Symbols container class
class CContainer:
	def __init__(self):
		self.elements = {}

	def __len__(self):
		return len(self.elements)
	
	def __getitem__(self, key):
		return self.elements[key]
	
	def __setitem__(self, key, value):
		self.elements[key] = value 
	
	def __delitem__(self, key):
		del self.elements[key]
	
	def __iter__(self):
		return iter(self.elements)
	
	def __contains__(self, value):
		return value in self.elements

	def values(self):
		return self.elements.values()

#t is also recommended that mappings provide the methods
# keys(), values(), items(), has_key(), get(), clear(), 
# setdefault(), iterkeys(), itervalues(), iteritems(), 
# pop(), popitem(), copy(), and update() 
# behaving similar to those for Python's standard dictionary objects.

# Symbols container class
class CSymbols(CContainer):
	pass
	
# Devices container class
class CDevices(CContainer):
	pass

# Nets container class
class CNets(CContainer):
	pass

# Schematic class
class CSchematic:
	def __init__(self,name="",path=""):
		self.units	= "inch"
		self.name	= name
		self.path	= path
		self.num	= -1
		self.outline	= Polygon()
		self.libraries	= []
		self.devices	= CDevices() #{}
		self.symbols	= CSymbols() #{}
		self.nets	= CNets()    #{}
		self.refids	= -1
		self.geometry	= []
	
	def addLibrary(self, item):
		self.libraries.append(item)
		
	def addDev(self, item, addsym=-1):
		self.devices[item.refid]=item
		# add symbol if addsym >= 0 it also means number of sides in symbol
		if addsym >= 0:
			dev = self.devices[item.refid] 	
			self.addSymbolFromDev(dev, addsym, dev.symbolname)
	
	def getDev(self, refid):
		return self.devices[refid]
		
	def addSymbol(self, item):
		self.symbols[item.name]=item
	
	def getSymbol(self, name):
		return self.symbols[name]
	
	def addSymbolFromDev(self, dev, numsides, name="", libname="", description=""):
		symbol = CSymbol(name, libname, description)
		# go through device terminals and add symbol pins from them
		# origin
		ox = 0
		oy = 0
		# delta 0.015"
		deltax = 15000
		deltay = 15000
		orientation = 0.0
		side = 0
		numonside  = 0
		terminals = len(dev.pins)
		if numsides > 0:
			portperside = terminals /  numsides
		else:
			portperside = terminals
			
		for num in range(terminals):
			
			if numsides < 1:					# produce one line
				side = 0
				dx = 0
				dy = deltay
				orientation = 0.0
			elif numsides == 2:					# produce 2 lines
				side = num / portperside
				if side == 0:					# left side
					ox = 0
					oy = 0
					dx = 0
					dy = deltay
					numonside = num
					orientation = 180.0
				else:
					ox = deltax * 2
					oy = (portperside - 1) * deltay	# right side
					dx = 0
					dy = -deltay
					numonside = num
					orientation = 0.0
			else:
				side = num / portperside
				if side == 0:					# left side, going up
					ox = 0
					oy = deltay
					dx = 0
					dy = deltay
					orientation = 180.0
				elif side == 1:					# upper side, going right
					ox = deltax
					oy = (portperside + 1) * deltay
					dx = deltax
					dy = 0
					orientation = 270.0
				elif side == 2:					# right side, going down
					ox = (portperside + 1) * deltax
					oy = (portperside) * deltay
					dx = 0
					dy = -deltay
					orientation = 0.0
				else:							# lower, going left
					ox = (portperside) * deltax
					oy = 0
					dx = -deltax
					dy = 0
					orientation = 90.0
			
			# get pin
			pin = dev.pins[num+1]
			numonside = num - side * portperside		
			x = ox + dx * numonside
			y = oy + dy * numonside
			name = pin.name
			port = CPort(name,num+1, x, y, orientation, side)
			#symbol.ports[port.name] = port
			symbol.addPort(port)

				
		self.symbols[symbol.name]=symbol
		
	
	def addNet(self, item):
		self.nets[item.name]=item
		
	def getNet(self, name):
		return self.nets[name]
# Via class
class CVia:
	def __init__(self,name="",x=0.0, y=0.0,netname="",num=-1):
		self.name=name
		self.num=num
		self.pos = Point(x,y)		# position
		self.netname=netname		# via net name
		self.layers=[]				# layers this pin connects to
		self.bbox = Rectangle()
	
	def __str__(self):
		return self.name

# Pour class
class CPour:
	def __init__(self,name="",netname="",num=-1):
		self.name=name
		self.num=num
		self.netname=netname		# net name
		self.poly = Polygon([])		# polygon
		self.layernum= 0				# layer
		self.isolate= 0				# isolate
		self.fill= 0				# fill 0 - solid 1 - hatch
		self.thermals= True			# thermals
		self.orphans= True			# orphans
		self.bbox = Rectangle()
	
	def __str__(self):
		return self.name



# Layer class
class CLayer:
	def __init__(self,name="",num=-1,bottom = False):
		self.name=name
		self.num=num
		self.blockages=[]					# list of blockages, Rectangle only
		self.bottom = bottom				# bottom orientation flag
	
	def __str__(self):
		return self.name

# Nets container class
class CPackages(CContainer):
	pass

# layer numbers
layerTOP = 1
layerBOTTOM = 2
layerGND = 3
layerVCC = 3
layerBLOCKTOP = 5
layerBLOCKBOTTOM = 6
layerSIGNAL3 = 7
layerSIGNAL4 = 8
layerSILK = 9
layerRATS = 10
layerPINPADS = 11
layerVIAS = 12
layerSOLDERMASK = 13
layerFARSIDE = 0x80			# more like a modifier flag to be combined with other
	
# Board class
class CBoard:
#	def __init__(self,sch=None,name="",path=""):
	def __init__(self,name="",path=""):
		self.units="inch"
		self.name=name
		self.path=path
		self.num=-1
		self.outline=Polygon()
#		self.sch = sch
		self.libraries=[]
		self.devices=CDevices() #{}
		self.packages=CPackages() #{}
		self.vias=[]
		self.nets=CNets() #{}
		self.pours=[]
		self.geometry=[]
		self.refids=-1
		self.layers=[]
		self.layers_number = 0
		self.bbox = Rectangle()
		
	# transfer from schematic
	def addFromSchematic(self, sch):
		for dev in sch.devices.values():
			self.addDev(dev)
			
		for net in sch.nets.values():
			self.addNet(net)
		
		for lib in sch.libraries:
			self.addLibary(net)
			
	def addLibrary(self, item):
		self.libraries.append(item)
		
	def addDev(self, item):
		self.devices[item.refid]=item
		self.packages[item.packagename]=item.package
		
	def getDev(self, refid):
		return self.devices[refid]
		
	def addNet(self, item):
		self.nets[item.name]=item
		
	def getNet(self, name):
		return self.nets[name]	

	def addLayer(self, item):
		self.layers.append(item)
		self.layers_number = self.layers_number + 1
		
	def getLayer(self,name):
		for l in self.layers:
			if l.name == name:
				return l
		return None
	
	def setOutline(self,outline):
		self.outline = outline

	

	
		

# Some tests
if __name__ == "__main__":
	schem = CSchematic()
	ic1 = CIC()
	ic1.refid ="U1"

	ic1.add( CPin("GND",1) )
	ic1.add( CPin("VCC",2) )
	schem.addPart(ic1)
	
	net1 = CNet("GND")
	net1.add(CNode(ic1,1))
	schem.addNet(net1)
	
	net2 = CNet("VCC")
	net2.add(CNode(ic1,2))
	schem.addNet(net2)
	eagle = CEagle(schem)
	eagle.outputNetlistScript()


