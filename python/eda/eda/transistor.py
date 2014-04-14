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
		
class CPNP(CDev):
	"PNP tranistor"
	def __init__(self,refid, val, name="pnp",libname="transistor", symbolname="PNP", packagename="transistor"):
		CDev.__init__(self,refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("E", 		1	))
		self.addPin( CPin("B", 		2	))
		self.addPin( CPin("C", 		3	))

class CNPN(CDev):
	"NPN tranistor"
	def __init__(self,refid, val, name="npn",libname="transistor", symbolname="NPN", packagename="transistor"):
		CDev.__init__(self,refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("E", 		1	))
		self.addPin( CPin("B", 		2	))
		self.addPin( CPin("C", 		3	))

# Some tests
if __name__ == "__main__":
	p = CPNP("Q1","","BC307")
	print p
	n = CNPN("Q1","","BC107")
	print n


