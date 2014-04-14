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
class DIP24(Component):
    "DIP 24 pin module"
    def __init__(self, refid, val, name="DIP24", libname="module", symbolname="DIP24", packagename="DIP24"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = DIP_package(24,name="DIP24", libname="package",description="DIP24 module 600 mil wide, 100 mil spacing", dx = 10000, dy = 60000)                 # should call make header
        self.parsePackage()                                # do we need this?
        self.addPin( CPin("SOUT",   1    ))
        self.addPin( CPin("SIN",    2    ))
        self.addPin( CPin("ATN",    3    ))
        self.addPin( CPin("VSS_1",  4    ))
        # 5 - 20  = P0 - P15
        for i in range(16):
            self.addPin( CPin("P"+str(i),    (i+5)    ))
        self.addPin( CPin("VDD",    21    ))
        self.addPin( CPin("RESET#", 22    ))
        self.addPin( CPin("VSS_2",  23    ))
        self.addPin( CPin("VIN",    24    ))
        
