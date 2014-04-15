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
		
class LPC213X(Component):
	"LPC2138/6/4/2/1 64 pin"
	def __init__(self, refid, val, name="lpc213x", libname="lpc2000", symbolname="lpc213x", packagename="LQFP64"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = LQFP64()
		self.parsePackage()
		# pins
		self.addPin( CPin("P0.21/PWM5/AD1.6/CAP1.3",		1))
		self.addPin( CPin("P0.22/AD1.7/CAP0.0/MAT0.0",		2))  
		self.addPin( CPin("RTXC1",							3))  
		self.addPin( CPin("P1.19/TRACEPKT3",				4))  
		self.addPin( CPin("RTXC2",							5))
		self.addPin( CPin("VSS_1",							6))  
		self.addPin( CPin("VDDA",							7))
		self.addPin( CPin("P1.18/TRACEPKT2",				8))
		self.addPin( CPin("P0.25/AD0.4/AOUT",				9))
		self.addPin( CPin("P0.26/AD0.5",					10))
		self.addPin( CPin("P0.27/AD0.0/CAP0.1/MAT0.1",		11))
		self.addPin( CPin("P1.17/TRACEPKT1",				12))
		self.addPin( CPin("P0.28/AD0.1/CAP0.2/MAT0.2",		13))
		self.addPin( CPin("P0.29/AD0.2/CAP0.3/MAT0.3",		14))
		self.addPin( CPin("P0.30/AD0.3/EINT3/CAP0.0",		15))
		self.addPin( CPin("P1.16/TRACEPKT0",				16))
		self.addPin( CPin("P0.31/UP_LED/CONNECT",			17))
		self.addPin( CPin("VSS_2",							18))
		self.addPin( CPin("P0.0/TXD0/PWM1",					19))
		self.addPin( CPin("P1.31/#TRST",					20))
		self.addPin( CPin("P0.1/RXD0/PWM3/EINT0",			21))
		self.addPin( CPin("P0.2/SCL0/CAP0.0",				22))
		self.addPin( CPin("VDD_1",							23))
		self.addPin( CPin("P1.26/RTCK",						24))
		self.addPin( CPin("VSS_3",							25))
		self.addPin( CPin("P0.3/SDA0/MAT0.0/EINT1",			26))
		self.addPin( CPin("P0.4/SCK0/CAP0.1/AD0.6",			27))
		self.addPin( CPin("P1.25/EXTIN0",					28))
		self.addPin( CPin("P0.5/MISO0/MAT0.1/AD0.7",		29))
		self.addPin( CPin("P0.6/MOSI0/CAP0.2/AD1.0",		30))
		self.addPin( CPin("P0.7/SSEL0/PWM2/EINT2",			31))
		self.addPin( CPin("P1.24/TRACECLK",					32))
		self.addPin( CPin("P0.8/TXD1/PWM4/A1.1",			33))
		self.addPin( CPin("P0.9/RXD1/PWM6/EINT3",			34))
		self.addPin( CPin("P0.10/RTS1/CAP1.0/AD1.2",		35))
		self.addPin( CPin("P1.23/PIPESTAT2",				36))
		self.addPin( CPin("P0.11/CTS1/CAP1.1/SCL1",			37))
		self.addPin( CPin("P0.12/DSR1/MAT1.0/AD1.3",		38))
		self.addPin( CPin("P0.13/DTR1/MAT1.1/AD1.4",		39))
		self.addPin( CPin("P1.22/PIPESTAT1",				40))
		self.addPin( CPin("P0.14/DCD1/EINT1/SDA1/",			41))
		self.addPin( CPin("VSS_4",							42))
		self.addPin( CPin("VDD_2",							43))
		self.addPin( CPin("P1.21/PIPESTAT0",				44))
		self.addPin( CPin("P0.15/RI1/EINT2/AD1.5",			45))
		self.addPin( CPin("P0.16/EINT0/MAT0.2/CAP0.2",		46))
		self.addPin( CPin("P0.17/CAP1.2/SCK1/MAT1.2",		47))
		self.addPin( CPin("P1.20/TRACESYNC",				48))
		self.addPin( CPin("VBAT",							49))
		self.addPin( CPin("VSS_5",							50))
		self.addPin( CPin("VDD_3",							51))
		self.addPin( CPin("P1.30/TMS",						52))
		self.addPin( CPin("P0.18/CAP1.3/MISO1/MAT1.3",		53))
		self.addPin( CPin("P0.19/MAT1.2/MOSI1/CAP1.2",		54))
		self.addPin( CPin("P0.20/MAT1.3/SSEL1/EINT3",		55))
		self.addPin( CPin("P1.29/TCK",						56))
		self.addPin( CPin("#RESET",							57))
		self.addPin( CPin("P0.23",							58))
		self.addPin( CPin("VSSA",							59))
		self.addPin( CPin("P1.28/TDI",						60))
		self.addPin( CPin("XTAL2",							61))
		self.addPin( CPin("XTAL1",							62))
		self.addPin( CPin("VREF",							63))
		self.addPin( CPin("P1.27/TDO",						64))


# Some tests
if __name__ == "__main__":
	lpc213x = LPC213X("U1","","LPC213X")
	print lpc213x


