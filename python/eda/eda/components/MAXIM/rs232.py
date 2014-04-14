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
		
class MAX3232(Component):
	"MAX3232 chip class "
	def __init__(self, refid, val, name="MAX3232", libname="MAXIM", symbolname="MAX3232", packagename="TSSOP16"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = TSSOP16()
		self.parsePackage()
		self.addPin( CPin("C1+", 		1	))
		self.addPin( CPin("V+", 		2	))
		self.addPin( CPin("C1-", 		3	))
		self.addPin( CPin("C2+", 		4	))
		self.addPin( CPin("C2-", 		5	))
		self.addPin( CPin("V-", 		6	))
		self.addPin( CPin("T2OUT", 		7	))
		self.addPin( CPin("R2IN", 		8	))
		self.addPin( CPin("R2OUT", 		9	))
		self.addPin( CPin("T2IN", 		10	))
		self.addPin( CPin("T1IN", 		11	))
		self.addPin( CPin("R1OUT", 		12	))
		self.addPin( CPin("R1IN", 		13	))
		self.addPin( CPin("T1OUT", 		14	))
		self.addPin( CPin("GND", 		15	))
		self.addPin( CPin("VCC", 		16	))
		
# Some tests
if __name__ == "__main__":
	max3232 = MAX3232("U1","","MAX3232")
	print max3232


