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
		
class STM3210X(Component):
	"STM3210x 48 pin"
	def __init__(self, refid, val, name="stm3210x", libname="stm32", symbolname="stm3210x", packagename="LQFP48"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = LQFP48()
		self.parsePackage()
		self.addPin( CPin("VBAT", 										1	))
		self.addPin( CPin("PC13-ANTI_TAMP", 							2	))
		self.addPin( CPin("PC14-OSC32_IN", 								3	))
		self.addPin( CPin("PC15-OSC32_OUT", 							4	))
		self.addPin( CPin("OSC_IN", 									5	))
		self.addPin( CPin("OSC_OUT", 									6	))
		self.addPin( CPin("NRST", 										7	))
		self.addPin( CPin("VSSA", 										8	))
		self.addPin( CPin("VDDA", 										9	))
		self.addPin( CPin("PA0-WKUP/USART2_CTS/ADC_IN0/TIM2_CH1_ETR",	10	))
		self.addPin( CPin("PA1/USART2_RTS/ADC_IN1/TIM2_CH2", 			11	))
		self.addPin( CPin("PA2/USART2_TX/ADC_IN2/TIM2_CH3", 			12	))
		self.addPin( CPin("PA3/USART2_RX/ADC_IN3/TIM2_CH4", 			13	))
		self.addPin( CPin("PA4/SPI1_NSS/USART2_CK/ADC_IN4", 			14	))
		self.addPin( CPin("PA5/SPI1_SCK/ADC_IN5", 						15	))
		self.addPin( CPin("PA6/SPI1_MISO/ADC_IN6/TIM3_CH1", 			16	))
		self.addPin( CPin("PA7/SPI1_MOSI/ADC_IN7/TIM3_CH2", 			17	))
		self.addPin( CPin("PB0/ADC_IN8/TIM3_CH3", 						18	))
		self.addPin( CPin("PB1/ADC_IN9/TIM3_CH4", 						19	))
		self.addPin( CPin("PB2/BOOT1", 									20	))
		self.addPin( CPin("PB10/I2C2_SCL/USART3_TX",					21	))
		self.addPin( CPin("PB11/I2C2_SDA/USART3_RX", 					22	))
		self.addPin( CPin("VSS_1", 										23	))
		self.addPin( CPin("VDD_1", 										24	))
		self.addPin( CPin("PB12/SPI2_NSS/I2C2_SMBAl/USART3_CK", 		25	))
		self.addPin( CPin("PB13/SPI2_SCK/USART3_CTS", 					26	))
		self.addPin( CPin("PB14/SPI2_MISO/USART3_RTS", 					27	))
		self.addPin( CPin("PB15/SPI2_MOSI", 							28	))
		self.addPin( CPin("PA8/USART1_CK/MCO", 							29	))
		self.addPin( CPin("PA9/USART1_TX", 								30	))
		self.addPin( CPin("PA10/USART1_RX",	 							31	))
		self.addPin( CPin("PA11/USART1_CTS", 							32	))
		self.addPin( CPin("PA12/USART1_RTS", 							33	))
		self.addPin( CPin("PA13/JTMS/SWDIO", 							34	))
		self.addPin( CPin("VSS_2",										35	))
		self.addPin( CPin("VDD_2", 										36	))
		self.addPin( CPin("PA14/JTCK/SWCLK", 							37	))
		self.addPin( CPin("PA15/JTDI", 									38	))
		self.addPin( CPin("PB3/JTDO/TRACESWO", 							39	))
		self.addPin( CPin("PB4/JNTRST", 								40	))
		self.addPin( CPin("PB5/I2C1_SMBAl", 							41	))
		self.addPin( CPin("PB6/I2C1_SCL/TIM4_CH1",	 					42	))
		self.addPin( CPin("PB7/I2C1_SDA/TIM4_CH2", 						43	))
		self.addPin( CPin("BOOT0", 										44	))
		self.addPin( CPin("PB8/TIM4_CH3", 								45	))
		self.addPin( CPin("PB9/TIM4_CH4", 								46	))
		self.addPin( CPin("VSS_3", 										47	))
		self.addPin( CPin("VDD_3", 										48	))
		

class STM32F10X_64(Component):
	"STM32F10x 64 pin"
	def __init__(self, refid, val, name="stm321f0x_64", libname="stm32", symbolname="stm32f10x_64", packagename="LQFP64"):
		Component.__init__(self, refid, val, name, libname, symbolname, packagename)
		self.package = LQFP64()
		self.parsePackage()
		self.addPin( CPin("VBAT", 										1	))
		self.addPin( CPin("PC13-TAMPER-RTC", 							2	))
		self.addPin( CPin("PC14-OSC32_IN", 								3	))
		self.addPin( CPin("PC15-OSC32_OUT", 							4	))
		self.addPin( CPin("OSC_IN", 									5	))
		self.addPin( CPin("OSC_OUT", 									6	))
		self.addPin( CPin("NRST", 										7	))
		self.addPin( CPin("PC0/ADC12_IN10", 							8	))
		self.addPin( CPin("PC0/ADC12_IN11", 							9	))
		self.addPin( CPin("PC0/ADC12_IN12", 							10	))
		self.addPin( CPin("PC0/ADC12_IN13", 							11	))
		self.addPin( CPin("VSSA", 										12	))
		self.addPin( CPin("VDDA", 										13	))
		self.addPin( CPin("PA0-WKUP/USART2_CTS/ADC_IN0/TIM2_CH1_ETR",	14	))
		self.addPin( CPin("PA1/USART2_RTS/ADC12_IN1/TIM2_CH2", 			15	))
		self.addPin( CPin("PA2/USART2_TX/ADC12_IN2/TIM2_CH3", 			16	))
		self.addPin( CPin("PA3/USART2_RX/ADC12_IN3/TIM2_CH4", 			17	))
		self.addPin( CPin("VSS_4", 										18	))
		self.addPin( CPin("VDD_4", 										19	))
		self.addPin( CPin("PA4/SPI1_NSS/USART2_CK/ADC12_IN4", 			20	))
		self.addPin( CPin("PA5/SPI1_SCK/ADC12_IN5", 					21	))
		self.addPin( CPin("PA6/SPI1_MISO/ADC12_IN6/TIM3_CH1", 			22	))
		self.addPin( CPin("PA7/SPI1_MOSI/ADC12_IN7/TIM3_CH2", 			23	))
		self.addPin( CPin("PC4/ADC12_IN14", 							24	))
		self.addPin( CPin("PC5/ADC12_IN15", 							25	))
		self.addPin( CPin("PB0/ADC12_IN8/TIM3_CH3", 					26	))
		self.addPin( CPin("PB1/ADC12_IN9/TIM3_CH4", 					27	))
		self.addPin( CPin("PB2/BOOT1", 									28	))
		self.addPin( CPin("PB10/I2C2_SCL/USART3_TX",					29	))
		self.addPin( CPin("PB11/I2C2_SDA/USART3_RX", 					30	))
		self.addPin( CPin("VSS_1", 										31	))
		self.addPin( CPin("VDD_1", 										32	))
		self.addPin( CPin("PB12/SPI2_NSS/I2C2_SMBAl/USART3_CK/TIM1_BKIN", 		33	))
		self.addPin( CPin("PB13/SPI2_SCK/USART3_CTS/TIM1_CH1N", 		34	))
		self.addPin( CPin("PB14/SPI2_MISO/USART3_RTS/TIM1_CH2N", 		35	))
		self.addPin( CPin("PB15/SPI2_MOSI/TIM1_CH3N", 					36	))
		self.addPin( CPin("PC6",			 							37	))
		self.addPin( CPin("PC7",			 							38	))
		self.addPin( CPin("PC8",			 							39	))
		self.addPin( CPin("PC9",			 							40	))
		self.addPin( CPin("PA8/USART1_CK/TIM1_CH1/MCO", 				41	))
		self.addPin( CPin("PA9/USART1_TX/TIM1_CH2", 					42	))
		self.addPin( CPin("PA10/USART1_RX/TIM1_CH3",	 				43	))
		self.addPin( CPin("PA11/USART1_CTS/CANRX/TIM1_CH4/USBDM", 		44	))
		self.addPin( CPin("PA12/USART1_RTS/CANTX/TIM1_ETR/USBDP", 		45	))
		self.addPin( CPin("PA13/JTMS/SWDIO", 							46	))
		self.addPin( CPin("VSS_2",										47	))
		self.addPin( CPin("VDD_2", 										48	))
		self.addPin( CPin("PA14/JTCK/SWCLK", 							49	))
		self.addPin( CPin("PA15/JTDI", 									50	))
		self.addPin( CPin("PC10",			 							51	))
		self.addPin( CPin("PC11",			 							52	))
		self.addPin( CPin("PC12",			 							53	))
		self.addPin( CPin("PD2/TIM3_ETR",			 					54	))
		self.addPin( CPin("PB3/JTDO/TRACESWO", 							55	))
		self.addPin( CPin("PB4/JNTRST", 								56	))
		self.addPin( CPin("PB5/I2C1_SMBAl", 							57	))
		self.addPin( CPin("PB6/I2C1_SCL/TIM4_CH1",	 					58	))
		self.addPin( CPin("PB7/I2C1_SDA/TIM4_CH2", 						59	))
		self.addPin( CPin("BOOT0", 										60	))
		self.addPin( CPin("PB8/TIM4_CH3", 								61	))
		self.addPin( CPin("PB9/TIM4_CH4", 								62	))
		self.addPin( CPin("VSS_3", 										63	))
		self.addPin( CPin("VDD_3", 										64	))
				
# Some tests
if __name__ == "__main__":
	stm3210 = STM3210X("U1","","STM32101")
	print stm3210


