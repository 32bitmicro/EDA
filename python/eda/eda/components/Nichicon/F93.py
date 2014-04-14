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

# All parameters in mm
# Vertical orientation
#
class genCASE_package(package):
    def __init__(self, L, W1, W2, H, S, case):
        package.__init__(self, case+"CASE", "Nichicon", case+"CASE package")
        self.smt = True
        # S is Thickness
        X = (W1 - S) / 2
        Y = (L - S) / 2
        
        X =  X  * 39.37 * 100
        Y =  Y  * 39.37 * 100
        T =  S  * 39.37 * 100
        C = 0.4 * T
        M = 1.2 * T
        
        self.pcbbody = ''
        self.pcbbody ='(' + CRLF
        self.pcbbody += '    Pad[ ' + "%d "% -X + "%d "% -Y + "%d "% X + "%d "% -Y + "%d "% T + "%d "% C + "%d "% M + ' "+" "1" "square"]' + CRLF
        self.pcbbody += '    Pad[ ' + "%d "% -X + "%d "%  Y + "%d "% X + "%d "%  Y + "%d "% T + "%d "% C + "%d "% M + ' "-" "2" "square"]' + CRLF
        
        X = W1 / 2
        Y = L / 2
        X =  X  * 39.37 * 100 + mil2pcb(15) # expand by 15 mils
        Y =  Y  * 39.37 * 100 + mil2pcb(15) # expand by 15 mils
        
        self.pcbbody += '    ElementLine [' "%d "% -X + "%d "% -Y + "%d "%  X + "%d "% -Y + ' 800]' + CRLF
        self.pcbbody += '    ElementLine [' "%d "%  X + "%d "% -Y + "%d "%  X + "%d "%  Y + ' 800]' + CRLF
        self.pcbbody += '    ElementLine [' "%d "%  X + "%d "%  Y + "%d "% -X + "%d "%  Y + ' 800]' + CRLF
        self.pcbbody += '    ElementLine [' "%d "% -X + "%d "%  Y + "%d "% -X + "%d "% -Y + ' 800]' + CRLF
        self.pcbbody += ')'  + CRLF
        #print self.pcbbody
        
# A Case -  EIA3216-16 (1206)
# L - length 3.2 mm
# W1 - width 1.6 mm
# W2 - pad width 1.2 mm
# H - height 1.6 mm
# S - pad length 0.8 mm
class F93_A(Component):
    "Tantalum capacitor"
    def __init__(self, refid, val, name="F93_A", libname="Nichicon", symbolname="F93_A", packagename="ACASE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = genCASE_package(L=3.2, W1=1.6, W2=1.2, H=1.6, S=0.8, case='A')
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
        
# B Case -  EIA3528-21
# L - length 3.5 mm
# W1 - width 2.8 mm
# W2 - pad width 2.2 mm
# H - height 1.9 mm
# S - pad length 0.8 mm
class F93_B(Component):
    "Tantalum capacitor"
    def __init__(self, refid, val, name="F93_B", libname="Nichicon", symbolname="F93_B", packagename="BCASE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = genCASE_package(L=3.5, W1=2.8, W2=2.2, H=1.9, S=0.8, case='B')
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))


# C Case -  EIA6032-25
# L - length 6.0 mm
# W1 - width 3.2 mm
# W2 - pad width 2.2 mm
# H - height 2.5 mm
# S - pad length 1.3 mm
class F93_C(Component):
    "Tantalum capacitor"
    def __init__(self, refid, val, name="F93_C", libname="Nichicon", symbolname="F93_C", packagename="CCASE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = genCASE_package(L=6.0, W1=3.2, W2=2.2, H=2.5, S=1.3, case='C')
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
# N Case -  EIA7343-28
# L - length 7.3 mm
# W1 - width 4.3 mm
# W2 - pad width 2.4 mm
# H - height 2.8 mm
# S - pad length 1.3 mm
class F93_N(Component):
    "Tantalum capacitor"
    def __init__(self, refid, val, name="F93_N", libname="Nichicon", symbolname="F93_N", packagename="NCASE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = genCASE_package(L=7.3, W1=4.3, W2=2.4, H=2.8, S=1.3, case='N')
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
        
# All Cases -  from 0805 to EIA7343-28
# L - length 7.3 mm
# W1 - width 4.0 mm use smaller due to spacing violation!
# W2 - pad width 2.4 mm
# H - height 2.8 mm
# S - pad length 3.1 mm
class F93_ALL(Component):
    "Tantalum capacitor"
    def __init__(self, refid, val, name="F93_ALL", libname="Nichicon", symbolname="CAPTANT", packagename="ALLCASE"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = genCASE_package(L=7.3, W1=4.0, W2=2.4, H=2.8, S=3.1, case='ALL')
        self.parsePackage()
        self.addPin( CPin("+",	1    ))
        self.addPin( CPin("-",	2    ))
