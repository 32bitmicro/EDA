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

import re
from eda import *
# additional module for parsing
from simpleparse.common import numbers, strings, comments

CRLF = '\n'

# Coordinate system used is the same as GNU PCB
# Origin (0,0) is in the Upper Left corner
# Positive X coordinates extend right
# Negative X coordinates extend left
# Positive Y coordinates extend down
# Negative Y coordinates extend up
# Angle (Rotation) is incremented clockwise (right turn)
# All packages are defined as looking from top (top layer) 

class package(CPackage):
    def __init__(self, name="", libname="",description=""):
        CPackage.__init__(self, name, libname, description)
        self.pcbbody = ''
        self.parsed = False
        self.shape3d = ''
        self.scale3d = 1.0

# 0805 package in pcb format
pcb_package_0805= """
(
    Pad[0 -700 0 700 4500 3000 5100 "1" "1" "square"]
    Pad[8000 -700 8000 700 4500 3000 5100 "2" "2" "square"]
    ElementLine [11700 -4400 -3700 -4400 800]
    ElementLine [11700 4400 11700 -4400 800]
    ElementLine [-3700 4400 11700 4400 800]
    ElementLine [-3700 -4400 -3700 4400 800]
)
""" 

class FIDUCIAL_package(package):
    def __init__(self, mmsize, layernum, name="FIDUCIAL", libname="package",description="Fiducial"):
		package.__init__(self, name, libname,description)
		self.smt = True
		d  = mm2pcb(mmsize)
		X1 = mm2pcb(0)
		Y1 = mm2pcb(0)
		# 0 means eagle will produce filled circle
		Thickness = 0
		# copper layer 1 - top 2 - bottom but
		cir = Circle(int(X1), int(Y1),int(d),int(Thickness), int(layernum))
		self.geometry.append(cir)
		# block top aka restrict 1.5 times bigger circle
		d  = mm2pcb(mmsize*1.5)
		cir = Circle(int(X1), int(Y1),int(d),int(Thickness), int(layerBLOCKTOP))
		self.geometry.append(cir)
		# solder mask 2 times bigger circle
		d  = mm2pcb(mmsize*2.0)
		cir = Circle(int(X1), int(Y1),int(d),int(Thickness), int(layerSOLDERMASK))
		self.geometry.append(cir)
		# silk?
		#Thickness = 1000
		   
class SMT0402_package(package):
    def __init__(self, name="SMT0402_package", libname="package",description="0402 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ='(' + CRLF
        s += '    Pad[-2952 0 -2165 0 2755 2000 4755 "input" "1" "square"]' + CRLF
        s += '    Pad[2165 0 2952 0 2755 2000 4755 "input" "2" "square"]' + CRLF
        s += '    ElementLine[-5830 2877 -5830 -2877 1000]' + CRLF
        s += '    ElementLine[-5830 -2877 5830 -2877 1000]' + CRLF
        s += '    ElementLine[5830 -2877 5830 2877 1000]' + CRLF
        s += '    ElementLine[5830 2877 -5830 2877 1000]' + CRLF
        s += ')'  + CRLF
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1

class SMT0603_package(package):
    def __init__(self, name="SMT0603_package", libname="package",description="0603 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ='(' + CRLF
        s += '    Pad[-3543 0 -3149 0 3937 2000 5937 "input" "1" "square"]' + CRLF
        s += '    Pad[3149 0 3543 0 3937 2000 5937 "input" "2" "square"]' + CRLF
        s += '    ElementLine[-7011 3468 -7011 -3468 1000]' + CRLF
        s += '    ElementLine[-7011 -3468 7011 -3468 1000]' + CRLF
        s += '    ElementLine[7011 -3468 7011 3468 1000]' + CRLF
        s += '    ElementLine[7011 3468 -7011 3468 1000]' + CRLF
        s += ')'  + CRLF
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1


class SMT0805_package(package):
    def __init__(self, name="SMT0805_package", libname="package",description="0805 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-3740 -393 -3740 393 5118 2000 7118 "input" "1" 0x0100]
   Pad[3740 -393 3740 393 5118 2000 7118 "input" "2" 0x0100]
   ElementLine[-7799 4452 -7799 -4452 1000]
   ElementLine[-7799 -4452 7799 -4452 1000]
   ElementLine[7799 -4452 7799 4452 1000]
   ElementLine[7799 4452 -7799 4452 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
        
class SMT1206_package(package):
    def __init__(self, name="SMT1206_package", libname="package",description="1206 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-5511 -393 -5511 393 6299 2000 8299 "input" "1" 0x0100]
   Pad[5511 -393 5511 393 6299 2000 8299 "input" "2" 0x0100]
   ElementLine[-10161 5043 -10161 -5043 1000]
   ElementLine[-10161 -5043 10161 -5043 1000]
   ElementLine[10161 -5043 10161 5043 1000]
   ElementLine[10161 5043 -10161 5043 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
        
class SMT1210_package(package):
    def __init__(self, name="SMT1210_package", libname="package",description="1210 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-5511 -2165 -5511 2165 6299 2000 8299 "input" "1" 0x0100]
   Pad[5511 -2165 5511 2165 6299 2000 8299 "input" "2" 0x0100]
   ElementLine[-10161 6814 -10161 -6814 1000]
   ElementLine[-10161 -6814 10161 -6814 1000]
   ElementLine[10161 -6814 10161 6814 1000]
   ElementLine[10161 6814 -10161 6814 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
class SMT1812_package(package):
    def __init__(self, name="SMT1812_package", libname="package",description="1812 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-7677 -2952 -7677 2952 7480 2000 9480 "input" "1" 0x0100]
   Pad[7677 -2952 7677 2952 7480 2000 9480 "input" "2" 0x0100]
   ElementLine[-12917 8192 -12917 -8192 1000]
   ElementLine[-12917 -8192 12917 -8192 1000]
   ElementLine[12917 -8192 12917 8192 1000]
   ElementLine[12917 8192 -12917 8192 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
                

class SMT1825_package(package):
    def __init__(self, name="SMT1825_package", libname="package",description="1825 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-7677 -9645 -7677 9645 7480 2000 9480 "input" "1" 0x0100]
   Pad[7677 -9645 7677 9645 7480 2000 9480 "input" "2" 0x0100]
   ElementLine[-12917 14885 -12917 -14885 1000]
   ElementLine[-12917 -14885 12917 -14885 1000]
   ElementLine[12917 -14885 12917 14885 1000]
   ElementLine[12917 14885 -12917 14885 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1


class SMT2010_package(package):
    def __init__(self, name="SMT2010_package", libname="package",description="2010 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-8661 -1771 -8661 1771 7086 2000 9086 "input" "1" 0x0100]
   Pad[8661 -1771 8661 1771 7086 2000 9086 "input" "2" 0x0100]
   ElementLine[-13704 6814 -13704 -6814 1000]
   ElementLine[-13704 -6814 13704 -6814 1000]
   ElementLine[13704 -6814 13704 6814 1000]
   ElementLine[13704 6814 -13704 6814 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
        
class SMT2220_package(package):
    def __init__(self, name="SMT2220_package", libname="package",description="2220 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[11023 -6299 11023 6299 6299 2000 8299 "" "1" 0x0100]
   Pad[-11023 -6299 -11023 6299 6299 2000 8299 "" "2" 0x0100]
   ElementLine[-15672 10949 -15672 -10949 1000]
   ElementLine[-15672 -10949 15672 -10949 1000]
   ElementLine[15672 -10949 15672 10949 1000]
   ElementLine[15672 10949 -15672 10949 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
        
class SMT2512_package(package):
    def __init__(self, name="SMT2512_package", libname="package",description="2512 chip package"):
        package.__init__(self, name, libname,description)
        self.smt = True   
        s ="""
(
   Pad[-11023 -2755 -11023 2755 7086 2000 9086 "input" "1" 0x0100]
   Pad[11023 -2755 11023 2755 7086 2000 9086 "input" "2" 0x0100]
   ElementLine[-16066 7799 -16066 -7799 1000]
   ElementLine[-16066 -7799 16066 -7799 1000]
   ElementLine[16066 -7799 16066 7799 1000]
   ElementLine[16066 7799 -16066 7799 1000]
)
        """
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
                      
class RES0805(package):
    def __init__(self, name="RES0805", libname="package",description="0805 chip resitor"):
        package.__init__(self, name, libname,description)
        self.smt = True
        s ='(' + CRLF
        s += '    Pad[0 -700 0 700 4500 3000 5100 "1" "1" "square"]' + CRLF
        s += '    Pad[8000 -700 8000 700 4500 3000 5100 "2" "2" "square"]' + CRLF
        s += '    ElementLine [11700 -4400 -3700 -4400 800]' + CRLF
        s += '    ElementLine [11700 4400 11700 -4400 800]' + CRLF
        s += '    ElementLine [-3700 4400 11700 4400 800]' + CRLF
        s += '    ElementLine [-3700 -4400 -3700 4400 800]' + CRLF
        s += ')'  + CRLF
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1

class CAP0805(package):
    def __init__(self, name="CAP0805", libname="package",description="0805 chip capacitor"):
        package.__init__(self, name, libname,description)
        self.smt = True        
        s = '(' + CRLF
        s += '    Pad[0 -700 0 700 4500 3000 5100 "1" "1" "square"]' + CRLF
        s += '    Pad[8000 -700 8000 700 4500 3000 5100 "2" "2" "square"]' + CRLF
        s += '    ElementLine [11700 -4400 -3700 -4400 800]' + CRLF
        s += '    ElementLine [11700 4400 11700 -4400 800]' + CRLF
        s += '    ElementLine [-3700 4400 11700 4400 800]' + CRLF
        s += '    ElementLine [-3700 -4400 -3700 4400 800]'  + CRLF
        s += ')'  + CRLF
        self.pcbbody = s
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
class LED0805(package):
    def __init__(self, name="LED0805", libname="package",description="0805 led"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = pcb_package_0805
        self.shape3d = "smd/chip_cms.wrl"
        self.scale3d = 0.1
        
class DIODE0805(package):
    def __init__(self, name="DIODE0805", libname="package",description="0805 diode"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = pcb_package_0805
        #self.shape3d = "smd/chip_cms.wrl"
        #self.scale3d = 0.1
        
class SOT23(package):
    def __init__(self, name="SOT23", libname="package",description="SMT 3 pin SOT-23 package"):
        package.__init__(self, name, libname,description)
        self.smt = True       
        s = '(' + CRLF
        s += '    Pad[0 -300 0 300 3400 3000 4000 "1" "1" "square,edge2"]' + CRLF
        s += '    Pad[7800 -300 7800 300 3400 3000 4000 "2" "2" "square,edge2"]' + CRLF
        s += '    Pad[3900 -8500 3900 -7900 3400 3000 4000 "3" "3" "square"] ' + CRLF
        s += '    ElementLine [10300 -11000 -2500 -11000 1000]' + CRLF
        s += '    ElementLine [10300 2900 10300 -11000 1000]' + CRLF
        s += '    ElementLine [-2500 2900 10300 2900 1000]' + CRLF
        s += '    ElementLine [-2500 -11000 -2500 2900 1000]' + CRLF
        s += ')'  + CRLF
        self.pcbbody = s
        
    
class SOT223(package):
    def __init__(self, name="SOT223", libname="package",description="SMT 4 pin SOT-223 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[0 -3300 0 3300 5600 3000 6200 "1" "1" "square,edge2"]
    Pad[9000 -3300 9000 3300 5600 3000 6200 "2" "2" "square,edge2"]
    Pad[18100 -3300 18100 3300 5600 3000 6200 "3" "3" "square,edge2"]
    Pad[4500 -24400 13500 -24400 12200 3000 12800 "4" "4" "square"]
    ElementLine [-5200 -32900 -5200 8500 1000]
    ElementLine [-5200 8500 23300 8500 1000]
    ElementLine [23300 8500 23300 -32900 1000]
    ElementLine [23300 -32900 -5200 -32900 1000]
    )
        '''
            
class EIA7343(package):
    def __init__(self, name="EIA7343", libname="package",description="SMT Tantalum capacitor : pin 1 +, pin 2 -"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-11500 -5600 -11500 5600 12300 2000 12900 "1" "1" "square"]
    Pad[11500 -5600 11500 5600 12300 2000 12900 "2" "2" "square"]
    ElementLine [-21900 -11700 -21900 11700 2000]
    ElementLine [-21900 11700 -15800 15000 1000]
    ElementLine [-15800 15000 20900 15000 1000]
    ElementLine [20900 15000 20900 -15000 1000]
    ElementLine [20900 -15000 -15800 -15000 1000]
    ElementLine [-15800 -15000 -21900 -11700 1000]
)        
        '''
        
class SO8(package):
    def __init__(self, name="SO8", libname="package",description="SO8 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[-7500 7000 -7500 13500 2787 1600 3787 "" "1" "square,edge2"]
    Pad[-2500 7000 -2500 13500 2787 1600 3787 "" "2" "square,edge2"]
    Pad[2500 7000 2500 13500 2787 1600 3787 "" "3" "square,edge2"]
    Pad[7500 7000 7500 13500 2787 1600 3787 "" "4" "square,edge2"]
    Pad[7500 -13500 7500 -7000 2787 1600 3787 "" "5" "square"]
    Pad[2500 -13500 2500 -7000 2787 1600 3787 "" "6" "square"]
    Pad[-2500 -13500 -2500 -7000 2787 1600 3787 "" "7" "square"]
    Pad[-7500 -13500 -7500 -7000 2787 1600 3787 "" "8" "square"]
    ElementLine [-10236 16142 10237 16142 1000]
    ElementLine [10237 -16142 10237 16142 1000]
    ElementLine [-10236 -16142 10237 -16142 1000]
    ElementLine [-10340 -16039 -10340 -2645 1000]
    ElementLine [-10236 2756 -10236 16142 1000]
    ElementArc [-10288 0 2500 2500 90 180 1000]
)        
        '''
        self.shape3d = "smd/cms_so8.wrl"

# Rotated 90 degree
class SOIC8(package):
    def __init__(self, name="SOIC8", libname="package",description="SOIC8 package SOIC-127P-600L1-8N"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
   Pad[-12600 -7500 -6300 -7500 2400 2000 4400 "" "1" 0x0100]
   Pad[-12600 -2500 -6300 -2500 2400 2000 4400 "" "2" 0x0100]
   Pad[-12600 2500 -6300 2500 2400 2000 4400 "" "3" 0x0100]
   Pad[-12600 7500 -6300 7500 2400 2000 4400 "" "4" 0x0100]
   Pad[6300 7500 12600 7500 2400 2000 4400 "" "5" 0x0100]
   Pad[6300 2500 12600 2500 2400 2000 4400 "" "6" 0x0100]
   Pad[6300 -2500 12600 -2500 2400 2000 4400 "" "7" 0x0100]
   Pad[6300 -7500 12600 -7500 2400 2000 4400 "" "8" 0x0100]
   ElementLine[-3100 -2200 -3100 -6250 1000]
   ElementLine[-3100 -6250 500 -9850 1000]
   ElementLine[500 -9850 3100 -9850 1000]
   ElementLine[3100 -9850 3100 -2200 1000]
   ElementLine[-3100 2200 -3100 9850 1000]
   ElementLine[-3100 9850 3100 9850 1000]
   ElementLine[3100 9850 3100 2200 1000]
)
        '''
        
class TSSOP16(package):
    def __init__(self, name="TSSOP16", libname="package",description="TSSOP16 package"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[8858 1182 12598 1182 1400 3000 4400 "12" "12" "edge2"]
    Pad[8858 3741 12598 3741 1400 3000 4400 "11" "11" "edge2"]
    Pad[8858 6300 12598 6300 1400 3000 4400 "10" "10" "edge2"]
    Pad[8858 8859 12598 8859 1400 3000 4400 "9" "9" "edge2"]
    Pad[-14567 -9054 -10827 -9054 1400 3000 4400 "1" "1" ""]
    Pad[-14567 -6495 -10827 -6495 1400 3000 4400 "1" "2" ""]
    Pad[8858 -1377 12598 -1377 1400 3000 4400 "13" "13" "edge2"]
    Pad[8858 -3936 12598 -3936 1400 3000 4400 "14" "14" "edge2"]
    Pad[8858 -6495 12598 -6495 1400 3000 4400 "15" "15" "edge2"]
    Pad[8858 -9054 12598 -9054 1400 3000 4400 "16" "16" "edge2"]
    Pad[-14567 1182 -10827 1182 1400 3000 4400 "5" "5" ""]
    Pad[-14567 3741 -10827 3741 1400 3000 4400 "6" "6" ""]
    Pad[-14567 6300 -10827 6300 1400 3000 4400 "7" "7" ""]
    Pad[-14567 8859 -10827 8859 1400 3000 4400 "8" "8" ""]
    Pad[-14567 -3936 -10827 -3936 1400 3000 4400 "3" "3" ""]
    Pad[-14567 -1377 -10827 -1377 1400 3000 4400 "4" "4" ""]
    ElementLine [-16142 10827 -16142 -11023 1000]
    ElementLine [14370 -11023 1378 -11023 1000]
    ElementLine [14371 -11023 14370 10827 1000]
    ElementLine [-1378 -11023 -16142 -11023 1000]
    ElementLine [14370 10827 -16142 10827 1000]
    ElementArc [-78 -11023 1300 1300 0 180 1000]
)        
        '''
               
class HCU49(package):
    def __init__(self, name="HCU49", libname="package",description="XTAL HCU49"):
        package.__init__(self, name, libname,description)
        self.pcbbody = '''
(
    Pin[158 189 6000 2000 6600 2800 "" "1" 0x00004101]
    Pin[20158 189 6000 2000 6600 2800 "" "2" 0x00004001]
    ElementLine [22521 -8355 -2669 -8355 1000]
    ElementLine [30708 -787 30708 787 1000]
    ElementLine [-2597 8732 22521 8732 1000]
    ElementLine [-10630 -787 -10630 787 1000]
    ElementArc [22675 -322 8033 8033 180 90 1000]
    ElementArc [-2362 393 8268 8268 0 90 1000]
    ElementArc [-2597 -322 8033 8033 270 90 1000]
    ElementArc [22440 393 8268 8268 90 90 1000]

    )        
        '''
                       
class HEADER10X2_package(package):
    def __init__(self, name="HEADER20X2", libname="package",description="Header 0.100 x 2 x n"):
        package.__init__(self, name, libname,description)
        self.pcbbody = '''
(
    Pin[0 0 7574 3000 8174 4000 "" "1" "square,edge2"]
    Pin[0 -10000 7574 3000 8174 4000 "" "2" "edge2"]
    Pin[10000 0 7574 3000 8174 4000 "" "3" "edge2"]
    Pin[10000 -10000 7574 3000 8174 4000 "" "4" "edge2"]
    Pin[20000 0 7574 3000 8174 4000 "" "5" "edge2"]
    Pin[20000 -10000 7574 3000 8174 4000 "" "6" "edge2"]
    Pin[30000 0 7574 3000 8174 4000 "" "7" "edge2"]
    Pin[30000 -10000 7574 3000 8174 4000 "" "8" "edge2"]
    Pin[40000 0 7574 3000 8174 4000 "" "9" "edge2"]
    Pin[40000 -10000 7574 3000 8174 4000 "" "10" "edge2"]
    Pin[50000 0 7574 3000 8174 4000 "" "11" "edge2"]
    Pin[50000 -10000 7574 3000 8174 4000 "" "12" "edge2"]
    Pin[60000 0 7574 3000 8174 4000 "" "13" "edge2"]
    Pin[60000 -10000 7574 3000 8174 4000 "" "14" "edge2"]
    Pin[70000 0 7574 3000 8174 4000 "" "15" "edge2"]
    Pin[70000 -10000 7574 3000 8174 4000 "" "16" "edge2"]
    Pin[80000 0 7574 3000 8174 4000 "" "17" "edge2"]
    Pin[80000 -10000 7574 3000 8174 4000 "" "18" "edge2"]
    Pin[90000 0 7574 3000 8174 4000 "" "19" "edge2"]
    Pin[90000 -10000 7574 3000 8174 4000 "" "20" "edge2"]
    ElementLine [-5000 -5000 5000 -5000 1000]
    ElementLine [96000 -15000 96000 5000 2000]
    ElementLine [-5000 -15000 96000 -15000 2000]
    ElementLine [-5000 -15000 -5000 5000 2000]
    ElementLine [5000 -5000 5000 5000 1000]
    ElementLine [-5000 5000 96000 5000 2000]
    )
        '''
   
class HEADER_package(package):
	#  Good thicknes is 64 mill and drill 36 mill, will press fit
    def __init__(self, M , N, name="HEADER", libname="package",description="Header 0.100 x n x m", dx = 10000, dy = 10000,shape="",Thickness=6400,Drill=3600 ):
		
        package.__init__(self, name, libname,description)
        # generate header M by N
        x = 0
        y = 0
        
        SFlags1  = '"square,edge2"'
        SFlags   = '"edge2"'
        #  Good thicknes is 64 mill and drill 36 mill, will press fit
        #Thickness = 6400 #7574
        Clearance = 3000
        Mask = 8174
        #Drill = 3600 #4000
        num = 1
        for mi in range(M):
            for ni in range(N):
                rX = x + dx * mi
                rY = y - dy * ni
                pin = CPin(str(num),num,int(rX),int(rY))
                pin.smt         = False
                pin.num         = int(num)
                pin.thickness   = int(Thickness)
                pin.clearance   = int(Clearance)
                pin.mask        = int(Mask)
                pin.drill       = int(Drill)
                pin.name        = '"' + str(num) + '"'
                pin.shape       = shape
                if mi==0 and ni == 0:
                # pcb attributes
                    pin.sflags       = SFlags1
                    sizex = Thickness
                    sizey = Thickness
                    pin.pad = CPad(sizex, sizey, "S", pin.drill)
                else:
                    pin.sflags       = SFlags
                    # make pad
                    sizex = Thickness
                    sizey = Thickness
                    pin.pad = CPad(sizex, sizey, "R", pin.drill )
                # make bbox covering pin with clearance, will be used for blockages    
                size = pin.thickness + pin.clearance
                x1 = int(pin.pos._x - size / 2)
                x2 = int(pin.pos._x + size / 2)
                y1 = int(pin.pos._y - size / 2)
                y2 = int(pin.pos._y + size / 2)
                pin.bbox = Rectangle(x1,y1,x2,y2,0)   
                self.pins[pin.num]=pin
                num = num  + 1
                
        X1 = x - 5000
        Y1 = y + 5000
        X2 = x + dx * (M - 1) + 5000
        Y2 = y - dy * (N - 0) + 5000
        Thickness = 1000
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        self.pcbbody = ''


# Nx2 only!!!
class HEADER_SMT_package(package):
    def __init__(self, M , N, name="HEADERSMT", libname="package",description="Header 0.100 x n x m", dx = 10000, dy = 10000):
        package.__init__(self, name, libname,description)
        self.smt = True
        if N != 2:
			print "unsupported smt pin header configuration M=" + str(M) + " N = " + str(N)
        # generate header M by N
        x = 0
        y = 0
        dx = mil2pcb(100)
        dy = mil2pcb(145 + 50)
        padsizex = mil2pcb(50)
        padsizey = mil2pcb(145)
        num = 1
        for mi in range(M):
            for ni in range(N):
                rX = x + dx * mi
                rY = y - dy * ni
                pin = CPin('"'+str(num)+'"',num,int(rX),int(rY))
                pin.pad = CPad(padsizex, padsizey, "S")
                pin.set_pin_pad_from_size(padsizex, padsizey)
                self.pins[pin.num]=pin
                num = num  + 1
                
        X1 = x - 5000
        Y1 = y + 5000
        X2 = x + dx * (M - 1) + 5000
        Y2 = y - dy * (N - 0) + 5000
        Thickness = 1000
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
#        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
#        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
#        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
#        self.geometry.append(line)
        self.pcbbody = ''

class DIP_package(package):
    def __init__(self, M , name="DIP", libname="package",description="DIP 0.100 x n x m", dx = 10000, dy = 10000):
        package.__init__(self, name, libname,description)
        # generate DIP M by N
        x = 0
        y = 0
        
        SFlags1  = '"square,edge2"'
        SFlags   = '"edge2"'
        #  Good thicknes is 64 mill and drill 36 mill, will press fit
        Thickness = 6400 #7574
        Clearance = 3000
        Mask = 8174
        Drill = 3600 #4000
        num = 1
        # pins defined in a circle
        for mi in range(M):
            if mi < M/2:
                rX = x + dx * mi
                rY = y
            else:
                rX = x - dx * ( mi - M/2 ) + dx * ( M/2 - 1 )
                rY = y - dy
                
            pin = CPin(str(num),num,int(rX),int(rY))
            pin.smt         = False
            pin.num         = int(num)
            pin.thickness   = int(Thickness)
            pin.clearance   = int(Clearance)
            pin.mask        = int(Mask)
            pin.drill       = int(Drill)
            pin.name        = '"' + str(num) + '"'
            if mi==0 :
            # pcb attributes
                pin.sflags       = SFlags1
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "S", pin.drill)
            else:
                pin.sflags       = SFlags
                # make pad
                sizex = Thickness
                sizey = Thickness
                pin.pad = CPad(sizex, sizey, "R", pin.drill )
            # make bbox covering pin with clearance, will be used for blockages    
            size = pin.thickness + pin.clearance
            x1 = int(pin.pos._x - size / 2)
            x2 = int(pin.pos._x + size / 2)
            y1 = int(pin.pos._y - size / 2)
            y2 = int(pin.pos._y + size / 2)
            pin.bbox = Rectangle(x1,y1,x2,y2,0)   
            self.pins[pin.num]=pin
            num = num  + 1
                
        X1 = x - 5000
        Y1 = y + 5000
        X2 = x + dx * (M - 1) + 5000
        Y2 = y + dy * (2 - 1) + 5000
        Thickness = 1000
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        self.pcbbody = ''


class HC08201_package(HEADER_package):
    def __init__(self, name="HC08201", libname="package",description="HC08201"):
        HEADER_package.__init__(self, 7, 2, name, libname,description)
        # Add outline
        x = -487 * 100
        y = -174 * 100
        
        # Main outline 40mm (1578) x 29.8 (1173)
        X1 = x
        Y1 = y
        X2 = X1 + 1578 * 100
        Y2 = Y1 + 1173 * 100
        Thickness = 1000
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        
        # Internal outline 30mm (1181) x 14 (551) offset 5 (196) mm and 11.3 (444)
        X1 = x + 196 * 100
        Y1 = y + 444 * 100
        X2 = X1 + 1181 * 100
        Y2 = Y1 + 551 * 100
        Thickness = 1000
        line = Line([Point(int(X1),int(Y1)),Point(int(X1),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y1))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1),int(Y2)),Point(int(X2),int(Y2))], int(Thickness))
        self.geometry.append(line)
        
        # ears
        d4mm = 157 * 100
        d2mm = d4mm / 2
        d1mm = d4mm / 4
        X1 = x
        Y1 = y
        X2 = x + 1578 * 100
        Y2 = y + 1173 * 100
        # left 
        line = Line([Point(int(X1),int(Y2)),Point(int(X1),int(Y2+d4mm))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X1+d4mm),int(Y2)),Point(int(X1+d4mm),int(Y2+d4mm))], int(Thickness))
        self.geometry.append(line)
        arc = Arc(X1+d2mm, Y2+d4mm, d2mm, d2mm, 0, 180, int(Thickness))
        self.geometry.append(arc)
        # right
        line = Line([Point(int(X2),int(Y2)),Point(int(X2),int(Y2+d4mm))], int(Thickness))
        self.geometry.append(line)
        line = Line([Point(int(X2-d4mm),int(Y2)),Point(int(X2-d4mm),int(Y2+d4mm))], int(Thickness))
        self.geometry.append(line)
        arc = Arc(X2-d2mm, Y2+d4mm, d2mm, d2mm, 0, 180, int(Thickness))
        self.geometry.append(arc)
        
        # holes
        Diameter = 78 /2  * 100 # 2mm
        off30_5mm = 1200 * 100
        off3_4mm = d1mm * 3.4
        off2mm = d1mm * 2
        dx = 78 * 100
        X1 = x + off2mm
        Y1 = y + off3_4mm
        X2 = x + 1578 * 100 - off2mm
        Y2 = y + 1173 * 100 - off3_4mm
        # Bottom
        arc = Arc(X1, Y1, Diameter, Diameter, 0, 360, int(Thickness))
        self.geometry.append(arc)
        arc = Arc(X2, Y1, Diameter, Diameter, 0, 360, int(Thickness))
        self.geometry.append(arc)
        # Top
        arc = Arc(X1, Y1+off30_5mm, d1mm, d1mm, 0, 360, int(Thickness))
        self.geometry.append(arc)
        arc = Arc(X2, Y1+off30_5mm, d1mm, d1mm, 0, 360, int(Thickness))
        self.geometry.append(arc)
        #
        # empty body
        self.pcbbody = ''
        
        
        
        
        
        
class DSUB9F_package(package):
    def __init__(self, name="DSUB9F", libname="package",description="Connector DSUB 9F AMP 747844"):
        package.__init__(self, name, libname,description)
        self.pcbbody = '''
(
   Pin[-21600 18200 7200 2000 9200 5200 "" "1" 0x0101]
   Pin[-10800 18200 7200 2000 9200 5200 "" "2" 0x01]
   Pin[0 18200 7200 2000 9200 5200 "" "3" 0x01]
   Pin[10800 18200 7200 2000 9200 5200 "" "4" 0x01]
   Pin[21600 18200 7200 2000 9200 5200 "" "5" 0x01]
   Pin[-16200 7000 7200 2000 9200 5200 "" "6" 0x01]
   Pin[-5400 7000 7200 2000 9200 5200 "" "7" 0x01]
   Pin[5400 7000 7200 2000 9200 5200 "" "8" 0x01]
   Pin[16200 7000 7200 2000 9200 5200 "" "9" 0x01]
   ElementLine[-21600 -14850 -21600 0 2000]
   ElementLine[-16200 -14850 -16200 0 2000]
   ElementLine[-10800 -14850 -10800 0 2000]
   ElementLine[-5400 -14850 -5400 0 2000]
   ElementLine[0 -14850 0 0 2000]
   ElementLine[5400 -14850 5400 0 2000]
   ElementLine[10800 -14850 10800 0 2000]
   ElementLine[16200 -14850 16200 0 2000]
   ElementLine[21600 -14850 21600 0 2000]
   Pin[-49200 12600 19500 2000 21500 12500 "" "10" 0x01]
   ElementLine[-55450 -24850 -55450 -19850 1000]
   ElementLine[-42950 -24850 -42950 -19850 1000]
   Pin[49200 12600 19500 2000 21500 12500 "" "11" 0x01]
   ElementLine[42950 -24850 42950 -19850 1000]
   ElementLine[55450 -24850 55450 -19850 1000]
   ElementLine[-31600 -19350 -31600 -14850 2000]
   ElementLine[-31600 -14850 31600 -14850 2000]
   ElementLine[31600 -14850 31600 -19350 2000]
   ElementLine[-60650 24850 -60650 -24850 1000]
   ElementLine[-60650 -24850 60650 -24850 1000]
   ElementLine[60650 -24850 60650 24850 1000]
   ElementLine[60650 24850 -60650 24850 1000]
   ElementLine[-60650 -19850 60650 -19850 1000]
)        
        '''

class USBA_package(package):
    def __init__(self, name="USBA", libname="package",description="Connector USB A"):
        package.__init__(self, name, libname,description)
        self.pcbbody = '''
(
    Pin[13200 -25900 11500 2000 11500 9100 "5" "5" ""]
    Pin[13200 25800 11500 2000 11500 9100 "6" "6" ""]
    Pin[23900 -4100 6500 2000 6500 3600 "2" "2" ""]
    Pin[23900 3900 6500 2000 6500 3600 "3" "3" ""]
    Pin[23900 -13900 6500 2000 6500 3600 "1" "1" "square"]
    Pin[23900 13700 6500 2000 6500 3600 "4" "4" ""]
    ElementLine [19700 -25900 27800 -25900 1000]
    ElementLine [-23300 25800 6700 25800 1000]
    ElementLine [19600 25800 27800 25800 1000]
    ElementLine [-23300 -25900 -23300 25800 1000]
    ElementLine [-23300 -25900 6500 -25900 1000]
    ElementLine [27800 -25900 27800 25800 1000]
    )        
        '''
           
class USBB_package(package):
    def __init__(self, name="USBB", libname="package",description="Connector USB B"):
        package.__init__(self, name, libname,description)
        self.pcbbody = '''
(
    Pin[51200 -18800 7000 2000 9000 3500 "4" "4" "edge2"]
    Pin[51200 -28600 7000 2000 9000 3500 "3" "3" "edge2"]
    Pin[59000 -28600 7000 2000 9000 3500 "2" "2" "edge2"]
    Pin[59000 -18800 7000 2000 9000 3500 "1" "1" "square,edge2"]
    Pin[40500 0 12000 2000 13000 10000 "5" "5" "edge2"]
    Pin[40500 -47400 12000 2000 13000 10000 "6" "6" "edge2"]
    ElementLine [0 0 34500 0 1000]
    ElementLine [0 -47400 0 0 1000]
    ElementLine [0 -47400 34500 -47400 1000]
    ElementLine [46500 0 64000 0 1000]
    ElementLine [64000 -47400 64000 0 1000]
    ElementLine [46500 -47400 64000 -47400 1000]
    ElementArc [40500 0 6000 6000 90 360 1000]
    ElementArc [40500 -47400 6000 6000 90 360 1000]
    )      
        '''
                             
class LQFP32(package):
    def __init__(self, name="LQFP32", libname="package",description="Square Quad-side flat pack"):
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
        
class LQFP48(package):
    def __init__(self, name="LQFP48", libname="package",description="Square Quad-side flat pack"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[2900 1000 2900 4500 1100 3000 1700 "1" "1" "edge2"]
    Pad[4800 1000 4800 4500 1100 3000 1700 "2" "2" "square,edge2"]
    Pad[6800 1000 6800 4500 1100 3000 1700 "3" "3" "square,edge2"]
    Pad[8800 1000 8800 4500 1100 3000 1700 "4" "4" "square,edge2"]
    Pad[10700 1000 10700 4500 1100 3000 1700 "5" "5" "square,edge2"]
    Pad[12700 1000 12700 4500 1100 3000 1700 "6" "6" "square,edge2"]
    Pad[14700 1000 14700 4500 1100 3000 1700 "7" "7" "square,edge2"]
    Pad[16600 1000 16600 4500 1100 3000 1700 "8" "8" "square,edge2"]
    Pad[18600 1000 18600 4500 1100 3000 1700 "9" "9" "square,edge2"]
    Pad[20600 1000 20600 4500 1100 3000 1700 "10" "10" "square,edge2"]
    Pad[22500 1000 22500 4500 1100 3000 1700 "11" "11" "square,edge2"]
    Pad[24500 1000 24500 4500 1100 3000 1700 "12" "12" "square,edge2"]
    Pad[28500 -2900 32000 -2900 1100 3000 1700 "13" "13" "square,edge2"]
    Pad[28500 -4800 32000 -4800 1100 3000 1700 "14" "14" "square,edge2"]
    Pad[28500 -6800 32000 -6800 1100 3000 1700 "15" "15" "square,edge2"]
    Pad[28500 -8800 32000 -8800 1100 3000 1700 "16" "16" "square,edge2"]
    Pad[28500 -10700 32000 -10700 1100 3000 1700 "17" "17" "square,edge2"]
    Pad[28500 -12700 32000 -12700 1100 3000 1700 "18" "18" "square,edge2"]
    Pad[28500 -14700 32000 -14700 1100 3000 1700 "19" "19" "square,edge2"]
    Pad[28500 -16600 32000 -16600 1100 3000 1700 "20" "20" "square,edge2"]
    Pad[28500 -18600 32000 -18600 1100 3000 1700 "21" "21" "square,edge2"]
    Pad[28500 -20600 32000 -20600 1100 3000 1700 "22" "22" "square,edge2"]
    Pad[28500 -22500 32000 -22500 1100 3000 1700 "23" "23" "square,edge2"]
    Pad[28500 -24500 32000 -24500 1100 3000 1700 "24" "24" "square,edge2"]
    Pad[24600 -32000 24600 -28500 1100 3000 1700 "25" "25" "square"]
    Pad[22700 -32000 22700 -28500 1100 3000 1700 "26" "26" "square"]
    Pad[20700 -32000 20700 -28500 1100 3000 1700 "27" "27" "square"]
    Pad[18700 -32000 18700 -28500 1100 3000 1700 "28" "28" "square"]
    Pad[16800 -32000 16800 -28500 1100 3000 1700 "29" "29" "square"]
    Pad[14800 -32000 14800 -28500 1100 3000 1700 "30" "30" "square"]
    Pad[12800 -32000 12800 -28500 1100 3000 1700 "31" "31" "square"]
    Pad[10900 -32000 10900 -28500 1100 3000 1700 "32" "32" "square"]
    Pad[8900 -32000 8900 -28500 1100 3000 1700 "33" "33" "square"]
    Pad[6900 -32000 6900 -28500 1100 3000 1700 "34" "34" "square"]
    Pad[5000 -32000 5000 -28500 1100 3000 1700 "35" "35" "square"]
    Pad[3000 -32000 3000 -28500 1100 3000 1700 "36" "36" "square"]
    Pad[-4500 -24600 -1000 -24600 1100 3000 1700 "37" "37" "square"]
    Pad[-4500 -22700 -1000 -22700 1100 3000 1700 "38" "38" "square"]
    Pad[-4500 -20700 -1000 -20700 1100 3000 1700 "39" "39" "square"]
    Pad[-4500 -18700 -1000 -18700 1100 3000 1700 "40" "40" "square"]
    Pad[-4500 -16800 -1000 -16800 1100 3000 1700 "41" "41" "square"]
    Pad[-4500 -14800 -1000 -14800 1100 3000 1700 "42" "42" "square"]
    Pad[-4500 -12800 -1000 -12800 1100 3000 1700 "43" "43" "square"]
    Pad[-4500 -10900 -1000 -10900 1100 3000 1700 "44" "44" "square"]
    Pad[-4500 -8900 -1000 -8900 1100 3000 1700 "45" "45" "square"]
    Pad[-4500 -6900 -1000 -6900 1100 3000 1700 "46" "46" "square"]
    Pad[-4500 -5000 -1000 -5000 1100 3000 1700 "47" "47" "square"]
    Pad[-4500 -3000 -1000 -3000 1100 3000 1700 "48" "48" "square"]
    ElementLine [0 -27500 0 -2800 1000]
    ElementLine [0 -27500 27500 -27500 1000]
    ElementLine [27500 -27500 27500 0 1000]
    ElementLine [2800 0 27500 0 1000]
    ElementLine [2800 0 0 -2800 1000]
    ElementArc [3500 -3500 1000 1000 90 360 1000]
)
        '''
        
class LQFP64(package):
    def __init__(self, name="LQFP64", libname="package",description="Square Quad-side flat pack"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[1000 -4900 4500 -4900 1100 3000 1700 "1" "1" "edge2"]
    Pad[1000 -6800 4500 -6800 1100 3000 1700 "2" "2" "square,edge2"]
    Pad[1000 -8800 4500 -8800 1100 3000 1700 "3" "3" "square,edge2"]
    Pad[1000 -10800 4500 -10800 1100 3000 1700 "4" "4" "square,edge2"]
    Pad[1000 -12700 4500 -12700 1100 3000 1700 "5" "5" "square,edge2"]
    Pad[1000 -14700 4500 -14700 1100 3000 1700 "6" "6" "square,edge2"]
    Pad[1000 -16700 4500 -16700 1100 3000 1700 "7" "7" "square,edge2"]
    Pad[1000 -18600 4500 -18600 1100 3000 1700 "8" "8" "square,edge2"]
    Pad[1000 -20600 4500 -20600 1100 3000 1700 "9" "9" "square,edge2"]
    Pad[1000 -22600 4500 -22600 1100 3000 1700 "10" "10" "square,edge2"]
    Pad[1000 -24500 4500 -24500 1100 3000 1700 "11" "11" "square,edge2"]
    Pad[1000 -26500 4500 -26500 1100 3000 1700 "12" "12" "square,edge2"]
    Pad[1000 -28500 4500 -28500 1100 3000 1700 "13" "13" "square,edge2"]
    Pad[1000 -30400 4500 -30400 1100 3000 1700 "14" "14" "square,edge2"]
    Pad[1000 -32400 4500 -32400 1100 3000 1700 "15" "15" "square,edge2"]
    Pad[1000 -34400 4500 -34400 1100 3000 1700 "16" "16" "square,edge2"]
    Pad[-4900 -43800 -4900 -40300 1100 3000 1700 "17" "17" "square"]
    Pad[-6800 -43800 -6800 -40300 1100 3000 1700 "18" "18" "square"]
    Pad[-8800 -43800 -8800 -40300 1100 3000 1700 "19" "19" "square"]
    Pad[-10800 -43800 -10800 -40300 1100 3000 1700 "20" "20" "square"]
    Pad[-12700 -43800 -12700 -40300 1100 3000 1700 "21" "21" "square"]
    Pad[-14700 -43800 -14700 -40300 1100 3000 1700 "22" "22" "square"]
    Pad[-16700 -43800 -16700 -40300 1100 3000 1700 "23" "23" "square"]
    Pad[-18600 -43800 -18600 -40300 1100 3000 1700 "24" "24" "square"]
    Pad[-20600 -43800 -20600 -40300 1100 3000 1700 "25" "25" "square"]
    Pad[-22600 -43800 -22600 -40300 1100 3000 1700 "26" "26" "square"]
    Pad[-24500 -43800 -24500 -40300 1100 3000 1700 "27" "27" "square"]
    Pad[-26500 -43800 -26500 -40300 1100 3000 1700 "28" "28" "square"]
    Pad[-28500 -43800 -28500 -40300 1100 3000 1700 "29" "29" "square"]
    Pad[-30400 -43800 -30400 -40300 1100 3000 1700 "30" "30" "square"]
    Pad[-32400 -43800 -32400 -40300 1100 3000 1700 "31" "31" "square"]
    Pad[-34400 -43800 -34400 -40300 1100 3000 1700 "32" "32" "square"]
    Pad[-43800 -34400 -40300 -34400 1100 3000 1700 "33" "33" "square"]
    Pad[-43800 -32500 -40300 -32500 1100 3000 1700 "34" "34" "square"]
    Pad[-43800 -30500 -40300 -30500 1100 3000 1700 "35" "35" "square"]
    Pad[-43800 -28500 -40300 -28500 1100 3000 1700 "36" "36" "square"]
    Pad[-43800 -26600 -40300 -26600 1100 3000 1700 "37" "37" "square"]
    Pad[-43800 -24600 -40300 -24600 1100 3000 1700 "38" "38" "square"]
    Pad[-43800 -22600 -40300 -22600 1100 3000 1700 "39" "39" "square"]
    Pad[-43800 -20700 -40300 -20700 1100 3000 1700 "40" "40" "square"]
    Pad[-43800 -18700 -40300 -18700 1100 3000 1700 "41" "41" "square"]
    Pad[-43800 -16700 -40300 -16700 1100 3000 1700 "42" "42" "square"]
    Pad[-43800 -14800 -40300 -14800 1100 3000 1700 "43" "43" "square"]
    Pad[-43800 -12800 -40300 -12800 1100 3000 1700 "44" "44" "square"]
    Pad[-43800 -10800 -40300 -10800 1100 3000 1700 "45" "45" "square"]
    Pad[-43800 -8900 -40300 -8900 1100 3000 1700 "46" "46" "square"]
    Pad[-43800 -6900 -40300 -6900 1100 3000 1700 "47" "47" "square"]
    Pad[-43800 -4900 -40300 -4900 1100 3000 1700 "48" "48" "square"]
    Pad[-34400 1000 -34400 4500 1100 3000 1700 "49" "49" "square,edge2"]
    Pad[-32500 1000 -32500 4500 1100 3000 1700 "50" "50" "square,edge2"]
    Pad[-30500 1000 -30500 4500 1100 3000 1700 "51" "51" "square,edge2"]
    Pad[-28500 1000 -28500 4500 1100 3000 1700 "52" "52" "square,edge2"]
    Pad[-26600 1000 -26600 4500 1100 3000 1700 "53" "53" "square,edge2"]
    Pad[-24600 1000 -24600 4500 1100 3000 1700 "54" "54" "square,edge2"]
    Pad[-22600 1000 -22600 4500 1100 3000 1700 "55" "55" "square,edge2"]
    Pad[-20700 1000 -20700 4500 1100 3000 1700 "56" "56" "square,edge2"]
    Pad[-18700 1000 -18700 4500 1100 3000 1700 "57" "57" "square,edge2"]
    Pad[-16700 1000 -16700 4500 1100 3000 1700 "58" "58" "square,edge2"]
    Pad[-14800 1000 -14800 4500 1100 3000 1700 "59" "59" "square,edge2"]
    Pad[-12800 1000 -12800 4500 1100 3000 1700 "60" "60" "square,edge2"]
    Pad[-10800 1000 -10800 4500 1100 3000 1700 "61" "61" "square,edge2"]
    Pad[-8900 1000 -8900 4500 1100 3000 1700 "62" "62" "square,edge2"]
    Pad[-6900 1000 -6900 4500 1100 3000 1700 "63" "63" "square,edge2"]
    Pad[-4900 1000 -4900 4500 1100 3000 1700 "64" "64" "square,edge2"]
    ElementLine [0 -2800 -2800 0 1000]
    ElementLine [0 -39300 0 -2800 1000]
    ElementLine [-39300 -39300 0 -39300 1000]
    ElementLine [-39300 -39300 -39300 0 1000]
    ElementLine [-39300 0 -2800 0 1000]
    ElementArc [-3500 -3500 1000 1000 180 360 1000]
)
        
        '''
        
class VQ44(package):
    def __init__(self, name="VQ44", libname="package",description="VQ44"):
        package.__init__(self, name, libname,description)
        self.smt = True
        self.pcbbody = '''
(
    Pad[20236 15748 24567 15748 1968 2000 3968 "23" "23" "edge2"]
    Pad[-24605 -12599 -20274 -12599 1968 2000 3968 "2" "2" ""]
    Pad[-24606 -9449 -20275 -9449 1968 2000 3968 "3" "3" ""]
    Pad[-24606 -3150 -20275 -3150 1968 2000 3968 "5" "5" ""]
    Pad[-24605 -6300 -20274 -6300 1968 2000 3968 "4" "4" ""]
    Pad[-24606 3150 -20275 3150 1968 2000 3968 "7" "7" ""]
    Pad[-24605 0 -20274 0 1968 2000 3968 "6" "6" ""]
    Pad[-24606 15748 -20275 15748 1968 2000 3968 "11" "11" ""]
    Pad[-24605 12598 -20274 12598 1968 2000 3968 "10" "10" ""]
    Pad[-24606 9449 -20275 9449 1968 2000 3968 "9" "9" ""]
    Pad[-24605 6299 -20274 6299 1968 2000 3968 "8" "8" ""]
    Pad[20236 -15748 24567 -15748 1968 2000 3968 "33" "33" "edge2"]
    Pad[20237 -12599 24568 -12599 1968 2000 3968 "32" "32" "edge2"]
    Pad[20236 -9449 24567 -9449 1968 2000 3968 "31" "31" "edge2"]
    Pad[20236 -3150 24567 -3150 1968 2000 3968 "29" "29" "edge2"]
    Pad[20237 -6300 24568 -6300 1968 2000 3968 "30" "30" "edge2"]
    Pad[20236 3150 24567 3150 1968 2000 3968 "27" "27" "edge2"]
    Pad[20237 0 24568 0 1968 2000 3968 "28" "28" "edge2"]
    Pad[-24606 -15748 -20275 -15748 1968 2000 3968 "1" "1" ""]
    Pad[20237 12598 24568 12598 1968 2000 3968 "24" "24" "edge2"]
    Pad[20236 9449 24567 9449 1968 2000 3968 "25" "25" "edge2"]
    Pad[20237 6299 24568 6299 1968 2000 3968 "26" "26" "edge2"]
    Pad[-15787 20275 -15787 24606 1968 2000 3968 "12" "12" "edge2"]
    Pad[12560 -24566 12560 -20235 1968 2000 3968 "35" "35" ""]
    Pad[9410 -24567 9410 -20236 1968 2000 3968 "36" "36" ""]
    Pad[3111 -24567 3111 -20236 1968 2000 3968 "38" "38" ""]
    Pad[6261 -24566 6261 -20235 1968 2000 3968 "37" "37" ""]
    Pad[-3189 -24567 -3189 -20236 1968 2000 3968 "40" "40" ""]
    Pad[-39 -24566 -39 -20235 1968 2000 3968 "39" "39" ""]
    Pad[-15787 -24567 -15787 -20236 1968 2000 3968 "44" "44" ""]
    Pad[-12637 -24566 -12637 -20235 1968 2000 3968 "43" "43" ""]
    Pad[-9488 -24567 -9488 -20236 1968 2000 3968 "42" "42" ""]
    Pad[-6338 -24566 -6338 -20235 1968 2000 3968 "41" "41" ""]
    Pad[15709 20275 15709 24606 1968 2000 3968 "22" "22" "edge2"]
    Pad[12560 20276 12560 24607 1968 2000 3968 "21" "21" "edge2"]
    Pad[9410 20275 9410 24606 1968 2000 3968 "20" "20" "edge2"]
    Pad[3111 20275 3111 24606 1968 2000 3968 "18" "18" "edge2"]
    Pad[6261 20276 6261 24607 1968 2000 3968 "19" "19" "edge2"]
    Pad[-3189 20275 -3189 24606 1968 2000 3968 "16" "16" "edge2"]
    Pad[-39 20276 -39 24607 1968 2000 3968 "17" "17" "edge2"]
    Pad[15709 -24567 15709 -20236 1968 2000 3968 "34" "34" ""]
    Pad[-12637 20276 -12637 24607 1968 2000 3968 "13" "13" "edge2"]
    Pad[-9488 20275 -9488 24606 1968 2000 3968 "14" "14" "edge2"]
    Pad[-6338 20276 -6338 24607 1968 2000 3968 "15" "15" "edge2"]
    ElementArc [-20899 -21079 900 900 90 360 400]
)        
        '''

class BUTTON_TH_package(package):
    def __init__(self, name="BUTTON_TH", libname="package",description="BUTTON_TH"):
        package.__init__(self, name, libname,description)
        self.smt = False
        self.pcbbody = '''
Element[0x00000000 "" "" "button_edge" 51000 54000 0 0 0 100 0x00000000]
(
    Pin[20000 0 6500 3000 7100 4600 "" "2" 0x00004001]
    Pin[25000 -10000 6500 3000 7100 4600 "" "4" 0x00004001]
    Pin[-6000 -10000 6500 3000 7100 4600 "" "3" 0x00004001]
    Pin[0 0 6500 3000 7100 4600 "" "1" 0x00004101]
    ElementLine [-10000 -15000 30000 -15000 1000]
    ElementLine [-10000 5000 30000 5000 1000]
    ElementLine [-10000 -15000 -10000 5000 1000]
    ElementLine [30000 -15000 30000 5000 1000]
)
        '''


#
# Devices
#
        
        
class Component(CDev):
    def __init__(self, refid="", val="", name="", libname="", symbolname="" , packagename=""):
        CDev.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.parsed=False
	self.datasheet=""
	self.drawing=""
         
    # parse
    # The lowest x and y coordinates of all sub-objects of an element are used as an attachment
    # point for the cross hair cursor of the main window, unless the element has a mark, in which
    # case that's the attachement point 
    
    def parsePad(self,args):
        #print 'Pad ' + args
#       Pad[-7500 7000 -7500 13500 2787 1600 3787 "" "1" "square,edge2"]
#       Pad [rX1 rY1 rX2 rY2 Thickness Clearance Mask "Name" "Number" SFlags]
#       Pad [rX1 rY1 rX2 rY2 Thickness Clearance Mask "Name" "Number" SFlags]
        rX1, rY1, rX2, rY2, Thickness, Clearance, Mask, Name, Number, SFlags = args.split()
        rX1 = int(rX1)
        rY1 = int(rY1)
        rX2 = int(rX2)
        rY2 = int(rY2)
        # Calculate center of the pad
        rX = int((rX1 + rX2) / 2)
        rY = int((rY1 + rY2) / 2)
        pin = CPin(Name,Number,rX,rY)
        pin.smt = True
        pin.num = int(Number.strip('"'))
        pin.thickness    = int(Thickness)
        pin.clearance    = int(Clearance)
        pin.mask         = int(Mask)
        # pcb attributes
        pin.rX1 = rX1
        pin.rY1 = rY1
        pin.rX2 = rX2
        pin.rY2 = rY2
        pin.sflags       = SFlags
        # make pad
        sizex = abs(rX1 - rX2) + pin.thickness    # distance between rX1 and rX2 + thinckess
        sizey = abs(rY1 - rY2) + pin.thickness    # rY1 and rY2 should be same so thinckess is sizey
        pin.pad = CPad(sizex, sizey, "S")
        
        size = pin.thickness + pin.clearance
        # make bbox and normalize it
        pin.bbox = Rectangle(rX1,rY1,rX2,rY2,0)
        # # make bbox covering pin with clearance, will be used for blockages
        rX1=pin.bbox.ll._x - size / 2
        rY1=pin.bbox.ll._y - size / 2
        rX2=pin.bbox.ur._x + size / 2
        rY2=pin.bbox.ur._y + size / 2
        pin.bbox = Rectangle(rX1,rY1,rX2,rY2,0)
        
        self.package.pins[pin.num]=pin
        
        
    def parsePin(self,args):
        #print 'Pin ' + args
#       Pin 16200 7000 7200 2000 9200 5200 "" "9" 0x01
#       Pin [rX rY Thickness Clearance Mask Drill "Name" "Number" SFlags]
        rX, rY, Thickness, Clearance, Mask, Drill, Name, Number, SFlags = args.split()
        pin = CPin(Name,Number,int(rX),int(rY))
        pin.smt = False
        pin.num = int(Number.strip('"'))
        pin.thickness    = int(Thickness)
        pin.clearance    = int(Clearance)
        pin.mask         = int(Mask)
        pin.drill        = int(Drill)
        # pcb attributes
        pin.sflags       = SFlags
        sizex = pin.thickness
        sizey = pin.thickness
        pin.pad = CPad(sizex, sizey, "R", pin.drill)
        # make bbox covering pin with clearance, will be used for blockages    
        size = pin.thickness + pin.clearance
        x1 = int(pin.pos._x - size / 2)
        x2 = int(pin.pos._x + size / 2)
        y1 = int(pin.pos._y - size / 2)
        y2 = int(pin.pos._y + size / 2)
        pin.bbox = Rectangle(x1,y1,x2,y2,0)
        self.package.pins[pin.num]=pin
        
        
        
            
    def parseLine(self,args):
        #print 'Line ' + args
#       ElementLine [X1 Y1 X2 Y2 Thickness]
        X1, Y1, X2, Y2, Thickness = args.split()
        line = Line([Point(int(X1),int(Y1)),Point(int(X2),int(Y2))], int(Thickness))
        self.package.geometry.append(line)
    
    def parseArc(self,args):
        #print 'Arc ' + args
#       ElementArc [X Y Width Height StartAngle DeltaAngle Thickness]
        #print ' parse Arc'
        X, Y, Width, Height, StartAngle, DeltaAngle, Thickness = args.split()
        arc = Arc( int(X), int(Y), int(Width), int(Height), int(StartAngle), int(DeltaAngle), int(Thickness))
        self.package.geometry.append(arc)
    
    # parse PCB package description and create device pins based on the package
    def parsePackage(self):
        #print 'parsing: "' + self.package.name + '" "' + self.package.description + '"'
        for line in self.package.pcbbody.splitlines():
            # filter out blank lines/comment lines
            lines = line.strip()
            
            # comment
            if not lines or lines.startswith('#'):
                continue
            # begin element body
            if not lines or lines.startswith('('):
                continue
            
            # end element body
            if not lines or lines.startswith(')'):
                continue
            
            words = lines.split('[')
            tag = words[0]
            tag = tag.strip()
###            print 'tag |' + tag + '|'
            args = words[1]
            args=args.strip('[]')
             
            if ( tag == 'Pad'):
                self.parsePad(args)
                
            if ( tag == 'Pin'):
                self.parsePin(args)
                
            if ( tag == 'ElementLine'):
                self.parseLine(args)
                
            if ( tag == 'ElementArc'):
                self.parseArc(args)
                
        # mark it parsed        
        self.parsed=True



class FIDUCIAL_L(Component):
	"Local FIDUCIAL class"
	def __init__(self, refid, val, name="fiducial_l", libname="fiducial", symbolname="fiducial_", packagename="FIDUCIAL"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		# make 1 mm local fiducial, val is size in mm
		self.package = FIDUCIAL_package(val, 1)	# default layer should be top ie 1
		self.parsePackage()
    
    
    
# will take package size as a parameter
class RESSMT(Component):
    "RESSMT class "
    def __init__(self, refid, val, name="resistor", libname="resistor", symbolname="resistor", packagename="RES0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = RES0805()
        self.parsePackage()
        self.addPin( CPin("1",    1    ))
        self.addPin( CPin("2",    2    ))
        
        
        
        
# will take package size as a parameter
class CAPSMT(Component):
    "CAPSMT class "
    def __init__(self, refid, val, name="capacitor", libname="capacitor", symbolname="capacitor", packagename="CAP0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = CAP0805()
        self.parsePackage()
        self.addPin( CPin("1",    1    ))
        self.addPin( CPin("2",    2    ))
        
 # will take package size as a parameter
class LEDSMT(Component):
    "LEDSMT class "
    def __init__(self, refid, val, name="LEDSMT", libname="LED", symbolname="LED", packagename="LED0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = LED0805()
        self.parsePackage()
        self.addPin( CPin("K",    1    ))
        self.addPin( CPin("A",    2    ))
        
# will take package size as a parameter
class DIODESMT(Component):
    "DIODESMT class "
    def __init__(self, refid, val, name="DIODESMT", libname="DIODE", symbolname="DIODE", packagename="DIODE0805"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = DIODE0805()
        self.parsePackage()
        self.addPin( CPin("K",    1    ))
        self.addPin( CPin("A",    2    ))
        
# will take package size as a parameter
class CAPPOLYSMT(Component):
    "CAPPOLYSMT class "
    def __init__(self, refid, val, name="capacitor_poly", libname="capacitor", symbolname="capacitor_poly", packagename="EIA7343"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = EIA7343()
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
class CAPTANTSMT(Component):
    "CAPTANTSMT class "
    def __init__(self, refid, val, name="capacitor_tantalum", libname="capacitor", symbolname="capacitor_tantalum", packagename="EIA7343"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = EIA7343()
        self.parsePackage()
        self.addPin( CPin("+",    1    ))
        self.addPin( CPin("-",    2    ))
        
class HEADER(Component):
    "Header class "
    def __init__(self, M,N,refid, val, name="header", libname="header", symbolname="header", packagename="HEADER_MXN_package"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HEADER_package(M,N,packagename,libname) # should call make header
        self.parsePackage()
        for i in range(M*N):
            self.addPin( CPin(str(i+1),    (i+1)    ))
            
class HC08201(Component):
    "HC08201 LCD class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="hc08201", packagename="HEADER_7X2"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HC08201_package(packagename,libname) # should call make header
        self.parsePackage()
        self.addPin( CPin('VSS',    1    ))
        self.addPin( CPin('VDD',    2    ))
        self.addPin( CPin('V0',     3    ))
        self.addPin( CPin('RS',     4    ))
        self.addPin( CPin('R/W',    5    ))
        self.addPin( CPin('E',      6    ))
        self.addPin( CPin('DB0',    7    ))
        self.addPin( CPin('DB1',    8    ))
        self.addPin( CPin('DB2',    9    ))
        self.addPin( CPin('DB3',    10   ))
        self.addPin( CPin('DB4',    11   ))
        self.addPin( CPin('DB5',    12   ))
        self.addPin( CPin('DB6',    13   ))
        self.addPin( CPin('DB7',    14   ))
        
           
class JTAG7X2(Component):
    "JTAG 14 pin 7x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag7x2", packagename="HEADER_7X2"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = HEADER_package(7, 2, packagename, libname, "JTAG 14 pin 7x2")
		self.parsePackage()
		self.addPin( CPin('VDD_1',  1    ))
		self.addPin( CPin('VSS_1',  2    ))
		self.addPin( CPin('nTRST',  3    ))
		self.addPin( CPin('VSS_2',  4    ))
		self.addPin( CPin('TDI',    5    ))
		self.addPin( CPin('VSS_3',  6    ))
		self.addPin( CPin('TMS',    7    ))
		self.addPin( CPin('VSS_4',  8    ))
		self.addPin( CPin('TCK',    9    ))
		self.addPin( CPin('VSS_5',  10   ))
		self.addPin( CPin('TDO',    11   ))
		self.addPin( CPin('nRESET', 12   ))
		self.addPin( CPin('VDD_2',  13   ))
		self.addPin( CPin('VSS_6',  14   ))
	
class JTAG10X2(Component):
    "JTAG 20 pin 10x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag10x2", packagename="HEADER_10X2"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = HEADER_package(10, 2, packagename, libname, "JTAG 20 pin 10x2")
		self.parsePackage()
		self.addPin( CPin('VDD_1',  1    ))
		self.addPin( CPin('VDD_2',  2    ))
		self.addPin( CPin('nTRST',  3    ))
		self.addPin( CPin('VSS_1',  4    ))
		self.addPin( CPin('TDI',    5    ))
		self.addPin( CPin('VSS_2',  6    ))
		self.addPin( CPin('TMS',    7    ))
		self.addPin( CPin('VSS_3',  8    ))
		self.addPin( CPin('TCK',    9    ))
		self.addPin( CPin('VSS_4',  10   ))
		self.addPin( CPin('NC_1',   11   ))
		self.addPin( CPin('VSS_5',  12   ))
		self.addPin( CPin('TDO',    13   ))
		self.addPin( CPin('VSS_6',  14   ))
		self.addPin( CPin('nRST',   15   ))
		self.addPin( CPin('VSS_7',  16   ))
		self.addPin( CPin('NC_2',   17   ))
		self.addPin( CPin('VSS_8',  18   ))
		self.addPin( CPin('NC_3',   19   ))
		self.addPin( CPin('VSS_9',  20   ))
	
class JTAG10X2_SMT(Component):
    "JTAG SMT 20 pin 10x2 class "
    def __init__(self, refid, val, name="header", libname="header", symbolname="jtag10x2", packagename="HEADER_SMT_10X2"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = HEADER_SMT_package(10, 2, packagename, libname, "JTAG SMT 20 pin 10x2")
		self.parsePackage()
		self.addPin( CPin('VDD_1',  1    ))
		self.addPin( CPin('VDD_2',  2    ))
		self.addPin( CPin('nTRST',  3    ))
		self.addPin( CPin('VSS_1',  4    ))
		self.addPin( CPin('TDI',    5    ))
		self.addPin( CPin('VSS_2',  6    ))
		self.addPin( CPin('TMS',    7    ))
		self.addPin( CPin('VSS_3',  8    ))
		self.addPin( CPin('TCK',    9    ))
		self.addPin( CPin('VSS_4',  10   ))
		self.addPin( CPin('NC_1',   11   ))
		self.addPin( CPin('VSS_5',  12   ))
		self.addPin( CPin('TDO',    13   ))
		self.addPin( CPin('VSS_6',  14   ))
		self.addPin( CPin('nRST',   15   ))
		self.addPin( CPin('VSS_7',  16   ))
		self.addPin( CPin('NC_2',   17   ))
		self.addPin( CPin('VSS_8',  18   ))
		self.addPin( CPin('NC_3',   19   ))
		self.addPin( CPin('VSS_9',  20   ))
		
class XTAL(Component):
    "XTAL class "
    def __init__(self, refid, val, name="xtal", libname="xtal", symbolname="xtal", packagename="HCU49"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = HCU49()
        self.parsePackage()
        self.addPin( CPin("X1",    1    ))
        self.addPin( CPin("X2",    2    ))
        
class DSUB9F(Component):
    "DSUB9F class "
    def __init__(self, refid, val, name="dsub9", libname="connector", symbolname="dsub9", packagename="DSUB9F"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = DSUB9F_package()
        self.parsePackage()
        # first 9 pins are connector pins
        for i in range(9):
            self.addPin( CPin(str(i),    (i+1)    ))
        # last 2 are mount pins
        self.addPin( CPin("COVER1",    10    ))
        self.addPin( CPin("COVER2",    11    ))
                
# LDOs  based in SOT223
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
        
class BUTTON_TH(Component):
    "BUTTON_TH class "
    def __init__(self, refid, val, name="BUTTON_TH", libname="connector", symbolname="button_th", packagename="BUTTON_TH"):
        Component.__init__(self, refid, val, name, libname, symbolname, packagename)
        self.package = BUTTON_TH_package()
        self.parsePackage()
        # first 9 pins are connector pins
        for i in range(4):
            self.addPin( CPin(str(i),    (i+1)    ))            
