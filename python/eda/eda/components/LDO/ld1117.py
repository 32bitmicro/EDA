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


# LD1117 LDOs

# LDOs in SOT223
class LD1117(Component):
    "LD1117 LDO class "
    def __init__(self, refid, val, name="ld1117S33", libname="ldo", symbolname="ld1117", packagename="SOT223"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = SOT223()
        self.parsePackage()
        self.addPin( CPin("GND",    1    ))
        self.addPin( CPin("OUT",    2    ))
        self.addPin( CPin("IN",     3    ))
        self.addPin( CPin("GND2",   4    ))        
        
class LD1117S33(LD1117):
    "LD11173V3 LDO class "
    def __init__(self, refid, val, name="ld1117S33", libname="ldo", symbolname="ld1117", packagename="SOT223"):
        LD1117.__init__(self, refid, val, name, libname, symbolname, packagename)
        
class LD1117S18(LD1117):
    "LD11171V8 LDO class "
    def __init__(self, refid, val, name="ld1117S18", libname="ldo", symbolname="ld1117", packagename="SOT223"):
        LD1117.__init__(self, refid, val, name, libname, symbolname, packagename)
