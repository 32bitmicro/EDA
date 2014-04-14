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
		
class CGND(CDev):
	"Ground"
	def __init__(self, refid, val="?", name="gnd", libname="passive", symbolname="", packagename=""):
		CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("GND", 		1	))

class CVCC(CDev):
	"Power supply"
	def __init__(self, refid, val="?", name="vcc", libname="passive", symbolname="",packagename=""):
		CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("VCC", 		1	))

class CRes(CDev):
	"Resistor"
	def __init__(self, refid, val="?", name="resistor", libname="passive", symbolname="RESISTOR", packagename="resistor"):
		CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("1", 		1	))
		self.addPin( CPin("2", 		2	))

class CCap(CDev):
	"Capacitor"
	def __init__(self, refid, val="?", name="capacitor", libname="passive", symbolname="CAPACITOR", packagename="capacitor"):
		CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("1", 		1	))
		self.addPin( CPin("2", 		2	))

class CCappolarized(CDev):
	"Capacitor"
	def __init__(self, refid, val="?", name="polarcapacitor", libname="passive", symbolname="POLARIZED", packagename="polarcapacitor"):
		CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.addPin( CPin("-", 		1	))
		self.addPin( CPin("+", 		2	))
		
# Some tests
if __name__ == "__main__":
	r = CRes("R1","10k")
	print r
	c = CCap("C1","10n")
	print c


