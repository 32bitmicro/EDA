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

# Pad [rX1 rY1 rX2 rY2 Thickness Clearance Mask "Name" "Number" SFlags] 
# 1/100 mil	
class HVQFN33(package):
    def __init__(self, name="HVQFN33", libname="package",description="HVQFN33 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
	# footgen HVQFN33 
        s = """
(
	Pad[-14371  -8956 -11615  -8956 1575  0 1575 "1" "1"   0x00000100]
	Pad[-14371  -6397 -11615  -6397 1575  0 1575 "2" "2"   0x00000100]
	Pad[-14371  -3838 -11615  -3838 1575  0 1575 "3" "3"   0x00000100]
	Pad[-14371  -1279 -11615  -1279 1575  0 1575 "4" "4"   0x00000100]
	Pad[-14371   1280 -11615   1280 1575  0 1575 "5" "5"   0x00000100]
	Pad[-14371   3839 -11615   3839 1575  0 1575 "6" "6"   0x00000100]
	Pad[-14371   6398 -11615   6398 1575  0 1575 "7" "7"   0x00000100]
	Pad[-14371   8957 -11615   8957 1575  0 1575 "8" "8"   0x00000100]
	Pad[ 11614   8956  14370   8956 1575  0 1575 "17" "17" 0x00000100]
	Pad[ 11614   6397  14370   6397 1575  0 1575 "18" "18" 0x00000100]
	Pad[ 11614   3838  14370   3838 1575  0 1575 "19" "19" 0x00000100]
	Pad[ 11614   1279  14370   1279 1575  0 1575 "20" "20" 0x00000100]
	Pad[ 11614  -1280  14370  -1280 1575  0 1575 "21" "21" 0x00000100]
	Pad[ 11614  -3839  14370  -3839 1575  0 1575 "22" "22" 0x00000100]
	Pad[ 11614  -6398  14370  -6398 1575  0 1575 "23" "23" 0x00000100]
	Pad[ 11614  -8957  14370  -8957 1575  0 1575 "24" "24" 0x00000100]
	Pad[ -8956  11614  -8956  14370 1575  0 1575 "9" "9"   0x00000100]
	Pad[ -6397  11614  -6397  14370 1575  0 1575 "10" "10" 0x00000100]
	Pad[ -3838  11614  -3838  14370 1575  0 1575 "11" "11" 0x00000100]
	Pad[ -1279  11614  -1279  14370 1575  0 1575 "12" "12" 0x00000100]
	Pad[  1280  11614   1280  14370 1575  0 1575 "13" "13" 0x00000100]
	Pad[  3839  11614   3839  14370 1575  0 1575 "14" "14" 0x00000100]
	Pad[  6398  11614   6398  14370 1575  0 1575 "15" "15" 0x00000100]
	Pad[  8957  11614   8957  14370 1575  0 1575 "16" "16" 0x00000100]
	Pad[  8956 -14371   8956 -11615 1575  0 1575 "25" "25" 0x00000100]
	Pad[  6397 -14371   6397 -11615 1575  0 1575 "26" "26" 0x00000100]
	Pad[  3838 -14371   3838 -11615 1575  0 1575 "27" "27" 0x00000100]
	Pad[  1279 -14371   1279 -11615 1575  0 1575 "28" "28" 0x00000100]
	Pad[ -1280 -14371  -1280 -11615 1575  0 1575 "29" "29" 0x00000100]
	Pad[ -3839 -14371  -3839 -11615 1575  0 1575 "30" "30" 0x00000100]
	Pad[ -6398 -14371  -6398 -11615 1575  0 1575 "31" "31" 0x00000100]
	Pad[ -8957 -14371  -8957 -11615 1575  0 1575 "32" "32" 0x00000100]
	Pad[     0      0      0      0 19094 0 19094  "33" "33" 0x00000100]
	ElementLine [ 16142  16142 -16142  16142 1000]
	ElementLine [-16142  16142 -16142 -16142 1000]
	ElementLine [-16142 -16142  16142 -16142 1000]
	ElementLine [ 16142 -16142  16142  16142 1000]
)
	"""  + CRLF
        self.pcbbody = s

	# Problem solder mask is not correct
	# Problem with pin 33 which should be devided into 9 pads
	# 4.85mm is max suze which is 19094 
	# Square pad has same X1,X2 and Y1,Y2 while Thickness is the size
	#Pad[ -9540      0   9540      0 1575 0 1575 "33" "33" 0x00000100]

class LPC134XFHN33(Component):
	"LPC134XFHN33 chip class "
	def __init__(self, refid, val, name="lpc134xfhn33", libname="lpc1300", symbolname="lpc134xfhn33", packagename="HVQFN33"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = HVQFN33()
		self.parsePackage()
		self.addPin( CPin("PIO2_0/~DTR",									1	))
		self.addPin( CPin("~RESET/PIO0_0", 									2	))
		self.addPin( CPin("PIO0_1/CLKOUT/CT32B0_MAT2/USB_FTOGGLE", 						3	))
		self.addPin( CPin("XTALIN", 										4	))
		self.addPin( CPin("XTALOUT", 										5	))
		self.addPin( CPin("VDDIO", 										6	))
		self.addPin( CPin("PIO1_8/CT16B1_CAP0", 								7	))
		self.addPin( CPin("PIO0_2/SSEL/CT16B0_CAP0", 								8	))
		self.addPin( CPin("PIO0_3/USB_VBUS", 									9	))
		self.addPin( CPin("PIO0_4/SCL", 									10	))
		self.addPin( CPin("PIO0_5/SDA", 									11	))
		self.addPin( CPin("PIO1_9/CT16B1_MAT0", 								12	))
		self.addPin( CPin("USB_DM", 										13	))
		self.addPin( CPin("USB_DP", 										14	))
		self.addPin( CPin("PIO2_5",										15	))
		self.addPin( CPin("PIO0_6/~USB_CONNECT/SCK", 								16	))
		self.addPin( CPin("PIO0_8/MISO/CT16B0_MAT0",		 						17	))
		self.addPin( CPin("PIO0_9/MOSI/CT16B0_MAT1/SWO", 							18	))
		self.addPin( CPin("SWCLK/PIO0_10/SCK/CT16B0_MAT2", 							19	))
		self.addPin( CPin("PIO1_10/AD6/CT16B1_MAT1", 								20	))
		self.addPin( CPin("TDI/PIO0_11/AD0/CT32B0_MAT3", 							21	))
		self.addPin( CPin("TMS/PIO1_0/AD1/CT32B1_CAP0", 							22	))
		self.addPin( CPin("TDO/PIO1_1/AD2/CT32B1_MAT0", 							23	))
		self.addPin( CPin("~TRST/PIO1_2/AD3/CT32B1_MAT1",							24	))
		self.addPin( CPin("SWDIO/PIO1_3/AD4/CT32B1_MAT2", 							25	))
		self.addPin( CPin("PIO1_4/AD5/CT32B1_MAT3/WAKEUP", 							26	))
		self.addPin( CPin("PIO1_11/AD7",	 								27	))
		self.addPin( CPin("PIO3_2", 										28	))
		self.addPin( CPin("VDD",										29	))
		self.addPin( CPin("PIO1_5/~RTS/CT32B0_CAP0", 								30	))
		self.addPin( CPin("PIO1_6/RXD/CT32B0_MAT0", 								31	))
		self.addPin( CPin("PIO1_7/TXD/CT32B0_MAT1", 								32	))
		self.addPin( CPin("VSS", 										33	))
		
	
class LPC134X(Component):
	"LPC134X chip class "
	def __init__(self, refid, val, name="lpc134x", libname="lpc1300", symbolname="lpc134x", packagename="LQFP48"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = LQFP48()
		self.parsePackage()
		self.addPin( CPin("PIO2_6",										1	))
		self.addPin( CPin("PIO2_0/~DTR",									2	))
		self.addPin( CPin("~RESET/PIO0_0", 									3	))
		self.addPin( CPin("PIO0_1/CLKOUT/CT32B0_MAT2/USB_FTOGGLE", 						4	))
		self.addPin( CPin("VSSIO", 										5	))
		self.addPin( CPin("XTALIN", 										6	))
		self.addPin( CPin("XTALOUT", 										7	))
		self.addPin( CPin("VDDIO", 										8	))
		self.addPin( CPin("PIO1_8/CT16B1_CAP0", 								9	))
		self.addPin( CPin("PIO0_2/SSEL/CT16B0_CAP0", 								10	))
		self.addPin( CPin("PIO2_7", 										11	))
		self.addPin( CPin("PIO2_8", 										12	))
		self.addPin( CPin("PIO2_1/~DSR", 									13	))
		self.addPin( CPin("PIO0_3/USB_VBUS", 									14	))
		self.addPin( CPin("PIO0_4/SCL", 									15	))
		self.addPin( CPin("PIO0_5/SDA", 									16	))
		self.addPin( CPin("PIO1_9/CT16B1_MAT0", 								17	))
		self.addPin( CPin("PIO2_4", 										18	))
		self.addPin( CPin("USB_DM", 										19	))
		self.addPin( CPin("USB_DP", 										20	))
		self.addPin( CPin("PIO2_5",										21	))
		self.addPin( CPin("PIO0_6/~USB_CONNECT/SCK", 								22	))
		self.addPin( CPin("PIO0_7/~CTS", 									23	))
		self.addPin( CPin("PIO2_9", 										24	))
		self.addPin( CPin("PIO2_10", 										25	))
		self.addPin( CPin("PIO2_2/~DCD", 									26	))
		self.addPin( CPin("PIO0_8/MISO/CT16B0_MAT0", 								27	))
		self.addPin( CPin("PIO0_9/MOSI/CT16B0_MAT1/SWO", 							28	))
		self.addPin( CPin("SWCLK/PIO0_10/SCK/CT16B0_MAT2", 							29	))
		self.addPin( CPin("PIO1_10/AD6/CT16B1_MAT1", 								30	))
		self.addPin( CPin("PIO2_11/SCK",	 								31	))
		self.addPin( CPin("TDI/PIO0_11/AD0/CT32B0_MAT3", 							32	))
		self.addPin( CPin("TMS/PIO1_0/AD1/CT32B1_CAP0", 							33	))
		self.addPin( CPin("TDO/PIO1_1/AD2/CT32B1_MAT0", 							34	))
		self.addPin( CPin("~TRST/PIO1_2/AD3/CT32B1_MAT1",							35	))
		self.addPin( CPin("PIO3_0", 										36	))
		self.addPin( CPin("PIO3_1", 										37	))
		self.addPin( CPin("PIO2_3/~RI", 									38	))
		self.addPin( CPin("SWDIO/PIO1_3/AD4/CT32B1_MAT2", 							39	))
		self.addPin( CPin("PIO1_4/AD5/CT32B1_MAT3/WAKEUP", 							40	))
		self.addPin( CPin("VSS", 										41	))
		self.addPin( CPin("PIO1_11/AD7",	 								42	))
		self.addPin( CPin("PIO3_2", 										43	))
		self.addPin( CPin("VDD",										44	))
		self.addPin( CPin("PIO1_5/~RTS/CT32B0_CAP0", 								45	))
		self.addPin( CPin("PIO1_6/RXD/CT32B0_MAT0", 								46	))
		self.addPin( CPin("PIO1_7/TXD/CT32B0_MAT1", 								47	))
		self.addPin( CPin("PIO3_3", 										48	))	

# Some tests
if __name__ == "__main__":
	lpc1343 = LPC134X("U1","","LPC1343")
	print lpc1343


