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
        
# Standard headers have 0.025" square pins
# Round pins can be 0.018" or 0.030"
class MCUCUBE_package(package):
    def __init__(self, M , name="MCUCUBE", libname="package",description="MCUCUBE 0.100 x m x m", dx = 10000, dy = 10000):
        package.__init__(self, name, libname,description)
        # generate MCUCUBE M by M
        x = 0
        y = 0
        
        SFlags1  = '"square,edge2"'
        SFlags   = '"edge2"'
        #  Good thicknes is 64 mill and drill 36 mill, will press fit
        Thickness = 6400 #7574
        Clearance = 3000
        Mask = 8174
        Drill = 3600 #4000
        num = 1
        # pins defined in a circle
	rX = 0
	rY = 0
	minum = 0
        for mi in range(M*4):
            if mi == 0:
		rX += 0
		rY += 0 
            elif mi == M*4/4:
		rX += 0
		rY += dy
            elif mi == M*4/2:
		rX += dx
		rY += 0
            elif mi == M*4*3/4:
		rX += 0
		rY += -dy

            if mi < (M*4/4):                        # upper left corner down
                rX = rX
                rY = rY + dy
            elif mi >= (M*4/4) and mi < (M*4/2) :     # lower left corner rigth 
                rX = rX + dx
                rY = rY
            elif mi >= (M*4/2) and mi < (M*4*3/4) :   # lower rigth corner up 
                rX = rX
                rY = rY - dy
            else:			            # upper right corner left
                rX = rX - dx
                rY = rY
 
            pin = CPin(str(num),num,int(rX),int(rY))
            pin.smt         = False
            pin.num         = int(num)
            pin.thickness   = int(Thickness)
            pin.clearance   = int(Clearance)
            pin.mask        = int(Mask)
            pin.drill       = int(Drill)
            pin.name        = '"' + str(num) + '"'
            if mi==0 :
            # pcb attributes
                pin.sflags       = SFlags1
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "S", pin.drill)
            else:
                pin.sflags       = SFlags
                # make pad
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "R", pin.drill )
            # make bbox covering pin with clearance, will be used for blockages    
            size = pin.thickness + pin.clearance
            x1 = int(pin.pos._x - size / 2)
            x2 = int(pin.pos._x + size / 2)
            y1 = int(pin.pos._y - size / 2)
            y2 = int(pin.pos._y + size / 2)
            pin.bbox = Rectangle(x1,y1,x2,y2,0)   
            self.pins[pin.num]=pin
            num = num  + 1
                
        X1 = x - 5000
        Y1 = y - 5000
        X2 = x + dx * (M + 1) + 5000
        Y2 = y + dy * (M + 1) + 5000
        Thickness = 1000
	# Outline
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
	# Mounting holes
	d = 25000
	ddx = 20000
	ddy = 20000
	cir = Circle(int(X1+ddx), int(Y1+ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X1+ddx), int(Y2-ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X2-ddx), int(Y1+ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X2-ddx), int(Y2-ddy),int(d),int(Thickness))
	self.geometry.append(cir)
        self.pcbbody = ''



# Standard headers have 0.025" square pins
# Round pins can be 0.018" or 0.030"
class MCUBE_package(package):
    def __init__(self, M , name="MCUBE", libname="package",description="MCUBE 0.100 x m x m", dx = 10000, dy = 10000):
        package.__init__(self, name, libname,description)
        # generate MCUBE M by M
        x = 0
        y = 0
        
        SFlags1  = '"square,edge2"'
        SFlags   = '"edge2"'
        #  Good thicknes is 64 mill and drill 36 mill, will press fit
        Thickness = 6400 #7574
        Clearance = 3000
        Mask = 8174
        Drill = 3600 #4000
        num = 1
        # pins defined in a 2 circles - inner and outer

	# outer circle 
	rX = 0 
	rY = 0 + dy
	minum = 0
        for mi in range(M*4):
            if mi == 0:
		rX += 0
		rY += 0 
            elif mi == M*4/4:
		rX += 0 + dx
		rY += 2 * dy
            elif mi == M*4/2:
		rX += 2 * dx
		rY += 0 - dy
            elif mi == M*4*3/4:
		rX += 0 - dx
		rY += 2 * -dy

            if mi < (M*4/4):                        # upper left corner down
                rX = rX
                rY = rY + dy
            elif mi >= (M*4/4) and mi < (M*4/2) :     # lower left corner rigth 
                rX = rX + dx
                rY = rY
            elif mi >= (M*4/2) and mi < (M*4*3/4) :   # lower rigth corner up 
                rX = rX
                rY = rY - dy
            else:			            # upper right corner left
                rX = rX - dx
                rY = rY
 
            pin = CPin(str(num),num,int(rX),int(rY))
            pin.smt         = False
            pin.num         = int(num)
            pin.thickness   = int(Thickness)
            pin.clearance   = int(Clearance)
            pin.mask        = int(Mask)
            pin.drill       = int(Drill)
            pin.name        = '"' + str(num) + '"'
            #if mi==0 :
            if mi == M*4/4:
            # pcb attributes square
                pin.sflags       = SFlags1
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "S", pin.drill)
            else:
                pin.sflags       = SFlags
                # make pad
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "R", pin.drill )
            # make bbox covering pin with clearance, will be used for blockages    
            size = pin.thickness + pin.clearance
            x1 = int(pin.pos._x - size / 2)
            x2 = int(pin.pos._x + size / 2)
            y1 = int(pin.pos._y - size / 2)
            y2 = int(pin.pos._y + size / 2)
            pin.bbox = Rectangle(x1,y1,x2,y2,0)   
            self.pins[pin.num]=pin
            num = num  + 1
               
	# inner circle 
	rX = 0 + dx
	rY = 0 + dy
	minum = 0
        for mi in range(M*4):
            if mi == 0:
		rX += 0
		rY += 0 
            elif mi == M*4/4:
		rX += 0
		rY += dy
            elif mi == M*4/2:
		rX += dx
		rY += 0
            elif mi == M*4*3/4:
		rX += 0
		rY += -dy

            if mi < (M*4/4):                        # upper left corner down
                rX = rX
                rY = rY + dy
            elif mi >= (M*4/4) and mi < (M*4/2) :     # lower left corner rigth 
                rX = rX + dx
                rY = rY
            elif mi >= (M*4/2) and mi < (M*4*3/4) :   # lower rigth corner up 
                rX = rX
                rY = rY - dy
            else:			            # upper right corner left
                rX = rX - dx
                rY = rY
 
            pin = CPin(str(num),num,int(rX),int(rY))
            pin.smt         = False
            pin.num         = int(num)
            pin.thickness   = int(Thickness)
            pin.clearance   = int(Clearance)
            pin.mask        = int(Mask)
            pin.drill       = int(Drill)
            pin.name        = '"' + str(num) + '"'
            # if mi==0 :
            if mi == M*4/4:
            # pcb attributes square
                pin.sflags       = SFlags1
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "S", pin.drill)
            else:
                pin.sflags       = SFlags
                # make pad
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "R", pin.drill )
            # make bbox covering pin with clearance, will be used for blockages    
            size = pin.thickness + pin.clearance
            x1 = int(pin.pos._x - size / 2)
            x2 = int(pin.pos._x + size / 2)
            y1 = int(pin.pos._y - size / 2)
            y2 = int(pin.pos._y + size / 2)
            pin.bbox = Rectangle(x1,y1,x2,y2,0)   
            self.pins[pin.num]=pin
            num = num  + 1


	# 
        X1 = x - 10000
        Y1 = y - 10000
        X2 = x + dx * (M + 3) + 10000
        Y2 = y + dy * (M + 3) + 10000
        Thickness = 1000
	# Outline
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
	# Mounting holes
	d  = 25000 # 0.25" inch spacer
	d1 = 11811 # 3 mm whole
	ddx = 12500
	ddy = 12500
	cir = Circle(int(X1+ddx), int(Y1+ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X1+ddx), int(Y1+ddy),int(d1),int(Thickness))
	self.geometry.append(cir)

	cir = Circle(int(X1+ddx), int(Y2-ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X1+ddx), int(Y2-ddy),int(d1),int(Thickness))
	self.geometry.append(cir)

	cir = Circle(int(X2-ddx), int(Y1+ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X2-ddx), int(Y1+ddy),int(d1),int(Thickness))
	self.geometry.append(cir)

	cir = Circle(int(X2-ddx), int(Y2-ddy),int(d),int(Thickness))
	self.geometry.append(cir)
	cir = Circle(int(X2-ddx), int(Y2-ddy),int(d1),int(Thickness))
	self.geometry.append(cir)

        self.pcbbody = ''




class MCUBE(Component):
    "MCUBE 17x2 x 17x2 pin module"
    def __init__(self, refid, val, name="MCUBE", libname="module", symbolname="MCUBE", packagename="MCUBE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = MCUBE_package(17,name="MCUBE", libname="package",description="MCUBE module 2000 mil wide, 100 mil spacing", dx = 10000, dy = 10000)                 # should call make header
        self.parsePackage()                                	# do we need this?
        for i in range(136):					# 17x2x4 = 136 
            self.addPin( CPin("P"+str(i),    (i+1)    ))

#        self.addPin( CPin("SOUT",   1    ))
#        self.addPin( CPin("SIN",    2    ))
#        self.addPin( CPin("ATN",    3    ))
#        self.addPin( CPin("VSS_1",  4    ))
#        # 5 - 20  = P0 - P15
#        for i in range(16):
#            self.addPin( CPin("P"+str(i),    (i+5)    ))
#        # 21 - 36 = X0 - X15
#        for i in range(16):
#            self.addPin( CPin("X"+str(i),    (i+21)    ))
#        self.addPin( CPin("VDD",    37    ))
#        self.addPin( CPin("RESET#", 38    ))
#        self.addPin( CPin("VSS_2",  39    ))
#        self.addPin( CPin("VIN",    40    ))


class MCUBE20(Component):
    "MCUBE 20 x 20 pin module"
    def __init__(self, refid, val, name="MCUBE20", libname="module", symbolname="MCUBE20", packagename="MCUBE20"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = MCUCUBE_package(20,name="MCUCUBE20", libname="package",description="MCUCUBE20 module 2000 mil wide, 100 mil spacing", dx = 10000, dy = 10000)                 # should call make header
        self.parsePackage()                                # do we need this?
        for i in range(80):
            self.addPin( CPin("P"+str(i),    (i+1)    ))

#        self.addPin( CPin("SOUT",   1    ))
#        self.addPin( CPin("SIN",    2    ))
#        self.addPin( CPin("ATN",    3    ))
#        self.addPin( CPin("VSS_1",  4    ))
#        # 5 - 20  = P0 - P15
#        for i in range(16):
#            self.addPin( CPin("P"+str(i),    (i+5)    ))
#        # 21 - 36 = X0 - X15
#        for i in range(16):
#            self.addPin( CPin("X"+str(i),    (i+21)    ))
#        self.addPin( CPin("VDD",    37    ))
#        self.addPin( CPin("RESET#", 38    ))
#        self.addPin( CPin("VSS_2",  39    ))
#        self.addPin( CPin("VIN",    40    ))
        
