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

from eda.components.NXP.lpc214x import *

from eda.components.JAE.USB import *
from eda.components.JAE.SD import *

from eda.components.ST.stm3210x import *

from eda.components.ST.M25PExx import *

from eda.components.ST.ST1480A import *

from eda.components.MAXIM.rs232 import *

from eda.components.FTDI.TTL_232R_3V3 import *

from eda.components.MODULE.DIP40 import *

from eda.components.MODULE.SW_DEBUG_CON import *

from eda.components.EEPROM.I2C import *

from eda.components.Abracon.ABM3B import *

from eda.components.Nichicon.F93 import *

from eda.components.Diodes.DCX100 import *

# LDO subcircuit
from eda.circuits.ldo_ld1117 import *


crefid = 1
rrefid = 1

#####################################################################
# connect to DIP40 by port 
# P0  <-> PA0
# P15 <-> PA15
# X0  <-> PB0
# X15 <-> PB15

# Use 0.036" holes for the header

# VIA Rajda
# 40 x 24 mil
# 32 x 12 mil na plytce
# 55 mili round is STANDARDVIA
# 40/28, 40/24, 40/20, 32/12

# Analog VDD
# filtr RC 100 ohm + 10uF
# Digital VDD
# 100nF on all VDD


def connect_by_port():
    # Pin 5 P0 - 10 RB0 GPIO; comparator output;MIWU/Interrupt input
    # IO AN0 - Analog input 0
    P0net = CNet("P0")
    sch.addNet(P0net)
    P0net.add(CNode(MOD1,'P0'))
    # CPU
    P0net.add(CNode(U1,'PA0-WKUP/USART2_CTS/ADC_IN0/TIM2_CH1_ETR'))
    
    
    # Pin 6 P1 - 11 RB1 GPIO; comparator negative input;MIWU/Interrupt input
    # IO AN1 - Analog input 1
    P1net = CNet("P1")
    sch.addNet(P1net)
    P1net.add(CNode(MOD1,'P1'))
    # CPU
    P1net.add(CNode(U1,'PA1/USART2_RTS/ADC_IN1/TIM2_CH2'))
    
    
    # Pin 7 P2 - 12 RB2 GPIO; comparator positive input;MIWU/Interrupt input 
    # IO AN2 - Analog input 2
    P2net = CNet("P2")
    sch.addNet(P2net)
    P2net.add(CNode(MOD1,'P2'))
    # CPU
    P2net.add(CNode(U1,'PA2/USART2_TX/ADC_IN2/TIM2_CH3'))
    
    
    # Pin 8 P3 - 13 RB3 GPIO; MIWU/Interrupt input 
    # IO AN3 - Analog input 3
    P3net = CNet("P3")
    sch.addNet(P3net)
    P3net.add(CNode(MOD1,'P3'))
    # CPU
    P3net.add(CNode(U1,'PA3/USART2_RX/ADC_IN3/TIM2_CH4'))
    
    
    # Pin 9 P4 - 14 RB4 GPIO; MIWU/Interrupt input; Timer T1 Capture Input 1
    P4net = CNet("P4")
    sch.addNet(P4net)
    P4net.add(CNode(MOD1,'P4'))
    # CPU
    P4net.add(CNode(U1,'PA4/SPI1_NSS/USART2_CK/ADC_IN4'))
    
    # Pin 10 P5 - 15 RB5 GPIO; MIWU/Interrupt input; Timer T1 Capture Input 2
    P5net = CNet("P5")
    sch.addNet(P5net)
    P5net.add(CNode(MOD1,'P5'))
    # CPU
    P5net.add(CNode(U1,'PA5/SPI1_SCK/ADC_IN5'))
    
    # Pin 11 P6 - 16 RB6 GPIO; MIWU/Interrupt input; Timer T1 PWM/Compare Output
    P6net = CNet("P6")
    sch.addNet(P6net)
    P6net.add(CNode(MOD1,'P6'))
    # CPU
    P6net.add(CNode(U1,'PA6/SPI1_MISO/ADC_IN6/TIM3_CH1'))
    
    # Pin 12 P7 - RB7 GPIO; MIWU/Interrupt input; Timer T1 External Event Counter Input
    P7net = CNet("P7")
    sch.addNet(P7net)
    P7net.add(CNode(MOD1,'P7'))
    # CPU
    P7net.add(CNode(U1,'PA7/SPI1_MOSI/ADC_IN7/TIM3_CH2'))
    
    # Pin 13 P8 - 20 RC0 GPIO;Timer T2 Capture Input 1
    P8net = CNet("P8")
    sch.addNet(P8net)
    P8net.add(CNode(MOD1,'P8'))
    # CPU
    P8net.add(CNode(U1,'PA8/USART1_CK/MCO'))
    
    # Pin 14 P9 - 21 RC1 GPIO;Timer T2 Capture Input 2
    P9net = CNet("P9")
    sch.addNet(P9net)
    P9net.add(CNode(MOD1,'P9'))
    # CPU
    P9net.add(CNode(U1,'PA9/USART1_TX'))
    
    # Pin 15 P10 - 22 RC2 GPIO;Timer T2 PWM compare output
    P10net = CNet("P10")
    sch.addNet(P10net)
    P10net.add(CNode(MOD1,'P10'))
    # CPU
    P10net.add(CNode(U1,'PA10/USART1_RX'))
    
    # Pin 16 P11 - 23 RC3 GPIO;Timer T2  External Event Counter Input
    P11net = CNet("P11")
    sch.addNet(P11net)
    P11net.add(CNode(MOD1,'P11'))
    # CPU
    P11net.add(CNode(U1,'PA11/USART1_CTS'))
    
    # Pin 17 P12 - 24 RC4 GPIO
    P12net = CNet("P12")
    sch.addNet(P12net)
    P12net.add(CNode(MOD1,'P12'))
    # CPU
    P12net.add(CNode(U1,'PA12/USART1_RTS'))
    
    # Pin 18 P13 - 25 RC5 GPIO
    P13net = CNet("P13")
    sch.addNet(P13net)
    P13net.add(CNode(MOD1,'P13'))
    # CPU
    P13net.add(CNode(U1,'PA13/JTMS/SWDIO'))
    
    # Pin 19 P14 - 26 RC6 GPIO
    P14net = CNet("P14")
    sch.addNet(P14net)
    P14net.add(CNode(MOD1,'P14'))
    # CPU
    P14net.add(CNode(U1,'PA14/JTCK/SWCLK'))
    
    # Pin 20 P15 - 27 RC7 GPIO
    P15net = CNet("P15")
    sch.addNet(P15net)
    P15net.add(CNode(MOD1,'P15'))
    # CPU
    P15net.add(CNode(U1,'PA15/JTDI'))
    
    # Right Side
    # Pin 21 X0 - 28 RD0 GPIO
    X0net = CNet("X0")
    sch.addNet(X0net)
    X0net.add(CNode(MOD1,'X0'))
    # CPU
    X0net.add(CNode(U1,'PB0/ADC_IN8/TIM3_CH3'))
    
    # Pin 22 X1 - 29 RD1 GPIO
    X1net = CNet("X1")
    sch.addNet(X1net)
    X1net.add(CNode(MOD1,'X1'))
    # CPU
    X1net.add(CNode(U1,'PB1/ADC_IN9/TIM3_CH4'))
    
    # Pin 23 X2 - 30 RD2 GPIO
    X2net = CNet("X2")
    sch.addNet(X2net)
    X2net.add(CNode(MOD1,'X2'))
    # CPU
    X2net.add(CNode(U1,'PB2/BOOT1'))
    
    # Pin 24 X3 - 31 RD3 GPIO
    X3net = CNet("X3")
    sch.addNet(X3net)
    X3net.add(CNode(MOD1,'X3'))
    # CPU
    X3net.add(CNode(U1,'PB3/JTDO/TRACESWO'))
    
    # Pin 25 X4 - 34 RD4 GPIO
    X4net = CNet("X4")
    sch.addNet(X4net)
    X4net.add(CNode(MOD1,'X4'))
    # CPU
    X4net.add(CNode(U1,'PB4/JNTRST'))
    
    # Pin 26 X5 - 35 RD5 GPIO
    X5net = CNet("X5")
    sch.addNet(X5net)
    X5net.add(CNode(MOD1,'X5'))
    # CPU
    X5net.add(CNode(U1,'PB5/I2C1_SMBAl'))
    
    # Pin 27 X6 - 36 RD6 GPIO
    X6net = CNet("X6")
    sch.addNet(X6net)
    X6net.add(CNode(MOD1,'X6'))
    # CPU
    X6net.add(CNode(U1,'PB6/I2C1_SCL/TIM4_CH1'))
    
    # Pin 28 X7 - 37 RD7 GPIO
    X7net = CNet("X7")
    sch.addNet(X7net)
    X7net.add(CNode(MOD1,'X7'))
    # CPU
    X7net.add(CNode(U1,'PB7/I2C1_SDA/TIM4_CH2'))
    
    # Pin 29 X8 - 38 RE0 GPIO
    X8net = CNet("X8")
    sch.addNet(X8net)
    X8net.add(CNode(MOD1,'X8'))
    # CPU
    X8net.add(CNode(U1,'PB8/TIM4_CH3'))
    
    # Pin 30 X9 - 39 RE1 GPIO
    X9net = CNet("X9")
    sch.addNet(X9net)
    X9net.add(CNode(MOD1,'X9'))
    # CPU
    X9net.add(CNode(U1,'PB9/TIM4_CH4'))
    
    # Pin 31 X10 - 40 RE2 GPIO
    X10net = CNet("X10")
    sch.addNet(X10net)
    X10net.add(CNode(MOD1,'X10'))
    # CPU
    X10net.add(CNode(U1,'PB10/I2C2_SCL/USART3_TX'))
    
    # Pin 32 X11 - 41 RE3 GPIO
    X11net = CNet("X11")
    sch.addNet(X11net)
    X11net.add(CNode(MOD1,'X11'))
    # CPU
    X11net.add(CNode(U1,'PB11/I2C2_SDA/USART3_RX'))
    
    # Pin 33 X12 - 42 RE4 GPIO
    X12net = CNet("X12")
    sch.addNet(X12net)
    X12net.add(CNode(MOD1,'X12'))
    # CPU
    X12net.add(CNode(U1,'PB12/SPI2_NSS/I2C2_SMBAl/USART3_CK'))
    
    # Pin 34 X13 - 43 RE5 GPIO
    X13net = CNet("X13")
    sch.addNet(X13net)
    X13net.add(CNode(MOD1,'X13'))
    # CPU
    X13net.add(CNode(U1,'PB13/SPI2_SCK/USART3_CTS'))
    
    # Pin 35 X14 - 44 RE6 GPIO
    X14net = CNet("X14")
    sch.addNet(X14net)
    X14net.add(CNode(MOD1,'X14'))
    # CPU
    X14net.add(CNode(U1,'PB14/SPI2_MISO/USART3_RTS'))
    
    # Pin 36 X15 - 45 RE7 GPIO
    X15net = CNet("X15")
    sch.addNet(X15net)
    X15net.add(CNode(MOD1,'X15'))
    # CPU
    X15net.add(CNode(U1,'PB15/SPI2_MOSI'))
#####################################################################



    
def gen_schematic(sch, DesignName, LibName):


	# Ground Net
	GNDnet = CNet("GND")
	sch.addNet(GNDnet)

	# VDD 3.3V Net
	VDD3V3net = CNet("3V3")
	sch.addNet(VDD3V3net)



	# Add stm3210x
	U1 = STM3210X("U1","","stm3210_lqfp48",LibName,"STM3210")
	sch.addDev(U1)
	sch.addSymbolFromDev(U1, 4, "STM3210")


	# Connect stm3210x to GND
	# VSS
	GNDnet.add(CNode(U1,'VSS_1'))
	GNDnet.add(CNode(U1,'VSS_2'))
	GNDnet.add(CNode(U1,'VSS_3'))
	# analog ground
	GNDnet.add(CNode(U1,'VSSA'))    

	# Connect stm3210x to 3V3
	VDD3V3net.add(CNode(U1,'VDD_1'))
	VDD3V3net.add(CNode(U1,'VDD_2'))
	VDD3V3net.add(CNode(U1,'VDD_3'))
	VDD3V3net.add(CNode(U1,'VDDA'))        # analog
	VDD3V3net.add(CNode(U1,'VBAT'))        # battery

	###########################################
	# Add simple reset with
	# Capacitor + Resistor

	# 0805 size
	C30 = CAPSMT("C30","100nF","CAP_RESET",LibName,"CAP")
	sch.addDev(C30)
	sch.addSymbolFromDev(C30, 0, "CAP")
	# pin 1 tied to GND, pin 2 tied to RESET#
	GNDnet.add(CNode(C30,'1'))

	# 0805 size
	R30 = RESSMT("R30","10k","RES_RESET",LibName,"RES")
	sch.addDev(R30)
	sch.addSymbolFromDev(R30, 0, "RES")
	# pin 1 tied to to RESET#, pin 2 tied 3V3
	VDD3V3net.add(CNode(R30,'2'))

	###########################################
	# Add Crystal and Capacitors
	Q1 = ABM3B("Q1","12 Mhz","Q1_12MHz",LibName,"ABM3B")
	sch.addDev(Q1)
	sch.addSymbolFromDev(Q1, 0, "ABM3B")

	# 0805 size
	CQ1 = CAPSMT("CQ1","18pF","CAP_1_Q1",LibName,"CAP")
	sch.addDev(CQ1)
	# 0805 size
	CQ2 = CAPSMT("CQ2","18pF","CAP_2_Q1",LibName,"CAP")
	sch.addDev(CQ2)

	OSC_OUTnet = CNet("OSC_OUT")
	sch.addNet(OSC_OUTnet)
	OSC_OUTnet.add(CNode(U1,'OSC_OUT'))
	OSC_OUTnet.add(CNode(Q1, '3'))
	GNDnet.add(CNode(Q1, 'GND_2'))
	OSC_OUTnet.add(CNode(CQ1, '1'))
	GNDnet.add(CNode(CQ1, '2'))

	OSC_INnet = CNet("OSC_IN")
	sch.addNet(OSC_INnet)
	OSC_INnet.add(CNode(U1,'OSC_IN'))
	OSC_INnet.add(CNode(Q1, '1'))
	GNDnet.add(CNode(Q1, 'GND_4'))
	OSC_INnet.add(CNode(CQ2, '2'))
	GNDnet.add(CNode(CQ2, '1'))

	###########################################
	# ADD LED and resistor # 0805 size
	# Green diode 2.1V
	LED1 = LEDSMT("LED1","Green","LED",LibName,"LED")
	sch.addDev(LED1)
	sch.addSymbolFromDev(LED1, 0, "LED")
	# 20 mA from 3.3V 3.3 - 2.1 = 1.2 V -> 60 ohm
	R50 = RESSMT("R50","60","RES_LED",LibName,"RES")
	sch.addDev(R50)

	LEDnet = CNet("LED")
	sch.addNet(LEDnet)

	GNDnet.add(CNode(LED1, 'K'))
	LEDnet.add(CNode(LED1, 'A'))
	LEDnet.add(CNode(R50,  '1'))
	VDD3V3net.add(CNode(R50,'2'))

	###########################################
	# RS232 TxD, RxD and Reset

	U4 = DCX114EU("U4","","DCX114EU_SERIAL",LibName,"DCX114EU")
	sch.addDev(U4)
	sch.addSymbolFromDev(U4, 2, "DCX114EU")

	# Tripple diode D1 is used for SIN, D2 is used for ATN
	U5 = BAS16TW("U5","","BAS16TW",LibName,"BAS16TW")
	sch.addDev(U5)
	sch.addSymbolFromDev(U5, 2, "BAS16TW")

	##########################################################
	# SIN
	# U4 Q1 is pre-biased NPN with R1 and R2 it is used for RxD input SIN
	# Base is conected to SIN and through diode and resistor to SOUT
	# Collector is connected via resistor to VDD3V3
	# Emiter is connected to GND

	GNDnet.add(CNode(U4,'EQ1'))
	#P2net.add(CNode(U4,'BQ1'))            # 'PA2/USART2_TX/ADC_IN2/TIM2_CH3'
	#SOUTnet.add(CNode(U4,'CQ1'))

	# 0805 size
	R41 = RESSMT("R41","10k","RES_RXD",LibName,"RES")
	sch.addDev(R41)

	#Connect collector with output resistor
	# Q1CNET is P3
	#Q1Cnet = CNet("Q1CNET")
	#sch.addNet(Q1Cnet)

	# Connect USART RxD
	#Q1Cnet.add(CNode(U1,'PA3/USART2_RX/ADC_IN3/TIM2_CH4'))
	#Q1Cnet.add(CNode(U4,'CQ1'))
	#Q1Cnet.add(CNode(R41,'1'))
	# Connect pull-up resistor to 3V3
	VDD3V3net.add(CNode(R41,'2'))

	##########################################################
	# SOUT
	# U4 Q2 is pre-biased PNP with R1 and R2
	# it is used for TxD output SOUT
	# Base is conected to TxD ouput from CPU
	# Emiter is at VDD3V3
	# Collector is connected to SOUT
	# through resistor and diode to TxD line from RS232
	# Capacitor between diode and resitor is conected to GND

	VDD3V3net.add(CNode(U4, 'EQ2'))
	#VDD3V3net.add(CNode(U4, 'BQ2'))
	#VDD3V3net.add(CNode(U4, 'CQ2'))


	##########################################################
	# Diode and resistor between SIN and SOUT
	# Resitsor R40  connected to SOUT
	R40 = RESSMT("R40","10k","RES_BOOST",LibName,"RES")
	sch.addDev(R40)
	#SOUTnet.add(CNode(R40,'1'))

	# Capacitor to ground
	C40 = CAPSMT("C40","100nF","CAP_BOOST",LibName,"CAP")
	sch.addDev(C40)
	GNDnet.add(CNode(C40, '1'))

	# Diode net 
	Dnet = CNet("DNET")
	sch.addNet(Dnet)
	Dnet.add(CNode(R40,'2'))        # Resistor
	Dnet.add(CNode(C40,'2'))        # Capacitor
	Dnet.add(CNode(U5,'A1'))        # Diode Anode SIN
	Dnet.add(CNode(U5,'A2'))        # Diode Anode ATN
	# Cathode is connected to SIN
	#SINnet.add(CNode(U5,'C1'))

	##########################################################
	# Reset
	U6 = DCX114EU("U6","","DCX114EU_RESET",LibName,"DCX114EU")
	sch.addDev(U6)

	# U6 Q1 is pre-biased NPN with R1 and R2
	# it is used for Reset ATN
	# Base is conected to ATN
	# Collector is connected to RESET#
	# Emiter is connected to GND
	GNDnet.add(CNode(U6, 'EQ1'))

	###########################################
	# Add 40 pin module layout
	MOD1=DIP40("MOD1","","DIP40",LibName,"DIP40")
	sch.addDev(MOD1)
	sch.addSymbolFromDev(MOD1, 2, "DIP40")


	# Add Header for left side
	#CON1=HEADER(20,1,"CON1","","Header 20x1")
	#sch.addDev(CON1)

	# Add Header for right side
	#CON2=HEADER(20,1,"CON2","","Header 20x1")
	#sch.addDev(CON2)


	###########################################
	# Power LDO
	# 3.3 V LDO
	# Power supply 12V
	VDD12Vnet = CNet("12V")
	sch.addNet(VDD12Vnet)

	U2 = LD1117S33("U2","","LD1117S33",LibName,"LD1117")
	sch.addDev(U2)
	sch.addSymbolFromDev(U2, 2, "LD1117")

	VDD12Vnet.add(CNode(U2,'IN'))
	VDD3V3net.add(CNode(U2,'OUT'))
	GNDnet.add(CNode(U2,'GND'))
	GNDnet.add(CNode(U2,'GND2'))
        
	# LDO ld1117 sub-circuit
	#ldo = ldo_ld1117()
	#ldo.add(sch,U2,VDD12Vnet,VDD3V3net,GNDnet,10,10)

	# Input caps
	C11 = F93_B("C11","","CAP_IN_TANT",LibName,"CAPTANT")
	sch.addDev(C11)
	sch.addSymbolFromDev(C11, 2, "CAPTANT")
	VDD12Vnet.add(CNode(C11,'+'))
	GNDnet.add(CNode(C11,'-'))

	# This cap is not needed on input
	#C12 = CAPSMT("C12","","cap ceramic IN")
	#sch.addDev(C12)       
	#VDD12Vnet.add(CNode(C12,'1'))
	#GNDnet.add(CNode(C12,'2'))
        
	# Output caps
	C21 = F93_B("C21","","CAP_OUT_TANT",LibName,"CAPTANT")
	sch.addDev(C21)
	VDD3V3net.add(CNode(C21,'+'))
	GNDnet.add(CNode(C21,'-'))

	C22 = CAPSMT("C22","","CAP_OUT_CER",LibName,"CAP")
	sch.addDev(C22)        
	VDD3V3net.add(CNode(C22,'1'))
	GNDnet.add(CNode(C22,'2'))


	###########################################
	# Add 24LCxx in SO8
	# I2C memory
	#U3 = EE24LCXX("U3","","EE24LCXX")

	###########################################
	# SPI memory 
	# Add M25PEXX in SO8
	U3 = M25PEXX("U3","","M25PEXX",LibName,"M25PEXX")
	sch.addDev(U3)
	sch.addSymbolFromDev(U3, 2, "M25PEXX")

	# 0805 size
	# tied to 3V3 and S#
	R60 = RESSMT("R60","10k","RES_3V3",LibName,"RES")
	sch.addDev(R60)
	# tied to PA4/SPI1_NSS/USART2_CK/ADC_IN4 and S#
	R61 = RESSMT("R61","63","RES_S#",LibName,"RES")
	sch.addDev(R61)

	# tied to PA6/SPI1_MISO/ADC_IN6/TIM3_CH1 and Q
	R62 = RESSMT("R62","62","RES_Q",LibName,"RES")
	sch.addDev(R62)

	# tie pins to ground and 3V3
	GNDnet.add(CNode(U3, 'VSS'))
	VDD3V3net.add(CNode(U3,'VCC'))
	VDD3V3net.add(CNode(U3,'TSL#_W#'))
	VDD3V3net.add(CNode(U3,'RESET#'))

	VDD3V3net.add(CNode(R60,'2'))

	# P4 net
	# Connect to SPI1 PA4 through R61
	#'PA4/SPI1_NSS/USART2_CK/ADC_IN4'
	#SPI1_NSSnet = CNet("SPI1_NSS")
	#sch.addNet(SPI1_NSSnet)
	#SPI1_NSSnet.add(CNode(U1, 'PA4/SPI1_NSS/USART2_CK/ADC_IN4'))
	#SPI1_NSSnet.add(CNode(R61, '1'))

	SPI_Snet = CNet("SPI_S#")
	sch.addNet(SPI_Snet)
	SPI_Snet.add(CNode(R61, '2'))
	SPI_Snet.add(CNode(U3, 'S#'))
	SPI_Snet.add(CNode(R60, '1'))    # pull-up  to 3V3

	# P5 net
	# Connect to SPI1 PA5
	#"PA5/SPI1_SCK/ADC_IN5"
	#SPI1_SCKnet = CNet("SPI1_SCK")
	#sch.addNet(SPI1_SCKnet)
	#SPI1_SCKnet.add(CNode(U1, 'PA5/SPI1_SCK/ADC_IN5'))
	#SPI1_SCKnet.add(CNode(U3, 'C'))


	# P6 Net
	# Connect to SPI1 PA6 through R62
	#"PA6/SPI1_MISO/ADC_IN6/TIM3_CH1"
	#SPI1_MISOnet = CNet("SPI1_MISO")
	#sch.addNet(SPI1_MISOnet)
	#SPI1_MISOnet.add(CNode(U1, 'PA6/SPI1_MISO/ADC_IN6/TIM3_CH1'))
	#SPI1_MISOnet.add(CNode(R62, '1'))

	SPI_Qnet = CNet("SPI_Q")
	sch.addNet(SPI_Qnet)
	SPI_Qnet.add(CNode(R62, '2'))
	SPI_Qnet.add(CNode(U3, 'Q'))

	# P&
	#"PA7/SPI1_MOSI/ADC_IN7/TIM3_CH2"
	#SPI1_MOSInet = CNet("SPI1_MOSI")
	#sch.addNet(SPI1_MOSInet)
	#SPI1_MOSInet.add(CNode(U1, 'PA7/SPI1_MOSI/ADC_IN7/TIM3_CH2'))
	#SPI1_MOSInet.add(CNode(U3, 'D'))

	###########################################
	# Add FTDI connector
	CON3=TTL_232R_3V3("CON3","","TTL_232R_3V3",LibName,"TTL_232R_3V3")
	sch.addDev(CON3)
	sch.addSymbolFromDev(CON3,1, "TTL_232R_3V3")
	GNDnet.add(CNode(CON3, 'GND'))

	# Jumper for 3V3 from the FTDI connector
	J1=HEADER(2,1,"J1","","J1",LibName,"J1", "J1")
	sch.addDev(J1)
	sch.addSymbolFromDev(J1,1, "J1")
	VDD3V3net.add(CNode(J1,'1'))
	# Connect J1 to 3V3 from serial connector
	VCC3V3net = CNet("VCC3V3")
	sch.addNet(VCC3V3net)
	VCC3V3net.add(CNode(J1,'2'))
	VCC3V3net.add(CNode(CON3, 'VCC'))


	# No connection to VDD3V3, should have jumper so it can power the chip from USB
	# VDD3V3net.add(CNode(CON3, 'VCC'))

	# Add connections to USART1

	#"PA9/USART1_TX" 
	TXDnet = CNet("TXD")
	sch.addNet(TXDnet)
	# CPU
	TXDnet.add(CNode(U1,'PA9/USART1_TX'))
	# Serial header
	TXDnet.add(CNode(CON3,'TXD'))

	#"PA10/USART1_RX"
	RXDnet = CNet("RXD")
	sch.addNet(RXDnet)
	# CPU
	RXDnet.add(CNode(U1,'PA10/USART1_RX'))
	# Serial header
	RXDnet.add(CNode(CON3,'RXD'))

	#"PA11/USART1_CTS"
	CTSnet = CNet("CTS")
	sch.addNet(CTSnet)
	# CPU
	CTSnet.add(CNode(U1,'PA11/USART1_CTS'))
	# Serial header
	CTSnet.add(CNode(CON3,'CTS#'))

	#"PA12/USART1_RTS"
	RTSnet = CNet("RTS")
	sch.addNet(RTSnet)
	# CPU
	RTSnet.add(CNode(U1,'PA12/USART1_RTS'))
	# Serial header
	RTSnet.add(CNode(CON3,'RTS#'))



	##################################################################################################
	# Connection to the DIP40 pin

	# Left side
	# Pin 1 SOUT
	# Serial Out
	SOUTnet = CNet("SOUT")
	sch.addNet(SOUTnet)
	SOUTnet.add(CNode(MOD1,'SOUT'))
	# CPU - can not connect directly
	# PA2/USART2_TX/ADC_IN2/TIM2_CH3
	# Serial header
	# Serial Interface - Resistor R40
	SOUTnet.add(CNode(R40,'1'))
	SOUTnet.add(CNode(U4,'CQ2'))



	# Pin 2 SIN
	# Serial IN
	SINnet = CNet("SIN")
	sch.addNet(SINnet)
	SINnet.add(CNode(MOD1,'SIN'))
	# CPU - can not connect directly
	# PA3/USART2_RX/ADC_IN3/TIM2_CH4
	# Serial Interface - Base Q1
	SINnet.add(CNode(U4,'BQ1'))
	# Cathode U5 D1
	SINnet.add(CNode(U5,'C1'))


	# Pin 3 ATN
	ATNnet = CNet("ATN")
	sch.addNet(ATNnet)
	ATNnet.add(CNode(MOD1,'ATN'))
	# Serial header
	###ATNnet.add(CNode(CON3,'RTS#'))
	# Reset Interface - Base Q1
	ATNnet.add(CNode(U6,'BQ1'))
	# Cathode U5 D2
	ATNnet.add(CNode(U5,'C2'))


	# Pin 4 VSS_1
	# Ground GND
	GNDnet.add(CNode(MOD1,'VSS_1'))

	#################################################################
	# Connect by closest pin

	# Pin 5 P0 - 10 RB0 GPIO; comparator output;MIWU/Interrupt input
	# IO AN0 - Analog input 0
	P0net = CNet("P0")
	sch.addNet(P0net)
	P0net.add(CNode(MOD1,'P0'))
	# CPU
	P0net.add(CNode(U1,'PA0-WKUP/USART2_CTS/ADC_IN0/TIM2_CH1_ETR'))


	# Pin 6 P1 - 11 RB1 GPIO; comparator negative input;MIWU/Interrupt input
	# IO AN1 - Analog input 1
	P1net = CNet("P1")
	sch.addNet(P1net)
	P1net.add(CNode(MOD1,'P1'))
	# CPU
	P1net.add(CNode(U1,'PA1/USART2_RTS/ADC_IN1/TIM2_CH2'))


	# Pin 7 P2 - 12 RB2 GPIO; comparator positive input;MIWU/Interrupt input 
	# IO AN2 - Analog input 2
	P2net = CNet("P2")
	sch.addNet(P2net)
	P2net.add(CNode(MOD1,'P2'))
	# CPU
	P2net.add(CNode(U1,'PA2/USART2_TX/ADC_IN2/TIM2_CH3'))
	# Serial interface
	P2net.add(CNode(U4,'BQ2'))            # 'PA2/USART2_TX/ADC_IN2/TIM2_CH3'


	# Pin 8 P3 - 13 RB3 GPIO; MIWU/Interrupt input 
	# IO AN3 - Analog input 3
	P3net = CNet("P3")
	sch.addNet(P3net)
	P3net.add(CNode(MOD1,'P3'))
	# CPU
	P3net.add(CNode(U1,'PA3/USART2_RX/ADC_IN3/TIM2_CH4'))
	# Serial interface
	P3net.add(CNode(U4,'CQ1'))
	P3net.add(CNode(R41,'1'))


	# Pin 9 P4 - 14 RB4 GPIO; MIWU/Interrupt input; Timer T1 Capture Input 1
	P4net = CNet("P4")
	sch.addNet(P4net)
	P4net.add(CNode(MOD1,'P4'))
	# CPU
	P4net.add(CNode(U1,'PA4/SPI1_NSS/USART2_CK/ADC_IN4'))
	# SPI NSS
	P4net.add(CNode(R61, '1'))

	# Pin 10 P5 - 15 RB5 GPIO; MIWU/Interrupt input; Timer T1 Capture Input 2
	P5net = CNet("P5")
	sch.addNet(P5net)
	P5net.add(CNode(MOD1,'P5'))
	# CPU
	P5net.add(CNode(U1,'PA5/SPI1_SCK/ADC_IN5'))
	# SPI SCK
	P5net.add(CNode(U3, 'C'))

	# Pin 11 P6 - 16 RB6 GPIO; MIWU/Interrupt input; Timer T1 PWM/Compare Output
	P6net = CNet("P6")
	sch.addNet(P6net)
	P6net.add(CNode(MOD1,'P6'))
	# CPU
	P6net.add(CNode(U1,'PA6/SPI1_MISO/ADC_IN6/TIM3_CH1'))
	# SPI MISO
	P6net.add(CNode(R62, '1'))

	# Pin 12 P7 - RB7 GPIO; MIWU/Interrupt input; Timer T1 External Event Counter Input
	P7net = CNet("P7")
	sch.addNet(P7net)
	P7net.add(CNode(MOD1,'P7'))
	# CPU
	P7net.add(CNode(U1,'PA7/SPI1_MOSI/ADC_IN7/TIM3_CH2'))
	# SPI
	P7net.add(CNode(U3, 'D'))

	# Pin 13 P8 - 20 RC0 GPIO;Timer T2 Capture Input 1
	P8net = CNet("P8")
	sch.addNet(P8net)
	P8net.add(CNode(MOD1,'P8'))
	# CPU
	P8net.add(CNode(U1,'PB0/ADC_IN8/TIM3_CH3'))

	# Pin 14 P9 - 21 RC1 GPIO;Timer T2 Capture Input 2
	P9net = CNet("P9")
	sch.addNet(P9net)
	P9net.add(CNode(MOD1,'P9'))
	# CPU
	P9net.add(CNode(U1,'PB1/ADC_IN9/TIM3_CH4'))

	# Pin 15 P10 - 22 RC2 GPIO;Timer T2 PWM compare output
	P10net = CNet("P10")
	sch.addNet(P10net)
	P10net.add(CNode(MOD1,'P10'))
	# CPU
	P10net.add(CNode(U1,'PB2/BOOT1'))

	# Pin 16 P11 - 23 RC3 GPIO;Timer T2  External Event Counter Input
	P11net = CNet("P11")
	sch.addNet(P11net)
	P11net.add(CNode(MOD1,'P11'))
	# CPU
	P11net.add(CNode(U1,'PB10/I2C2_SCL/USART3_TX'))

	# Pin 17 P12 - 24 RC4 GPIO
	P12net = CNet("P12")
	sch.addNet(P12net)
	P12net.add(CNode(MOD1,'P12'))
	# CPU
	P12net.add(CNode(U1,'PB11/I2C2_SDA/USART3_RX'))

	# Pin 18 P13 - 25 RC5 GPIO
	P13net = CNet("P13")
	sch.addNet(P13net)
	P13net.add(CNode(MOD1,'P13'))
	# CPU
	P13net.add(CNode(U1,'PB12/SPI2_NSS/I2C2_SMBAl/USART3_CK'))

	# Pin 19 P14 - 26 RC6 GPIO
	P14net = CNet("P14")
	sch.addNet(P14net)
	P14net.add(CNode(MOD1,'P14'))
	# CPU
	P14net.add(CNode(U1,'PB13/SPI2_SCK/USART3_CTS'))

	# Pin 20 P15 - 27 RC7 GPIO
	P15net = CNet("P15")
	sch.addNet(P15net)
	P15net.add(CNode(MOD1,'P15'))
	# CPU
	P15net.add(CNode(U1,'PB14/SPI2_MISO/USART3_RTS'))

	# Right Side
	# Pin 21 X0 - 28 RD0 GPIO
	X0net = CNet("X0")
	sch.addNet(X0net)
	X0net.add(CNode(MOD1,'X0'))
	# CPU
	X0net.add(CNode(U1,'PB15/SPI2_MOSI'))

	# Pin 22 X1 - 29 RD1 GPIO
	X1net = CNet("X1")
	sch.addNet(X1net)
	X1net.add(CNode(MOD1,'X1'))
	# CPU
	X1net.add(CNode(U1,'PA8/USART1_CK/MCO'))

	# Pin 23 X2 - 30 RD2 GPIO
	X2net = CNet("X2")
	sch.addNet(X2net)
	X2net.add(CNode(MOD1,'X2'))
	# CPU
	X2net.add(CNode(U1,'PA13/JTMS/SWDIO'))

	# Pin 24 X3 - 31 RD3 GPIO
	X3net = CNet("X3")
	sch.addNet(X3net)
	X3net.add(CNode(MOD1,'X3'))
	# CPU
	X3net.add(CNode(U1,'PA14/JTCK/SWCLK'))

	# Pin 25 X4 - 34 RD4 GPIO
	X4net = CNet("X4")
	sch.addNet(X4net)
	X4net.add(CNode(MOD1,'X4'))
	# CPU
	X4net.add(CNode(U1,'PA15/JTDI'))


	# Pin 26 X5 - 35 RD5 GPIO
	X5net = CNet("X5")
	sch.addNet(X5net)
	X5net.add(CNode(MOD1,'X5'))
	# CPU
	X5net.add(CNode(U1,'PB3/JTDO/TRACESWO'))

	# Pin 27 X6 - 36 RD6 GPIO
	X6net = CNet("X6")
	sch.addNet(X6net)
	X6net.add(CNode(MOD1,'X6'))
	# CPU
	#X6net.add(CNode(U1,'PA13/JTMS/SWDIO'))
	X6net.add(CNode(U1,'PB4/JNTRST'))

	# Pin 28 X7 - 37 RD7 GPIO
	X7net = CNet("X7")
	sch.addNet(X7net)
	X7net.add(CNode(MOD1,'X7'))
	# CPU
	#X7net.add(CNode(U1,'PA14/JTCK/SWCLK'))
	X7net.add(CNode(U1,'PB5/I2C1_SMBAl'))

	# Pin 29 X8 - 38 RE0 GPIO
	X8net = CNet("X8")
	sch.addNet(X8net)
	X8net.add(CNode(MOD1,'X8'))
	# CPU
	#X8net.add(CNode(U1,'PA15/JTDI'))
	X8net.add(CNode(U1,'PB6/I2C1_SCL/TIM4_CH1'))

	# Pin 30 X9 - 39 RE1 GPIO
	X9net = CNet("X9")
	sch.addNet(X9net)
	X9net.add(CNode(MOD1,'X9'))
	# CPU
	#X9net.add(CNode(U1,'PB3/JTDO/TRACESWO'))
	X9net.add(CNode(U1,'PB7/I2C1_SDA/TIM4_CH2'))

	# Pin 31 X10 - 40 RE2 GPIO
	X10net = CNet("X10")
	sch.addNet(X10net)
	X10net.add(CNode(MOD1,'X10'))
	# CPU
	#X10net.add(CNode(U1,'PB4/JNTRST'))
	# CPU boot pin control, 0 - User Flash 1 - System Memory as long as BOOT2 is tied low
	X10net.add(CNode(U1,'BOOT0'))

	# Pin 32 X11 - 41 RE3 GPIO
	X11net = CNet("X11")
	sch.addNet(X11net)
	X11net.add(CNode(MOD1,'X11'))
	# CPU
	#X11net.add(CNode(U1,'PB5/I2C1_SMBAl'))
	X11net.add(CNode(U1,'PB8/TIM4_CH3'))

	# Pin 33 X12 - 42 RE4 GPIO
	X12net = CNet("X12")
	sch.addNet(X12net)
	X12net.add(CNode(MOD1,'X12'))
	# CPU
	#X12net.add(CNode(U1,'PB6/I2C1_SCL/TIM4_CH1'))
	X12net.add(CNode(U1,'PB9/TIM4_CH4'))


	# Pin 34 X13 - 43 RE5 GPIO
	X13net = CNet("X13")
	sch.addNet(X13net)
	X13net.add(CNode(MOD1,'X13'))
	# CPU
	#X13net.add(CNode(U1,'PB7/I2C1_SDA/TIM4_CH2'))
	X13net.add(CNode(U1,'PC13-ANTI_TAMP'))

	# Pin 35 X14 - 44 RE6 GPIO
	X14net = CNet("X14")
	sch.addNet(X14net)
	X14net.add(CNode(MOD1,'X14'))
	# CPU
	#X14net.add(CNode(U1,'PB8/TIM4_CH3'))
	X14net.add(CNode(U1,'PC14-OSC32_IN'))


	# Pin 36 X15 - 45 RE7 GPIO
	X15net = CNet("X15")
	sch.addNet(X15net)
	X15net.add(CNode(MOD1,'X15'))
	# CPU
	#X15net.add(CNode(U1,'PB9/TIM4_CH4'))
	X15net.add(CNode(U1,'PC15-OSC32_OUT'))

	# Pin 37 VDD
	# VDD3V3net
	VDD3V3net.add(CNode(MOD1,'VDD'))

	# Pin 38 RES#
	# Reset
	RESETnet = CNet("RESET#")
	sch.addNet(RESETnet)
	RESETnet.add(CNode(MOD1,'RESET#'))
	# CPU
	RESETnet.add(CNode(U1,'NRST'))
	# Reset circuit C30 and R30
	RESETnet.add(CNode(C30,'2'))
	RESETnet.add(CNode(R30,'1'))
	# Reset Interface - Collector Q2
	RESETnet.add(CNode(U6, 'CQ1'))

	# Pin 39 VSS_2
	# Ground GND
	GNDnet.add(CNode(MOD1,'VSS_2'))

	# Pin 40 VIN
	# VDD12Vnet
	VDD12Vnet.add(CNode(MOD1,'VIN'))
	# LDO
	VDD12Vnet.add(CNode(U2,'IN'))



	# SWD Connector
	# 1 - GND
	# 2 - VCC
	# 3 - PA14 - "PA14/JTCK/SWCLK"
	# 4 - # RESET
	# 5 - PA13 - "PA13/JTMS/SWDIO" pull-up 100k on the board recommended by ARM
	# 6 - PB3  - "PB3/JTDO/TRACESWO"

	SWDCON=SW_DEBUG_CON("SWDCON","","SW_DEBUG_CON",LibName,"SWDCON")
	sch.addDev(SWDCON)
	sch.addSymbolFromDev(SWDCON, 2, "SWDCON")
	# 1 - GND
	GNDnet.add(CNode(SWDCON, 'GND'))
	# 2 - VCC
	VDD3V3net.add(CNode(SWDCON, 'VCC'))
	# 3- PA14 - "PA14/JTCK/SWCLK"
	X3net.add(CNode(SWDCON,'SWCLK'))
	# 4 - RESET#
	RESETnet.add(CNode(SWDCON,'RESET#'))
	# 5 - PA13 - "PA13/JTMS/SWDIO"
	X2net.add(CNode(SWDCON,'SWDIO'))
	# 6 - PB3  - "PB3/JTDO/TRACESWO"
	X5net.add(CNode(SWDCON, 'TRACESWO'))
	

def make(dname="stm32dip40", lname="stm32dip40"):
    	# Schematic
	DesignName = dname
	LibName = lname

	# Create schematic
	sch = CSchematic()
	# Simple rectangle
	sizex = 7.0
	sizey = 6.0
	sch.outline.append(Point(0,0))
	sch.outline.append(Point(inch2sch(sizex),0))
	sch.outline.append(Point(inch2sch(sizex),inch2sch(sizey)))
	sch.outline.append(Point(0,inch2sch(sizey)))
	sch.bbox=Rectangle(0, 0, inch2sch(sizex), inch2sch(sizey)) # shoul be calculated automatically

	gen_schematic(sch, DesignName, LibName)

	return sch

if __name__ == "__main__":
	sch = make('stm32dip40', 'stm32dip40')
    
