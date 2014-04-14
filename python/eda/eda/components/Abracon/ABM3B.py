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
   
# ll Pad ll and ur corner
# -11550 -7050 -4450 -2350
# Thickness is 4700
# Coordinates of the pad line, x coordinates subtract 1/2 of the Thicknes
# -9200, -4700, -6800, -4700
# View from top
#
#  4  3 
#  1  2
#
class ABM3B_package(package):
    def __init__(self, name="ABM3B", libname="Abracon",description="ABM3B package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-9200 +4700 -6800 +4700 4700 2000 6000 "1" "1" "square"]
    Pad[+9200 +4700 +6800 +4700 4700 2000 6000 "GND" "2" "square"]
    Pad[+9200 -4700 +6800 -4700 4700 2000 6000 "3" "3" "square"]
    Pad[-9200 -4700 -6800 -4700 4700 2000 6000 "GND" "4" "square"]
    ElementLine [-12500 +8000 +12500 +8000 1000]
    ElementLine [+12500 +8000 +12500 -8000 1000]
    ElementLine [+12500 -8000 -12500 -8000 1000]
    ElementLine [-12500 -8000 -12500 +8000 1000]
)        
        '''
                
class ABM3B(Component):
    "Ceramic crystal 5.0 x 3.2 mm"
    def __init__(self, refid, val, name="ABM3B", libname="Abracon", symbolname="ABM3B", packagename="ABM3B"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = ABM3B_package()
        self.parsePackage()
        self.addPin( CPin("1",    1    ))
        self.addPin( CPin("GND_2",    2    ))
        self.addPin( CPin("3",    3    ))
        self.addPin( CPin("GND_4",   4    ))

             
