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

import re
from eda import *
from eda.packages.package import *
# additional module for parsing
from simpleparse.common import numbers, strings, comments

CRLF = '\n'

# Coordinate system used is the same as GNU PCB
# Origin (0,0) is in the Upper Left corner
# Positive X coordinates extend right
# Negative X coordinates extend left
# Positive Y coordinates extend down
# Negative Y coordinates extend up
# Angle (Rotation) is incremented clockwise (right turn)
# All packages are defined as looking from top (top layer) 

#
# Components
#
class Component(CDev):
    def __init__(self, refid="", val="", name="", libname="", symbolname="" , packagename=""):
        CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.parsed=False
        self.datasheet=""
        self.drawing=""
         
    # parse
    # The lowest x and y coordinates of all sub-objects of an element are used as an attachment
    # point for the cross hair cursor of the main window, unless the element has a mark, in which
    # case that's the attachement point 
    
    def parsePad(self,args):
        #print 'Pad ' + args
#       Pad[-7500 7000 -7500 13500 2787 1600 3787 "" "1" "square,edge2"]
#       Pad [rX1 rY1 rX2 rY2 Thickness Clearance Mask "Name" "Number" SFlags]
#       Pad [rX1 rY1 rX2 rY2 Thickness Clearance Mask "Name" "Number" SFlags]
        rX1, rY1, rX2, rY2, Thickness, Clearance, Mask, Name, Number, SFlags = args.split()
        rX1 = int(rX1)
        rY1 = int(rY1)
        rX2 = int(rX2)
        rY2 = int(rY2)
        # Calculate center of the pad
        rX = int((rX1 + rX2) / 2)
        rY = int((rY1 + rY2) / 2)
        pin = CPin(Name,Number,rX,rY)
        pin.smt = True
        pin.num = int(Number.strip('"'))
        pin.thickness    = int(Thickness)
        pin.clearance    = int(Clearance)
        pin.mask         = int(Mask)
        # pcb attributes
        pin.rX1 = rX1
        pin.rY1 = rY1
        pin.rX2 = rX2
        pin.rY2 = rY2
        pin.sflags       = SFlags
        # make pad
        sizex = abs(rX1 - rX2) + pin.thickness    # distance between rX1 and rX2 + thinckess
        sizey = abs(rY1 - rY2) + pin.thickness    # rY1 and rY2 should be same so thinckess is sizey
        pin.pad = CPad(sizex, sizey, "S")
        
        size = pin.thickness + pin.clearance
        # make bbox and normalize it
        pin.bbox = Rectangle(rX1,rY1,rX2,rY2,0)
        # # make bbox covering pin with clearance, will be used for blockages
        rX1=pin.bbox.ll._x - size / 2
        rY1=pin.bbox.ll._y - size / 2
        rX2=pin.bbox.ur._x + size / 2
        rY2=pin.bbox.ur._y + size / 2
        pin.bbox = Rectangle(rX1,rY1,rX2,rY2,0)
        
        self.package.pins[pin.num]=pin
        
        
    def parsePin(self,args):
        #print 'Pin ' + args
#       Pin 16200 7000 7200 2000 9200 5200 "" "9" 0x01
#       Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
        rX, rY, Thickness, Clearance, Mask, Drill, Name, Number, SFlags = args.split()
        pin = CPin(Name,Number,int(rX),int(rY))
        pin.smt = False
        pin.num = int(Number.strip('"'))
        pin.thickness    = int(Thickness)
        pin.clearance    = int(Clearance)
        pin.mask         = int(Mask)
        pin.drill        = int(Drill)
        # pcb attributes
        pin.sflags       = SFlags
        sizex = pin.thickness
        sizey = pin.thickness
        pin.pad = CPad(sizex, sizey, "R", pin.drill)
        # make bbox covering pin with clearance, will be used for blockages    
        size = pin.thickness + pin.clearance
        x1 = int(pin.pos._x - size / 2)
        x2 = int(pin.pos._x + size / 2)
        y1 = int(pin.pos._y - size / 2)
        y2 = int(pin.pos._y + size / 2)
        pin.bbox = Rectangle(x1,y1,x2,y2,0)
        self.package.pins[pin.num]=pin

    def parseLine(self,args):
        #print 'Line ' + args
#       ElementLine [X1 Y1 X2 Y2 Thickness]
        X1, Y1, X2, Y2, Thickness = args.split()
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.package.geometry.append(line)

    def parseArc(self,args):
        #print 'Arc ' + args
#       ElementArc [X Y Width Height StartAngle DeltaAngle Thickness]
        #print ' parse Arc'
        X, Y, Width, Height, StartAngle, DeltaAngle, Thickness = args.split()
        arc = Arc( int(X), int(Y), int(Width), int(Height), int(StartAngle), int(DeltaAngle), int(Thickness))
        self.package.geometry.append(arc)

    # parse PCB package description and create device pins based on the package
    def parsePackage(self):
        #print 'parsing: "' + self.package.name + '" "' + self.package.description + '"'
        for line in self.package.pcbbody.splitlines():
            # filter out blank lines/comment lines
            lines = line.strip()
            
            # comment
            if not lines or lines.startswith('#'):
                continue
            # begin element body
            if not lines or lines.startswith('('):
                continue
            
            # end element body
            if not lines or lines.startswith(')'):
                continue
            
            words = lines.split('[')
            tag = words[0]
            tag = tag.strip()
###            print 'tag |' + tag + '|'
            args = words[1]
            args=args.strip('[]')
             
            if ( tag == 'Pad'):
                self.parsePad(args)
                
            if ( tag == 'Pin'):
                self.parsePin(args)
                
            if ( tag == 'ElementLine'):
                self.parseLine(args)
                
            if ( tag == 'ElementArc'):
                self.parseArc(args)
                
        # mark it parsed        
        self.parsed=True

#
# Some  Components/Devices
#

class FIDUCIAL_L(Component):
    "Local FIDUCIAL class"
    def __init__(self, refid, val, name="fiducial_l", libname="fiducial", symbolname="fiducial_", packagename="FIDUCIAL"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        # make 1 mm local fiducial, val is size in mm
        self.package = FIDUCIAL_package(val, 1)	# default layer should be top ie 1
        self.parsePackage()
    
    
    
# will take package size as a parameter
class RESSMT(Component):
    "RESSMT class "
    def __init__(self, refid, val, name="resistor", libname="resistor", symbolname="resistor", packagename="RES0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = RES0805()
        self.parsePackage()
        self.addPin( CPin("1",    1    ))
        self.addPin( CPin("2",    2    ))
        
# will take package size as a parameter
class CAPSMT(Component):
    "CAPSMT class "
    def __init__(self, refid, val, name="capacitor", libname="capacitor", symbolname="capacitor", packagename="CAP0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = CAP0805()
        self.parsePackage()
        self.addPin( CPin("1",    1    ))
        self.addPin( CPin("2",    2    ))
        
# will take package size as a parameter
class LEDSMT(Component):
    "LEDSMT class "
    def __init__(self, refid, val, name="LEDSMT", libname="LED", symbolname="LED", packagename="LED0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = LED0805()
        self.parsePackage()
        self.addPin( CPin("K",    1    ))
        self.addPin( CPin("A",    2    ))
        
# will take package size as a parameter
class DIODESMT(Component):
    "DIODESMT class "
    def __init__(self, refid, val, name="DIODESMT", libname="DIODE", symbolname="DIODE", packagename="DIODE0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = DIODE0805()
        self.parsePackage()
        self.addPin( CPin("K",    1    ))
        self.addPin( CPin("A",    2    ))
        
# will take package size as a parameter
class CAPPOLYSMT(Component):
    "CAPPOLYSMT class "
    def __init__(self, refid, val, name="capacitor_poly", libname="capacitor", symbolname="capacitor_poly", packagename="EIA7343"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = EIA7343()
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
class CAPTANTSMT(Component):
    "CAPTANTSMT class "
    def __init__(self, refid, val, name="capacitor_tantalum", libname="capacitor", symbolname="capacitor_tantalum", packagename="EIA7343"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = EIA7343()
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
class HEADER(Component):
    "Header class "
    def __init__(self, M,N,refid, val, name="header", libname="header", symbolname="header", packagename="HEADER_MXN_package"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HEADER_package(M,N,packagename,libname) # should call make header
        self.parsePackage()
        for i in range(M*N):
            self.addPin( CPin(str(i+1),    (i+1)    ))
            
class HC08201(Component):
    "HC08201 LCD class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="hc08201", packagename="HEADER_7X2"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HC08201_package(packagename,libname) # should call make header
        self.parsePackage()
        self.addPin( CPin('VSS',    1    ))
        self.addPin( CPin('VDD',    2    ))
        self.addPin( CPin('V0',     3    ))
        self.addPin( CPin('RS',     4    ))
        self.addPin( CPin('R/W',    5    ))
        self.addPin( CPin('E',      6    ))
        self.addPin( CPin('DB0',    7    ))
        self.addPin( CPin('DB1',    8    ))
        self.addPin( CPin('DB2',    9    ))
        self.addPin( CPin('DB3',    10   ))
        self.addPin( CPin('DB4',    11   ))
        self.addPin( CPin('DB5',    12   ))
        self.addPin( CPin('DB6',    13   ))
        self.addPin( CPin('DB7',    14   ))
        
           
class JTAG7X2(Component):
    "JTAG 14 pin 7x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag7x2", packagename="HEADER_7X2"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HEADER_package(7, 2, packagename, libname, "JTAG 14 pin 7x2")
        self.parsePackage()
        self.addPin( CPin('VDD_1',  1    ))
        self.addPin( CPin('VSS_1',  2    ))
        self.addPin( CPin('nTRST',  3    ))
        self.addPin( CPin('VSS_2',  4    ))
        self.addPin( CPin('TDI',    5    ))
        self.addPin( CPin('VSS_3',  6    ))
        self.addPin( CPin('TMS',    7    ))
        self.addPin( CPin('VSS_4',  8    ))
        self.addPin( CPin('TCK',    9    ))
        self.addPin( CPin('VSS_5',  10   ))
        self.addPin( CPin('TDO',    11   ))
        self.addPin( CPin('nRESET', 12   ))
        self.addPin( CPin('VDD_2',  13   ))
        self.addPin( CPin('VSS_6',  14   ))

class JTAG10X2(Component):
    "JTAG 20 pin 10x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag10x2", packagename="HEADER_10X2"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HEADER_package(10, 2, packagename, libname, "JTAG 20 pin 10x2")
        self.parsePackage()
        self.addPin( CPin('VDD_1',  1    ))
        self.addPin( CPin('VDD_2',  2    ))
        self.addPin( CPin('nTRST',  3    ))
        self.addPin( CPin('VSS_1',  4    ))
        self.addPin( CPin('TDI',    5    ))
        self.addPin( CPin('VSS_2',  6    ))
        self.addPin( CPin('TMS',    7    ))
        self.addPin( CPin('VSS_3',  8    ))
        self.addPin( CPin('TCK',    9    ))
        self.addPin( CPin('VSS_4',  10   ))
        self.addPin( CPin('NC_1',   11   ))
        self.addPin( CPin('VSS_5',  12   ))
        self.addPin( CPin('TDO',    13   ))
        self.addPin( CPin('VSS_6',  14   ))
        self.addPin( CPin('nRST',   15   ))
        self.addPin( CPin('VSS_7',  16   ))
        self.addPin( CPin('NC_2',   17   ))
        self.addPin( CPin('VSS_8',  18   ))
        self.addPin( CPin('NC_3',   19   ))
        self.addPin( CPin('VSS_9',  20   ))

class JTAG10X2_SMT(Component):
    "JTAG SMT 20 pin 10x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag10x2", packagename="HEADER_SMT_10X2"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HEADER_SMT_package(10, 2, packagename, libname, "JTAG SMT 20 pin 10x2")
        self.parsePackage()
        self.addPin( CPin('VDD_1',  1    ))
        self.addPin( CPin('VDD_2',  2    ))
        self.addPin( CPin('nTRST',  3    ))
        self.addPin( CPin('VSS_1',  4    ))
        self.addPin( CPin('TDI',    5    ))
        self.addPin( CPin('VSS_2',  6    ))
        self.addPin( CPin('TMS',    7    ))
        self.addPin( CPin('VSS_3',  8    ))
        self.addPin( CPin('TCK',    9    ))
        self.addPin( CPin('VSS_4',  10   ))
        self.addPin( CPin('NC_1',   11   ))
        self.addPin( CPin('VSS_5',  12   ))
        self.addPin( CPin('TDO',    13   ))
        self.addPin( CPin('VSS_6',  14   ))
        self.addPin( CPin('nRST',   15   ))
        self.addPin( CPin('VSS_7',  16   ))
        self.addPin( CPin('NC_2',   17   ))
        self.addPin( CPin('VSS_8',  18   ))
        self.addPin( CPin('NC_3',   19   ))
        self.addPin( CPin('VSS_9',  20   ))

class XTAL(Component):
    "XTAL class "
    def __init__(self, refid, val, name="xtal", libname="xtal", symbolname="xtal", packagename="HCU49"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HCU49()
        self.parsePackage()
        self.addPin( CPin("X1",    1    ))
        self.addPin( CPin("X2",    2    ))
        
class DSUB9F(Component):
    "DSUB9F class "
    def __init__(self, refid, val, name="dsub9", libname="connector", symbolname="dsub9", packagename="DSUB9F"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = DSUB9F_package()
        self.parsePackage()
        # first 9 pins are connector pins
        for i in range(9):
            self.addPin( CPin(str(i),    (i+1)    ))
        # last 2 are mount pins
        self.addPin( CPin("COVER1",    10    ))
        self.addPin( CPin("COVER2",    11    ))
                        
class BUTTON_TH(Component):
    "BUTTON_TH class "
    def __init__(self, refid, val, name="BUTTON_TH", libname="connector", symbolname="button_th", packagename="BUTTON_TH"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = BUTTON_TH_package()
        self.parsePackage()
        # first 9 pins are connector pins
        for i in range(4):
            self.addPin( CPin(str(i),    (i+1)    ))            
