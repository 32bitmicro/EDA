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
		
class LPC210X(Component):
	"LPC2101/2/3 chip class "
	def __init__(self, refid, val, name="lpc210x", libname="lpc2000", symbolname="lpc210x", packagename="LQFP48"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = LQFP48()
		self.parsePackage()
		self.addPin( CPin("P0.19/MAT1.2/MISO1", 		1	))
		self.addPin( CPin("P0.20/MAT1.3/MOSI1", 		2	))
		self.addPin( CPin("P0.21/MAT3.0/SSEL1", 		3	))
		self.addPin( CPin("VBATT", 						4	))
		self.addPin( CPin("VDD1V8", 					5	))
		self.addPin( CPin("~RST", 						6	))
		self.addPin( CPin("VSS_1", 						7	))
		self.addPin( CPin("P0.27/TRST/CAP2.0", 			8	))
		self.addPin( CPin("P0.28/TMS/CAP2.1", 			9	))
		self.addPin( CPin("P0.29/TCK/CAP2.2", 			10	))
		self.addPin( CPin("X1", 						11	))
		self.addPin( CPin("X2", 						12	))
		self.addPin( CPin("P0.0/TXD0/MAT3.1", 			13	))
		self.addPin( CPin("P0.1/RXD0/MAT3.2", 			14	))
		self.addPin( CPin("P0.30/TDI/MAT3.3", 			15	))
		self.addPin( CPin("P0.31/TDO", 					16	))
		self.addPin( CPin("VDD3V3_1", 					17	))
		self.addPin( CPin("P0.2/SCL0/CAP0.0", 			18	))
		self.addPin( CPin("VSS_2", 						19	))
		self.addPin( CPin("RTXC1", 						20	))
		self.addPin( CPin("P0.3/SDA0/MAT0.0",			21	))
		self.addPin( CPin("P0.4/SCK0/CAP0.1", 			22	))
		self.addPin( CPin("P0.5/MISO0/MAT0.1", 			23	))
		self.addPin( CPin("P0.6/MOSI0/CAP0.2", 			24	))
		self.addPin( CPin("RTXC2", 						25	))
		self.addPin( CPin("RTCK", 						26	))
		self.addPin( CPin("DBGSEL", 					27	))
		self.addPin( CPin("P0.7/SSEL0/MAT2.0", 			28	))
		self.addPin( CPin("P0.8/TXD1/MAT2.1", 			29	))
		self.addPin( CPin("P0.9/RXD1/MAT2.2", 			30	))
		self.addPin( CPin("VSSA",	 					31	))
		self.addPin( CPin("P0.22/AD0.0", 				32	))
		self.addPin( CPin("P0.23/AD0.1", 				33	))
		self.addPin( CPin("P0.24/AD0.2", 				34	))
		self.addPin( CPin("P0.10/RTS1/CAP1.0/AD0.3",	35	))
		self.addPin( CPin("P0.11/CTS1/CAP1.1/AD0.4", 	36	))
		self.addPin( CPin("P0.12/DSR1/MAT1.0/AD0.5", 	37	))
		self.addPin( CPin("P0.25/AD0.6", 				38	))
		self.addPin( CPin("P0.26/AD0.7", 				39	))
		self.addPin( CPin("VDD3V3_2", 					40	))
		self.addPin( CPin("P0.13/DTR1/MAT1.1", 			41	))
		self.addPin( CPin("VDDA",	 					42	))
		self.addPin( CPin("VSS_3", 						43	))
		self.addPin( CPin("P0.14/DCD1/SCK1/EINT1/~BSL", 44	))
		self.addPin( CPin("P0.15/RI1/EINT2", 			45	))
		self.addPin( CPin("P0.16/EINT0/MAT0.2", 		46	))
		self.addPin( CPin("P0.17/CAP1.2/SCL1", 			47	))
		self.addPin( CPin("P0.18/CAP1.3/SDA1", 			48	))
		
		
# Some tests
if __name__ == "__main__":
	lpc2103 = LPC210X("U1","","LPC2103")
	print lpc2103


