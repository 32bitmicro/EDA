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


class MultiPowerSO30(package):
    def __init__(self, name="MultiPowerSO30", libname="ST",description="MultiPowerSO-30"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-4300 2700 -1200 2700 1500 3000 2100 "1" "1" ""]
    Pad[-4300 5800 -1200 5800 1500 3000 2100 "2" "2" "square"]
    Pad[-4300 8900 -1200 8900 1500 3000 2100 "3" "3" "square"]
    Pad[-4300 12100 -1200 12100 1500 3000 2100 "4" "4" "square"]
    Pad[-4300 15200 -1200 15200 1500 3000 2100 "5" "5" "square"]
    Pad[-4300 18400 -1200 18400 1500 3000 2100 "6" "6" "square"]
    Pad[-4300 21500 -1200 21500 1500 3000 2100 "7" "7" "square"]
    Pad[-4300 24700 -1200 24700 1500 3000 2100 "8" "8" "square"]
    Pad[2700 28700 2700 31800 1500 3000 2100 "9" "9" "square,edge2"]
    Pad[5800 28700 5800 31800 1500 3000 2100 "10" "10" "square,edge2"]
    Pad[8900 28700 8900 31800 1500 3000 2100 "11" "11" "square,edge2"]
    Pad[12100 28700 12100 31800 1500 3000 2100 "12" "12" "square,edge2"]
    Pad[15200 28700 15200 31800 1500 3000 2100 "13" "13" "square,edge2"]
    Pad[18400 28700 18400 31800 1500 3000 2100 "14" "14" "square,edge2"]
    Pad[21500 28700 21500 31800 1500 3000 2100 "15" "15" "square,edge2"]
    Pad[24700 28700 24700 31800 1500 3000 2100 "16" "16" "square,edge2"]
    Pad[28700 24800 31800 24800 1500 3000 2100 "17" "17" "square,edge2"]
    Pad[28700 21700 31800 21700 1500 3000 2100 "18" "18" "square,edge2"]
    Pad[28700 18600 31800 18600 1500 3000 2100 "19" "19" "square,edge2"]
    Pad[28700 15400 31800 15400 1500 3000 2100 "20" "20" "square,edge2"]
    Pad[28700 12300 31800 12300 1500 3000 2100 "21" "21" "square,edge2"]
    Pad[28700 9100 31800 9100 1500 3000 2100 "22" "22" "square,edge2"]
    Pad[28700 6000 31800 6000 1500 3000 2100 "23" "23" "square,edge2"]
    Pad[28700 2800 31800 2800 1500 3000 2100 "24" "24" "square,edge2"]
    Pad[24800 -4300 24800 -1200 1500 3000 2100 "25" "25" "square"]
    Pad[21700 -4300 21700 -1200 1500 3000 2100 "26" "26" "square"]
    Pad[18600 -4300 18600 -1200 1500 3000 2100 "27" "27" "square"]
    Pad[15400 -4300 15400 -1200 1500 3000 2100 "28" "28" "square"]
    Pad[12300 -4300 12300 -1200 1500 3000 2100 "29" "29" "square"]
    Pad[9100 -4300 9100 -1200 1500 3000 2100 "30" "30" "square"]
    Pad[6000 -4300 6000 -1200 1500 3000 2100 "31" "31" "square"]
    Pad[2800 -4300 2800 -1200 1500 3000 2100 "32" "32" "square"]
    ElementLine [2800 0 27500 0 1000]
    ElementLine [27500 0 27500 27500 1000]
    ElementLine [27500 27500 0 27500 1000]
    ElementLine [0 27500 0 2800 1000]
    ElementLine [0 2800 2800 0 1000]
    ElementArc [3500 3500 1000 1000 0 360 1000]
)        
        '''
        
class VNH2SP30(Component):
    "VNH2SP30 in 150 mil SO8 narrow"
    def __init__(self, refid, val, name="VNH2SP30", libname="ST", symbolname="VNH2SP30-E", packagename="MultiPowerSO30"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = MultiPowerSO30()
        self.parsePackage()
        self.addPin( CPin("RO",   1    ))
        self.addPin( CPin("RE#",  2    ))
        self.addPin( CPin("DE",   3    ))
        self.addPin( CPin("DI",   4    ))
        self.addPin( CPin("GND",  5    ))
        self.addPin( CPin("A",    6    ))
        self.addPin( CPin("B",    7    ))
        self.addPin( CPin("VCC",  8    ))
        
