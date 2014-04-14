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
        
class FT2232D(Component):
    "FTDI FT2232D USB interface"
    def __init__(self, refid, val, name="FT2232D", libname="ftdi", symbolname="FT2232D", packagename="LQFP48"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = LQFP48()
        self.parsePackage()
        self.addPin( CPin("EESK",      1    ))
        self.addPin( CPin("EEDATA",    2    ))
        self.addPin( CPin("VCC",       3    ))
        self.addPin( CPin("RESET#",    4    ))
        self.addPin( CPin("RSTOUT#",   5    ))
        self.addPin( CPin("3V3OUT",    6    ))
        self.addPin( CPin("USBDP",     7    ))
        self.addPin( CPin("USBDM",     8    ))
        self.addPin( CPin("GND",       9    ))
        self.addPin( CPin("SI/WUA",    10    ))
        self.addPin( CPin("ACBUS3",    11    ))
        self.addPin( CPin("ACBUS2",    12    ))
        self.addPin( CPin("ACBUS1",    13    ))
        self.addPin( CPin("VCCIOA",    14    ))
        self.addPin( CPin("ACBUS0",    15    ))
        self.addPin( CPin("ADBUS7",    16    ))
        self.addPin( CPin("ADBUS6",    17    ))
        self.addPin( CPin("GND",       18    ))
        self.addPin( CPin("ADBUS5",    19    ))
        self.addPin( CPin("ADBUS4",    20    ))
        self.addPin( CPin("ADBUS3",    21    ))
        self.addPin( CPin("ADBUS2",    22    ))
        self.addPin( CPin("ADBUS1",    23    ))
        self.addPin( CPin("ADBUS0",    24    ))
        self.addPin( CPin("GND",       25    ))
        self.addPin( CPin("SI/WUB",    26    ))
        self.addPin( CPin("BCBUS3",    27    ))
        self.addPin( CPin("BCBUS2",    28    ))
        self.addPin( CPin("BCBUS1",    29    ))
        self.addPin( CPin("BCBUS0",    30    ))
        self.addPin( CPin("VCCIOB",    31    ))
        self.addPin( CPin("BDBUS7",    32    ))
        self.addPin( CPin("BDBUS6",    33    ))
        self.addPin( CPin("GND",       34    ))
        self.addPin( CPin("BDBUS5",    35    ))
        self.addPin( CPin("BDBUS4",    36    ))
        self.addPin( CPin("BDBUS3",    37    ))
        self.addPin( CPin("BDBUS2",    38    ))
        self.addPin( CPin("BDBUS1",    39    ))
        self.addPin( CPin("BDBUS0",    40    ))
        self.addPin( CPin("PWREN#",    41    ))
        self.addPin( CPin("VCC",       42    ))
        self.addPin( CPin("XTIN",      43    ))
        self.addPin( CPin("XTOUT",     44    ))
        self.addPin( CPin("AGND",      45    ))
        self.addPin( CPin("AVCC",      46    ))
        self.addPin( CPin("TEST",      47    ))
        self.addPin( CPin("EECS",      48    ))
        
        
# Some tests
if __name__ == "__main__":
    ft2232 = FT2232D("U1","","FT2232D")
    print ft2232
