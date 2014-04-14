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
   
#Orientation, + is center
#   ---
# -1   6-
# -2 + 5-
# -3   4-
#   ---

# Pad Thickness is 0.4 = 1574
# Pad Width is 0.8
# X1 X2 = Pad Width - Pad Thickness
#0.8 - 0.4 = 0.4 / 2 = 0.2
# Pad center to center is 0.65 vertically and 1.9 horizontally

#Left Side, right side is mirror
#Centers       X1       X2       X1      X2       Y
#X     Y 
#-0.85 -0.65  -1.05    -0.65   -4133   -2559   -2559
#-0.85  0     -1.05    -0.65   -4133   -2559   0
#-0.85 +0.65  -1.05    -0.65   -4133   -2559   -2559
# !!! Not Yet
class SOT363_package(package):
    def __init__(self, name="SOT363", libname="Diodes",description="SOT363 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-4133 -2559 -2559 -2559 1574 500 2000 "1" "1" "square"]
    Pad[-4133    +0 -2559    +0 1574 500 2000 "2" "2" "square"]
    Pad[-4133 +2559 -2559 +2559 1574 500 2000 "3" "3" "square"]
    Pad[+2559 +2559 +4133 +2559 1574 500 2000 "4" "4" "square"]
    Pad[+2559    -0 +4133    -0 1574 500 2000 "5" "5" "square"]
    Pad[+2559 -2559 +4133 -2559 1574 500 2000 "6" "6" "square"]
    ElementLine [-5600 +4400 +5600 +4400 1000]
    ElementLine [+5600 +4400 +5600 -4400 1000]
    ElementLine [+5600 -4400 -5600 -4400 1000]
    ElementLine [-5600 -4400 -5600 +4400 1000]
)        
        '''
           
           
#Orientation, + is center
#   ---
# -1   6-
# -2 + 5-
# -3   4-
#   ---

#Pad Thickness is 0.375 = 1476
# Pad Width is 0.5
# X1 X2 = Pad Width - Pad Thickness
#0.5 - 0.375 = 0.125 / 2 = 0.0625 

#Left Side, right side is mirror
#Centers      X1       X2       X1      X2       Y
#X     Y 
#-0.75 -0.5  -0.8125 -0.6875    -3198   -2706   -1968
#-0.75  0    -0.8125 -0.6875    -3198   -2706   0
#-0.75 +0.5  -0.8125 -0.6875    -3198   -2706   -1968

class SOT563_package(package):
    def __init__(self, name="SOT563", libname="Diodes",description="SOT563 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-3198 -1968 -2706 -1968 1476 500 2000 "1" "1" "square"]
    Pad[-3198    +0 -2706    +0 1476 500 2000 "1" "2" "square"]
    Pad[-3198 +1968 -2706 +1968 1476 500 2000 "1" "3" "square"]
    Pad[+2706 +1968 +3198 +1968 1476 500 2000 "1" "4" "square"]
    Pad[+2706    -0 +3198    -0 1476 500 2000 "1" "5" "square"]
    Pad[+2706 -1968 +3198 -1968 1476 500 2000 "1" "6" "square"]
    ElementLine [-5200 +4000 +5200 +4000 1000]
    ElementLine [+5200 +4000 +5200 -4000 1000]
    ElementLine [+5200 -4000 -5200 -4000 1000]
    ElementLine [-5200 -4000 -5200 +4000 1000]
)        
        '''
             
class BAS16V(Component):
    "Dual diode"
    def __init__(self, refid, val, name="BAS16V", libname="Diodes", symbolname="BAS16V", packagename="SOT363"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = SOT563_package()
        self.parsePackage()
        self.addPin( CPin("A1",   1    ))
        self.addPin( CPin("NC1",  2    ))
        self.addPin( CPin("C2",   3    ))
        self.addPin( CPin("A2",   4    ))
        self.addPin( CPin("NC2",  5    ))
        self.addPin( CPin("C1",   6    ))
        
        
class BAS16TW(Component):
    "Triple diode"
    def __init__(self, refid, val, name="BAS16TW", libname="Diodes", symbolname="BAS16TW", packagename="SOT363"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = SOT363_package()
        self.parsePackage()
        self.addPin( CPin("A1",   1    ))
        self.addPin( CPin("A2",   2    ))
        self.addPin( CPin("A3",   3    ))
        self.addPin( CPin("C3",   4    ))
        self.addPin( CPin("C2",   5    ))
        self.addPin( CPin("C1",   6    ))
        
# Q1 PNP Q2 NPN
class DCX100NS(Component):
    "Dual pre-biased transistor"
    def __init__(self, refid, val, name="DCX100NS", libname="Diodes", symbolname="DCX100NS", packagename="SOT563"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = SOT563_package()
        self.parsePackage()
        self.addPin( CPin("EQ1",   1    ))
        self.addPin( CPin("BQ1",   2    ))
        self.addPin( CPin("CQ2",   3    ))
        self.addPin( CPin("EQ2",   4    ))
        self.addPin( CPin("BQ2",   5    ))
        self.addPin( CPin("CQ1",   6    ))

# Q1 NPN Q2 PNP
class DCX114EU(Component):
    "Dual pre-biased transistor"
    def __init__(self, refid, val, name="DCX114EU", libname="Diodes", symbolname="DCX114EU", packagename="SOT363"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = SOT363_package()
        self.parsePackage()
        self.addPin( CPin("EQ1",   1    ))
        self.addPin( CPin("BQ1",   2    ))
        self.addPin( CPin("CQ2",   3    ))
        self.addPin( CPin("EQ2",   4    ))
        self.addPin( CPin("BQ2",   5    ))
        self.addPin( CPin("CQ1",   6    ))
