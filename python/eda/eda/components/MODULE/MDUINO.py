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
class MDUINO(package):
    def __init__(self, name="MDUINO", libname="package",description="MDUINO"):
        package.__init__(self, name, libname,description)
        # generate MDUINO
        x = 0
        y = 0
        M = 0 
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
        dx = 3000 # FIXME
        dy = 3000 # FIXME
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
