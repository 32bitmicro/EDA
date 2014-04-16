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

from edautils import *
from eda import *

pcb_symbols= """
Symbol(' ' 18)
(
)
Symbol('!' 12)
(
	SymbolLine(0 35 0 40 8)
	SymbolLine(0 0 0 25 8)
)
Symbol('"' 12)
(
	SymbolLine(0 0 0 10 8)
	SymbolLine(10 0 10 10 8)
)
Symbol('#' 12)
(
	SymbolLine(0 25 20 25 8)
	SymbolLine(0 15 20 15 8)
	SymbolLine(15 10 15 30 8)
	SymbolLine(5 10 5 30 8)
)
Symbol('$' 12)
(
	SymbolLine(15 5 20 10 8)
	SymbolLine(5 5 15 5 8)
	SymbolLine(0 10 5 5 8)
	SymbolLine(0 10 0 15 8)
	SymbolLine(0 15 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 30 8)
	SymbolLine(15 35 20 30 8)
	SymbolLine(5 35 15 35 8)
	SymbolLine(0 30 5 35 8)
	SymbolLine(10 0 10 40 8)
)
Symbol('%' 12)
(
	SymbolLine(0 5 0 10 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 10 0 8)
	SymbolLine(10 0 15 5 8)
	SymbolLine(15 5 15 10 8)
	SymbolLine(10 15 15 10 8)
	SymbolLine(5 15 10 15 8)
	SymbolLine(0 10 5 15 8)
	SymbolLine(0 40 40 0 8)
	SymbolLine(35 40 40 35 8)
	SymbolLine(40 30 40 35 8)
	SymbolLine(35 25 40 30 8)
	SymbolLine(30 25 35 25 8)
	SymbolLine(25 30 30 25 8)
	SymbolLine(25 30 25 35 8)
	SymbolLine(25 35 30 40 8)
	SymbolLine(30 40 35 40 8)
)
Symbol('&' 12)
(
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 5 0 15 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 25 15 10 8)
	SymbolLine(5 40 10 40 8)
	SymbolLine(10 40 20 30 8)
	SymbolLine(0 15 25 40 8)
	SymbolLine(5 0 10 0 8)
	SymbolLine(10 0 15 5 8)
	SymbolLine(15 5 15 10 8)
	SymbolLine(0 25 0 35 8)
)
Symbol(''' 12)
(
	SymbolLine(0 10 10 0 8)
)
Symbol('(' 12)
(
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 5 0 35 8)
)
Symbol(')' 12)
(
	SymbolLine(0 0 5 5 8)
	SymbolLine(5 5 5 35 8)
	SymbolLine(0 40 5 35 8)
)
Symbol('*' 12)
(
	SymbolLine(0 10 20 30 8)
	SymbolLine(0 30 20 10 8)
	SymbolLine(0 20 20 20 8)
	SymbolLine(10 10 10 30 8)
)
Symbol('+' 12)
(
	SymbolLine(0 20 20 20 8)
	SymbolLine(10 10 10 30 8)
)
Symbol(',' 12)
(
	SymbolLine(0 50 10 40 8)
)
Symbol('-' 12)
(
	SymbolLine(0 20 20 20 8)
)
Symbol('.' 12)
(
	SymbolLine(0 40 5 40 8)
)
Symbol('/' 12)
(
	SymbolLine(0 35 30 5 8)
)
Symbol('0' 12)
(
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 30 20 10 8)
)
Symbol('1' 12)
(
	SymbolLine(5 40 15 40 8)
	SymbolLine(10 0 10 40 8)
	SymbolLine(0 10 10 0 8)
)
Symbol('2' 12)
(
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 20 0 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 15 8)
	SymbolLine(0 40 25 15 8)
	SymbolLine(0 40 25 40 8)
)
Symbol('3' 12)
(
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 20 20 20 8)
)
Symbol('4' 12)
(
	SymbolLine(0 20 20 0 8)
	SymbolLine(0 20 25 20 8)
	SymbolLine(20 0 20 40 8)
)
Symbol('5' 12)
(
	SymbolLine(0 0 20 0 8)
	SymbolLine(0 0 0 20 8)
	SymbolLine(0 20 5 15 8)
	SymbolLine(5 15 15 15 8)
	SymbolLine(15 15 20 20 8)
	SymbolLine(20 20 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('6' 12)
(
	SymbolLine(15 0 20 5 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(0 20 15 20 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(20 25 20 35 8)
)
Symbol('7' 12)
(
	SymbolLine(0 40 25 15 8)
	SymbolLine(25 0 25 15 8)
	SymbolLine(0 0 25 0 8)
)
Symbol('8' 12)
(
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 15 5 20 8)
	SymbolLine(0 5 0 15 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 15 8)
	SymbolLine(15 20 20 15 8)
)
Symbol('9' 12)
(
	SymbolLine(0 40 20 20 8)
	SymbolLine(20 5 20 20 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 5 0 15 8)
	SymbolLine(0 15 5 20 8)
	SymbolLine(5 20 20 20 8)
)
Symbol(':' 12)
(
	SymbolLine(0 15 5 15 8)
	SymbolLine(0 25 5 25 8)
)
Symbol(';' 12)
(
	SymbolLine(0 40 10 30 8)
	SymbolLine(10 15 10 20 8)
)
Symbol('<' 12)
(
	SymbolLine(0 20 10 10 8)
	SymbolLine(0 20 10 30 8)
)
Symbol('=' 12)
(
	SymbolLine(0 15 20 15 8)
	SymbolLine(0 25 20 25 8)
)
Symbol('>' 12)
(
	SymbolLine(0 10 10 20 8)
	SymbolLine(0 30 10 20 8)
)
Symbol('?' 12)
(
	SymbolLine(10 20 10 25 8)
	SymbolLine(10 35 10 40 8)
	SymbolLine(0 5 0 10 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 10 8)
	SymbolLine(10 20 20 10 8)
)
Symbol('A' 12)
(
	SymbolLine(0 5 0 40 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 20 0 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 40 8)
	SymbolLine(0 20 25 20 8)
)
Symbol('B' 12)
(
	SymbolLine(0 40 20 40 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(25 25 25 35 8)
	SymbolLine(20 20 25 25 8)
	SymbolLine(5 20 20 20 8)
	SymbolLine(5 0 5 40 8)
	SymbolLine(0 0 20 0 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 15 8)
	SymbolLine(20 20 25 15 8)
)
Symbol('C' 12)
(
	SymbolLine(5 40 20 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 20 0 8)
)
Symbol('D' 12)
(
	SymbolLine(5 0 5 40 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 35 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(0 40 20 40 8)
	SymbolLine(0 0 20 0 8)
)
Symbol('E' 12)
(
	SymbolLine(0 20 15 20 8)
	SymbolLine(0 40 20 40 8)
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 0 20 0 8)
)
Symbol('F' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 0 20 0 8)
	SymbolLine(0 20 15 20 8)
)
Symbol('G' 12)
(
	SymbolLine(20 0 25 5 8)
	SymbolLine(5 0 20 0 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 20 40 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(25 25 25 35 8)
	SymbolLine(20 20 25 25 8)
	SymbolLine(10 20 20 20 8)
)
Symbol('H' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(25 0 25 40 8)
	SymbolLine(0 20 25 20 8)
)
Symbol('I' 12)
(
	SymbolLine(0 0 10 0 8)
	SymbolLine(5 0 5 40 8)
	SymbolLine(0 40 10 40 8)
)
Symbol('J' 12)
(
	SymbolLine(0 0 15 0 8)
	SymbolLine(15 0 15 35 8)
	SymbolLine(10 40 15 35 8)
	SymbolLine(5 40 10 40 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('K' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 20 20 0 8)
	SymbolLine(0 20 20 40 8)
)
Symbol('L' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 40 20 40 8)
)
Symbol('M' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 0 15 15 8)
	SymbolLine(15 15 30 0 8)
	SymbolLine(30 0 30 40 8)
)
Symbol('N' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 0 0 5 8)
	SymbolLine(0 5 25 30 8)
	SymbolLine(25 0 25 40 8)
)
Symbol('O' 12)
(
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('P' 12)
(
	SymbolLine(5 0 5 40 8)
	SymbolLine(0 0 20 0 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 15 8)
	SymbolLine(20 20 25 15 8)
	SymbolLine(5 20 20 20 8)
)
Symbol('Q' 12)
(
	SymbolLine(0 5 0 35 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 15 0 8)
	SymbolLine(15 0 20 5 8)
	SymbolLine(20 5 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(10 30 20 40 8)
)
Symbol('R' 12)
(
	SymbolLine(0 0 20 0 8)
	SymbolLine(20 0 25 5 8)
	SymbolLine(25 5 25 15 8)
	SymbolLine(20 20 25 15 8)
	SymbolLine(5 20 20 20 8)
	SymbolLine(5 0 5 40 8)
	SymbolLine(5 20 25 40 8)
)
Symbol('S' 12)
(
	SymbolLine(20 0 25 5 8)
	SymbolLine(5 0 20 0 8)
	SymbolLine(0 5 5 0 8)
	SymbolLine(0 5 0 15 8)
	SymbolLine(0 15 5 20 8)
	SymbolLine(5 20 20 20 8)
	SymbolLine(20 20 25 25 8)
	SymbolLine(25 25 25 35 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(5 40 20 40 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('T' 12)
(
	SymbolLine(0 0 20 0 8)
	SymbolLine(10 0 10 40 8)
)
Symbol('U' 12)
(
	SymbolLine(0 0 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(20 0 20 35 8)
)
Symbol('V' 12)
(
	SymbolLine(0 0 0 30 8)
	SymbolLine(0 30 10 40 8)
	SymbolLine(10 40 20 30 8)
	SymbolLine(20 0 20 30 8)
)
Symbol('W' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 40 15 25 8)
	SymbolLine(15 25 30 40 8)
	SymbolLine(30 0 30 40 8)
)
Symbol('X' 12)
(
	SymbolLine(0 0 0 5 8)
	SymbolLine(0 5 25 30 8)
	SymbolLine(25 30 25 40 8)
	SymbolLine(0 30 0 40 8)
	SymbolLine(0 30 25 5 8)
	SymbolLine(25 0 25 5 8)
)
Symbol('Y' 12)
(
	SymbolLine(0 0 0 5 8)
	SymbolLine(0 5 10 15 8)
	SymbolLine(10 15 20 5 8)
	SymbolLine(20 0 20 5 8)
	SymbolLine(10 15 10 40 8)
)
Symbol('Z' 12)
(
	SymbolLine(0 0 25 0 8)
	SymbolLine(25 0 25 5 8)
	SymbolLine(0 30 25 5 8)
	SymbolLine(0 30 0 40 8)
	SymbolLine(0 40 25 40 8)
)
Symbol('[' 12)
(
	SymbolLine(0 0 5 0 8)
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 40 5 40 8)
)
Symbol('\' 12)
(
	SymbolLine(0 5 30 35 8)
)
Symbol(']' 12)
(
	SymbolLine(0 0 5 0 8)
	SymbolLine(5 0 5 40 8)
	SymbolLine(0 40 5 40 8)
)
Symbol('^' 12)
(
	SymbolLine(0 5 5 0 8)
	SymbolLine(5 0 10 5 8)
)
Symbol('_' 12)
(
	SymbolLine(0 40 20 40 8)
)
Symbol('a' 12)
(
	SymbolLine(15 20 20 25 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(20 20 20 35 8)
	SymbolLine(20 35 25 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
)
Symbol('b' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(20 25 20 35 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(0 25 5 20 8)
)
Symbol('c' 12)
(
	SymbolLine(5 20 20 20 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 20 40 8)
)
Symbol('d' 12)
(
	SymbolLine(20 0 20 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
)
Symbol('e' 12)
(
	SymbolLine(5 40 20 40 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(0 30 20 30 8)
	SymbolLine(20 30 20 25 8)
)
Symbol('f' 10)
(
	SymbolLine(5 5 5 40 8)
	SymbolLine(5 5 10 0 8)
	SymbolLine(10 0 15 0 8)
	SymbolLine(0 20 10 20 8)
)
Symbol('g' 12)
(
	SymbolLine(15 20 20 25 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(0 50 5 55 8)
	SymbolLine(5 55 15 55 8)
	SymbolLine(15 55 20 50 8)
	SymbolLine(20 20 20 50 8)
)
Symbol('h' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 40 8)
)
Symbol('i' 10)
(
	SymbolLine(0 10 0 15 8)
	SymbolLine(0 25 0 40 8)
)
Symbol('j' 10)
(
	SymbolLine(5 10 5 15 8)
	SymbolLine(5 25 5 50 8)
	SymbolLine(0 55 5 50 8)
)
Symbol('k' 12)
(
	SymbolLine(0 0 0 40 8)
	SymbolLine(0 25 15 40 8)
	SymbolLine(0 25 10 15 8)
)
Symbol('l' 10)
(
	SymbolLine(0 0 0 35 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('m' 12)
(
	SymbolLine(5 25 5 40 8)
	SymbolLine(5 25 10 20 8)
	SymbolLine(10 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 40 8)
	SymbolLine(20 25 25 20 8)
	SymbolLine(25 20 30 20 8)
	SymbolLine(30 20 35 25 8)
	SymbolLine(35 25 35 40 8)
	SymbolLine(0 20 5 25 8)
)
Symbol('n' 12)
(
	SymbolLine(5 25 5 40 8)
	SymbolLine(5 25 10 20 8)
	SymbolLine(10 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 40 8)
	SymbolLine(0 20 5 25 8)
)
Symbol('o' 12)
(
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(20 25 20 35 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('p' 12)
(
	SymbolLine(5 25 5 55 8)
	SymbolLine(0 20 5 25 8)
	SymbolLine(5 25 10 20 8)
	SymbolLine(10 20 20 20 8)
	SymbolLine(20 20 25 25 8)
	SymbolLine(25 25 25 35 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(10 40 20 40 8)
	SymbolLine(5 35 10 40 8)
)
Symbol('q' 12)
(
	SymbolLine(20 25 20 55 8)
	SymbolLine(15 20 20 25 8)
	SymbolLine(5 20 15 20 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(0 25 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
)
Symbol('r' 12)
(
	SymbolLine(5 25 5 40 8)
	SymbolLine(5 25 10 20 8)
	SymbolLine(10 20 20 20 8)
	SymbolLine(0 20 5 25 8)
)
Symbol('s' 12)
(
	SymbolLine(5 40 20 40 8)
	SymbolLine(20 40 25 35 8)
	SymbolLine(20 30 25 35 8)
	SymbolLine(5 30 20 30 8)
	SymbolLine(0 25 5 30 8)
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 20 20 8)
	SymbolLine(20 20 25 25 8)
	SymbolLine(0 35 5 40 8)
)
Symbol('t' 10)
(
	SymbolLine(5 0 5 35 8)
	SymbolLine(5 35 10 40 8)
	SymbolLine(0 15 10 15 8)
)
Symbol('u' 12)
(
	SymbolLine(0 20 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
	SymbolLine(20 20 20 35 8)
)
Symbol('v' 12)
(
	SymbolLine(0 20 0 30 8)
	SymbolLine(0 30 10 40 8)
	SymbolLine(10 40 20 30 8)
	SymbolLine(20 20 20 30 8)
)
Symbol('w' 12)
(
	SymbolLine(0 20 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(5 40 10 40 8)
	SymbolLine(10 40 15 35 8)
	SymbolLine(15 20 15 35 8)
	SymbolLine(15 35 20 40 8)
	SymbolLine(20 40 25 40 8)
	SymbolLine(25 40 30 35 8)
	SymbolLine(30 20 30 35 8)
)
Symbol('x' 12)
(
	SymbolLine(0 20 20 40 8)
	SymbolLine(0 40 20 20 8)
)
Symbol('y' 12)
(
	SymbolLine(0 20 0 35 8)
	SymbolLine(0 35 5 40 8)
	SymbolLine(20 20 20 50 8)
	SymbolLine(15 55 20 50 8)
	SymbolLine(5 55 15 55 8)
	SymbolLine(0 50 5 55 8)
	SymbolLine(5 40 15 40 8)
	SymbolLine(15 40 20 35 8)
)
Symbol('z' 12)
(
	SymbolLine(0 20 20 20 8)
	SymbolLine(0 40 20 20 8)
	SymbolLine(0 40 20 40 8)
)
Symbol('{' 12)
(
	SymbolLine(5 5 10 0 8)
	SymbolLine(5 5 5 15 8)
	SymbolLine(0 20 5 15 8)
	SymbolLine(0 20 5 25 8)
	SymbolLine(5 25 5 35 8)
	SymbolLine(5 35 10 40 8)
)
Symbol('|' 12)
(
	SymbolLine(0 0 0 40 8)
)
Symbol('}' 12)
(
	SymbolLine(0 0 5 5 8)
	SymbolLine(5 5 5 15 8)
	SymbolLine(5 15 10 20 8)
	SymbolLine(5 25 10 20 8)
	SymbolLine(5 25 5 35 8)
	SymbolLine(0 40 5 35 8)
)
Symbol('~' 12)
(
	SymbolLine(0 25 5 20 8)
	SymbolLine(5 20 10 20 8)
	SymbolLine(10 20 15 25 8)
	SymbolLine(15 25 20 25 8)
	SymbolLine(20 25 25 20 8)
)
"""

pcb_layers = """
Layer(1 "solder")
(
)
Layer(2 "component")
(
)
Layer(3 "GND")
(
)
Layer(4 "power")
(
)
Layer(5 "signal1")
(
)
Layer(6 "signal2")
(
)
Layer(7 "unused")
(
)
Layer(8 "unused")
(
)
Layer(9 "silk")
(
)
Layer(10 "silk")
(
)
"""

class CPCB:
	" PCB class "
	def __init__(self, sch=None,brd=None):
		self.name=""
		self.sch=sch
		self.brd=brd
		self.script_path=""


	def addLayers(self):
# These layers have to be added in the board
#		self.brd.addLayer(CLayer("solder",1))			# bottom orientation
#		self.brd.addLayer(CLayer("component",2))
# these layers are already added
##		self.brd.addLayer(CLayer("GND",3))
##		self.brd.addLayer(CLayer("VCC",4))
##		self.brd.addLayer(CLayer("blksolder",5))		# bottom orientation
##		self.brd.addLayer(CLayer("blkcomponent",6))
##		self.brd.addLayer(CLayer("signal3",7))
##		self.brd.addLayer(CLayer("signal4",8))
##		self.brd.addLayer(CLayer("Vias",9))
##		self.brd.addLayer(CLayer("silk",10))
		pass
#Layer(1 "solder")
#(
#	Line(1375 1075 1325 1025 40 30 0x00000020)
#)

	# gen sch layers scr"
	def genSchLayersScr(self):
		ns = ''
		CRLF = "\n"
	
		ns = pcb_layers;

		return ns;



#ADD 'C1' 'G$1' POLARISED_CASE_H@ipc-7351-capacitor R0.000 (-0.300 3.300);
#ADD 'Q1' 'G$1' -PNP-SOT23-EBC@transistor R0.000 (1.600 3.300);
#ADD 'Q5' 'G$1' MMBT2222ALT1-NPN-SOT23-BEC@transistor R0.000 (0.900 2.800);
#ADD 'V1' 'GND' GND@supply2 R0.000 (0.600 0.100);
#ADD 'V2' 'G$1' VCC@supply2 R0.000 (5.600 4.200);



	# gen sch add scr"
	def genSchAddScr(self):
		ns = ''
		CRLF = "\n"
		ns += "GRID INCH 0.005" + CRLF
		ns += "Layer (91 Nets;" + CRLF
		ns += "Layer (92 Busses;" + CRLF
		ns += "Layer (93 Pins;" + CRLF
		ns += "Layer (94 Symbols;" + CRLF
		ns += "Layer (95 Names;" + CRLF
		ns += "Layer (96 Values;" + CRLF
		ns += "Layer (250 Descript;" + CRLF
		ns += "Layer (251 SMDround;" + CRLF
		ns += "DISPLAY -PINS" + CRLF
		ns += CRLF
		ns += "EDIT .S1" + CRLF
		ns += "SET WIRE_BEND 2;" + CRLF
		ns += "CHANGE STYLE 'Continuous'" + CRLF
		
		for dev in self.sch.devices:
			ns += "ADD '" + str(dev.refid) + "' 'G$1' " + str(dev.name) + "@" + str(dev.libname) + " " + dev.orientation + "R%.3f"% (dev.rotation) +" (" + str(dev.position) + ");" + CRLF   
			
		ns += "GRID LAST" + CRLF
		
		return ns
		
	# gen cmd sch net-connect"
	def genSchNetConnectScr(self):
		ns = ''
		CRLF = "\n"
		runcmd="run " + self.script_path + "/sch-net-connect.ulp"
		
		for net in self.sch.nets.values:	
			prevdev=""
			prevpin=""
			l = ""
			first = 1
			for node in net.nodes:
				if first:
					first = 0
					prevdev=str(node.dev.refid)
					prevpin=str(node.pin)
				else:
					l = runcmd +  " " + net.name + " " + prevdev + " " + prevpin + " " + str(node.dev.refid) + " " + str(node.pin) + ";" + CRLF
					ns += l	
					prevdev=str(node.dev.refid)
					prevpin=str(node.pin)
					
		# string function
		return ns
	
	# gen sch netlist listing
	def genSchNetlistLst(self):
		ns = ''
		CRLF = '\n'
		for net in self.sch.nets.values():
			name = net.name
			
			ns += net.name + ' '
			for node in net.nodes:
				ns += str(node.dev.refid) + '-' + str(node.pin.num) + ' '
			ns += CRLF
		ns += CRLF	#extra one
		# string function
		return ns
	
	
	# gen sch netlist script
	def genSchNetlistScr(self):
		ns = ''
		CRLF = "\n"
		ns = "# Netlist script" + CRLF
		ns += "# EAGLE Version 4.11" + CRLF
		ns += "# Copyright Hobby-Robotics" + CRLF
		ns += expandtab("#Net\tPart\tPad",12) + CRLF
		ns += CRLF
		for net in self.sch.nets.values():
			ns += CRLF
			ns += "Change Class 0;" + CRLF
			l = "Signal " + " '" + net.name + "'"
			first = 1
			for node in net.nodes:
				if first:
					first = 0
					l += "\t'"
				else:
					l += "\t\t"
					
				l += str(node.dev.refid) + "'\t'" + str(node.pin) + "' \\" + CRLF
					
			ns += expandtab(str(l),12)
			ns += "\t\t\t;" + CRLF
		# string function
		return ns
		

# Select
# {"All objects" Select(ObjectByName) ActiveWhen(have_regex)}
# {"Elements" Select(ElementByName) ActiveWhen(have_regex)}
# {"Pads" Select(PadByName) ActiveWhen(have_regex)}
# {"Pins" Select(PinByName) ActiveWhen(have_regex)}
# {"Text" Select(TextByName) ActiveWhen(have_regex)}
# {"Vias" Select(ViaByName) ActiveWhen(have_regex)}
# Move
# {"Move selected elements to other side" Flip(SelectedElements) a={"Shift-B" "Shift<Key>b"}}
#   {"Remove selected objects" RemoveSelected()}


#  {Connects m=C
#   {"Lookup connection to object" GetXY(Select the object) Connection(Find) a={"Ctrl-F" "Ctrl<Key>f"}}
#   {"Reset scanned pads/pins/vias" Connection(ResetPinsViasAndPads) Display(Redraw)}
#   {"Reset scanned lines/polygons" Connection(ResetLinesAndPolygons) Display(Redraw)}
#   {"Reset all connections" Connection(Reset) Display(Redraw) a={"Shift-F" "Shift<Key>f"}}
#   {"Optimize rats nest" Atomic(Save) DeleteRats(AllRats)
#    Atomic(Restore) AddRats(AllRats) Atomic(Block) a={"O" "<Key>o"}}
#   {"Erase rats nest" DeleteRats(AllRats) a={"E" "<Key>e"}}
#   {"Erase selected rats" DeleteRats(SelectedRats) a={"Shift-E" "Shift<Key>e"}}
#
#   {"Auto-route selected rats" AutoRoute(Selected)}
#   {"Auto-route all rats" AutoRoute(AllRats)}
#   {"Rip up all auto-routed tracks" RipUp(All)}
#   {"Optimize routed tracks"
#    {"Auto-Optimize" djopt(auto)  a={"Shift-=" "Shift<Key>="}}
#    {"Debumpify" djopt(debumpify) }
#    {"Unjaggy" djopt(unjaggy) }
#    {"Vianudge" djopt(vianudge) }
#    {"Viatrim" djopt(viatrim) }
#    {"Ortho pull" djopt(orthopull) }
#    {"Simple optimization" djopt(simple)  a={"=" "<Key>="}}
#    {"Miter" djopt(miter) }
#    {"Puller" a={"Y" "<Key>y"} Puller() }
#
#    {"Only autorouted nets" OptAutoOnly() checked=optautoonly}
#   }
#  {"Design Rule Checker" DRC()}
#   {"Apply vendor drill mapping" ApplyVendor()}
#  }

	def genBrdPlaceBottom(self):
		ns = ''
	#Select(ElementByName|ObjectByName|PadByName|PinByName)
		for dev in self.brd.devices.values():
			name = str(dev.refid)
			if dev.bottom:
				#Select(ElementByName) ActiveWhen(have_regex)
				ns += 'Select(ElementByName) ActiveWhen( ' + name +  ' )\n' 
				ns += 'Flip(SelectedElements)\n' 
				ns += 'Unselect(All)\n'
		return ns

	# gen brd cmd scr"
	def genBrdCmdScr(self):
		ns = ''
		CRLF = "\n"
		ns += "# Gen EDA generated" + CRLF
		ns += "# date:" + CRLF			# version 
		ns += "# user:" + CRLF			# version 
# LoadFrom(Layout|LayoutToBuffer|ElementToBuffer|Netlist|Revert,filename)
		ns +=  'LoadFrom( Layout, '  + self.script_path + '/' + self.brd.name + '.pcb )' + CRLF			# layout
		ns +=  'LoadFrom( Netlist, ' + self.script_path + '/' + self.brd.name + '.net )' + CRLF			# netlist
# Do not do that, do it in the placement
#		ns += self.genBrdPlaceBottom()
# AddRats(AllRats|SelectedRats|Close)
		ns +=  'AddRats(AllRats)' + CRLF									# add all rats
# AutoRoute(AllRats|SelectedRats)
		ns +=  'AutoRoute(AllRats)' + CRLF									# route all rats
# Auto-Optimize djopt(auto)
		ns +=  'djopt(auto)' + CRLF											# optimize all routes
# SaveTo(Layout|LayoutAs,filename)
		ns +=  'SaveTo( LayoutAs, '  + self.script_path + '/' + self.brd.name + '.brd )' + CRLF			# board

		ns +=  'Quit( )' + CRLF												# Quit
		return ns
	
#####################################		
## release: pcb 1.7.1.ALPHA
## date:    Sun Jul 22 15:22:22 2001
## user:    tp (Terry Porter,,,)
## host:    gronk.porter.net

#PCB("" 6047 4000)
#
#Grid(25 0 0 0)
#Cursor(400 0 2)
#Flags(0x000000c0)
#Groups("1,s:2,c:3:4:5:6:7:8")
#Styles("Signal,10,40,20:Power,25,60,35:Fat,40,60,35:Skinny,8,36,20")

####################################
# release: pcb 1.99v
# date:    Tue May  1 07:59:48 2007
# user:    pawel (pawel,U-WODNICKI\pawel,S-1-5-21-1835012242-1811546175-1750076985-1007)
# host:    Wodnicki
#
#FileVersion[20070407]
#
#PCB["" 350000 330000]
#
#Grid[3937.007904 1800 100 1]
#Cursor[133000 107500 2.000000]
#PolyArea[200000000.000000]
#Thermal[0.500000]
#DRC[1000 1000 1000 1000 1500 1000]
#Flags("rubberband,nameonpcb,alldirection,uniquename,snappin")
#Groups("4,5,6,c:1,2,3,s:8:7")
#Styles["Signal,1000,4000,2000,1000:Power,2500,6000,3500,1000:Fat,4000,6000,3500,1000:Skinny,800,3600,2000,1000"]


	# gen brd board scr"
	def genBrdBoardScr(self):
		ns = ''
		CRLF = "\n"
		ns += "# boostEDA generated" + CRLF
		ns += "# date:" + CRLF			# version 
		ns += "# user:" + CRLF			# version 
		
		# determine board size, aka outline for rectangular ones only
		self.brd.outline.calcBBox()
				
		xsize = self.brd.outline.bbox.sizeX()
		ysize = self.brd.outline.bbox.sizeY()
		ns += "PCB[\"" + self.brd.name + "\" "
		ns += "%d "% (xsize)	# x size
		ns += " %d"% (ysize)	# y size
		ns += "]" + CRLF
		ns += "Grid(25 0 0 0)" + CRLF 
		ns += "Cursor(400 0 2)" + CRLF 
		ns += "Flags(0x000000c0)" + CRLF 
		ns += "Groups(\"1,s:2,c:3:4:5:6:7:8\")" + CRLF 
		ns += "Styles(\"Signal,10,40,20:Power,25,60,35:Fat,40,60,35:Skinny,8,36,20\")" + CRLF 
		return ns

#Layer(1 "solder")
#(
#	Line(1375 1075 1325 1025 40 30 0x00000020)
#)

	def genBrdLayerFromNet(self,layer,net):		
		ns = ''
		# Should come from board technology 
		
###		print "out net " + net.name
###		print "layer num " + str(layer.num)
		for line in net.route:
			#print "found line on net layer num " + str(line.layernum)
			if line.layernum == layer.num:
###				print "out line on net " + net.name
###				print "net.route length " + str(len(net.route))
###				print "line.points length " + str(len(line.points))
				Thickness = line.thickness
				Clearance = line.thickness * 2
				first = True
				prev  = Point()
				for pt in line.points:
					#print "pt  " + str(pt)
					if first:
						first = False
					else:
						X1 = int(prev._x)
						Y1 = int(prev._y)
						X2 = int(pt._x)
						Y2 = int(pt._y)
						ns += 'Line [' + " %d "% X1 + " %d "% Y1 + " %d "% X2 + " %d "% Y2
						ns += " %d "% Thickness
						ns += " %d "% Clearance
						ns += '"auto"'
						ns += ']\n' 
					prev = pt
					
		return ns
	
	def genLayerBlockages(self,layer):
		ns = ''
		# blockages use absolute coordinates, 		
		for rect in layer.blockages:
			# order of processing is important
			X1=int(rect.ll._x)
			Y1=int(rect.ll._y)
			X2=int(rect.ur._x)
			Y2=int(rect.ur._y)
			
			ns += ' Polygon("clearpoly")\n'
			ns += '(\n' 
			ns += " [%d "% X1 + " %d ]"% Y1
			ns += " [%d "% X1 + " %d ]"% Y2
			ns += " [%d "% X2 + " %d ]"% Y2
			ns += " [%d "% X2 + " %d ]"% Y1
			ns += '\n'
			ns += ')\n'
		return ns;
		
	# routing
	# gen brd layers scr"
	def genBrdLayersScr(self):
###		print "PCB! gen brd layers scr"
		ns = ''
		CRLF = "\n"
		for l in self.brd.layers:
###			print "layer " +  l.name
			ns += "Layer (" +str(l.num) + " \"" + l.name + "\")" + CRLF
			ns += "(" + CRLF
			# here go all of the layer elements
			for net in self.brd.nets.values():
				ns += self.genBrdLayerFromNet(l,net)		# Routes
				ns += self.generateNetPour(l,net)			# Geometry
			
			ns += self.genLayerBlockages(l)
			
			ns += ")" + CRLF
		return ns;

	def generateRoutes(self):
		return self.genBrdLayersScr()


	def generateNetPour(self,layer,net):
		ns = ''
		CRLF = "\n"
		
###		print " layer " + str(layer)
		
		for geom in net.geometry:					
###			print " found geom in " + net.name  + " type " + str(type(geom)) + " layer " + str(geom.layernum) + CRLF
			
			
			if geom.layernum != layer.num :
				continue


			# Handle rectangle
			#if type(geom) is Rectangle :
			if isinstance(geom, Rectangle) :

###				print " found Rectangle" + CRLF
				
				rect = Rectangle(geom.ll._x, geom.ll._y, geom.ur._x, geom.ur._y, geom.layernum )
				rect.normalize()						# normalize just in case
				
				# order of processing is important
				X1=int(rect.ll._x)
				Y1=int(rect.ll._y)
				X2=int(rect.ur._x)
				Y2=int(rect.ur._y)
				
				ns += ' Polygon("clearpoly")\n'
				ns += '(\n' 
				ns += " [%d "% X1 + " %d ]"% Y1
				ns += " [%d "% X1 + " %d ]"% Y2
				ns += " [%d "% X2 + " %d ]"% Y2
				ns += " [%d "% X2 + " %d ]"% Y1
				ns += '\n'
				ns += ')\n'					
					
		return ns;
		
	# Geometry on nets, aka pour
	def generatePour(self):
		ns = ''
		CRLF = "\n"
		for l in self.brd.layers:
###			print "layer " +  l.name
			ns += "Layer (" +str(l.num) + " \"" + l.name + "\")" + CRLF
			ns += "(" + CRLF
			# here go through the layers
			for net in self.brd.nets.values():
				ns += self.generateNetPour(l,net)
				
			ns += ")" + CRLF
		return ns;


# Via[]
# Via[17000 182000 31000 3000 34000 2800 "" ""]
# Via [X Y Thickness Clearance Mask Drill "Name" SFlags]
# Via (X Y Thickness Clearance Mask Drill "Name" NFlags)
# Via (X Y Thickness Clearance Drill "Name" NFlags)
# Via (X Y Thickness Drill "Name" NFlags)
# Via (X Y Thickness "Name" NFlags) 
#  	 X Y coordinates of center
# Thickness outer diameter of copper annulus
# Clearance add to thickness to get clearance diameter
# Mask diameter of solder mask opening
# Drill diameter of drill
# Name string, name of via (vias have names?)
# SFlags symbolic or numerical flags
# NFlags numerical flags only		
	def generateVias(self):
		ns = ''
		CRLF = "\n"
###		print " board vias " + str(len(self.brd.vias))
		for via in self.brd.vias:
###			print "via " + via.name
			ns += "Via ["
			ns += " %d "% int(via.pos._x) + " %d "% int(via.pos._y)
			ns += ' 4000 2000 0 2000 "" "" '
			ns += "]" + CRLF
		return ns;
	
	
	
#NetList()
#(
#	Net("unnamed_net1" "(unknown)")
#	(
#		Connect("L1-2")
#		Connect("L2-1")
#		Connect("C2-1")
#		Connect("C1-1")
#	)
#)

	# gen brd net scr"
	def genBrdNetlistScr(self):
		ns = ''
		CRLF = "\n"
		ns = 'NetList()' + CRLF
		ns += '(' + CRLF
		for net in self.sch.nets.values():
			name = net.name
			
			ns += "Net(\"" + net.name + "\" \"(unknown)\")" + CRLF
			ns += "(" + CRLF
			for node in net.nodes:
				ns += expandtab("\tConnect(\"") + str(node.dev.refid) + "-" + str(node.pin.num) + "\")" + CRLF
			ns += ")" + CRLF
		ns += ')' + CRLF
		return ns


# pcb footprint file may contain any of the following commands: 
# Element [element_flags, description, pcb-name, value, mark_x, mark_y, text_x, text_y, text_direction, text_scale, text_flags]
# Pad [x1 y1 x2 y2 thickness clearance mask name pad_number flags]
# Pin [x y thickness clearance mask drillholedia name number flags]
# ElementArc [x y r1 r2 startangle sweepangle thickness]
# ElementLine [x1 y1 x2 y2 thickness] > thickness != 1000 = 10 mils almost for all footprints
# Comment lines start with the #-sign 



#Elements

# Element [element_flags, description, pcb-name, value, mark_x, mark_y, text_x, text_y, text_direction, text_scale, text_flags] item 	allowed value 	explanation 	comment 
# element_flags 		unsigned hex value 		
# description 		string 	text description of footprint 	written by footprint author 
# pcb name 		string 	refdes used on this particular pcb 	xxx 
# value 			string 	value of component on this particular pcb layout 	xxx 
# mark_x 		1/100th mils 		
# mark_y 		1/100th mils 		
# text_x 		1/100th mils 		
# text_y 		1/100th mils 		
# text direction 	decimal integer 	0=horiz; 1=ccw90; 2=180; 3=cw90 	
# text_scale 		decimal integer 		usu. set 100 
# text_flags 		unsigned hex

# Pads

# Pad[x1 y1 x2 y2 thickness clearance mask name pad_number flags] Item 	Allowed Value 	Explanation 	Comment 
# x1 			1/100th mils 	x(1st point) 	
# y1 			1/100th mils 	y(1st point) 	
# x2 			1/100th mils 	x(2nd point) 	
# y2 			1/100th mils 	y(2nd point) 	
# thickness 		1/100 mils 	width of metal surrounding line segment 	see Brorson .pdf 
# clearance 		1/100 mils 	distance to any other copper on any layer 	actually 1/2 of this number is used! 
# mask 			1/100th mils 	width of mask relief 	actual width of the mask centered on pad copper 
# name 			string 	name of pad (arb. string) 	e.g. pad_1 or positive or any other string 
# pad_number 		string 	pad # 	used for nets. it MUST be consistent with the definitions on the netlist. 
# flags 	hex value 	xxx

# Pin[x y thickness clearance mask drillholedia name number flags] Item 	Allowed Value 	Explanation 	Comment 
# x 	1/100th mils 	pin x coord. 	
# y 	1/100th mils 	pin y coord. 	
# thickness 	1/100th mils 	copper diameter 	
# clearance 	1/100th mils 	2*(cu to cu clearance) 	if you want a 10 mil clearance, put 2000 (20 mils) here 
# mask 	1/100th mils 	diameter of mask aperture 	actual dia. of hole in mask 
# drillholedia 	1/100th mils 	dia. of hole 	
# name 	string 	arb. pin name 	
# number 	decimal integer 	pin number used by nets/rats 	
# flags 	hex 	xxx

# Via[]
# Via[17000 182000 31000 3000 34000 2800 "" ""]
# Via [X Y Thickness Clearance Mask Drill "Name" SFlags]
# Via (X Y Thickness Clearance Mask Drill "Name" NFlags)
# Via (X Y Thickness Clearance Drill "Name" NFlags)
# Via (X Y Thickness Drill "Name" NFlags)
# Via (X Y Thickness "Name" NFlags) 
#  	 X Y coordinates of center
# Thickness outer diameter of copper annulus
# Clearance add to thickness to get clearance diameter
# Mask diameter of solder mask opening
# Drill diameter of drill
# Name string, name of via (vias have names?)
# SFlags symbolic or numerical flags
# NFlags numerical flags only




# On the Layer 
# Line[]
# Line[137500 107500 132500 102500 4000 3000 "clearline"]
# Text[423000 391500 2 100 "T J PORTER   ELECTRONICS" "auto"]
# Polygon("clearpoly")
# (
#	[2000 198000] [47000 198000] [47000 187000] [126000 187000] [126000 198000] 
#	[297000 198000] [297000 1000] [2000 1000] 
# )
	
# Notes:
# Pins - Throughole
# Pads - SMD

# Examples for version 1.99
# TH
# Element["" "Cap" "C17" "" 215500 81500 -9000 -32900 0 150 ""]
# (
#        Pin[0 0 8000 3000 11000 3500 "1" "1" ""]
#        Pin[0 -20000 8000 3000 11000 3500 "2" "2" ""]
#        ElementLine [-5000 5000 5000 5000 1000]
#        ElementLine [5000 5000 5000 -25000 1000]
#        ElementLine [5000 -25000 -5000 -25000 1000]
#        ElementLine [-5000 -25000 -5000 5000 1000]
#
# )

# SMD
# Element["" "SMD 0805" "C13" "" 252500 151000 -3000 4500 0 150 ""]
# (
#        Pad[0 0 0 0 6000 3000 9000 "1" "1" "square"]
#        Pad[0 -9000 0 -9000 6000 3000 9000 "2" "2" "square"]
#        ElementLine [-3500 -12500 -3500 3500 1000]
#        ElementLine [3500 -12500 -3500 -12500 1000]
#        ElementLine [3500 3500 3500 -12500 1000]
#        ElementLine [-3500 3500 3500 3500 1000]
# )
# 



# Original
#Element["" "SOT-23 package" "Q7" "" 66666 66666 3200 5900 0 100 ""]
#(
#	Pad[0 -300 0 300 3400 3000 4000 "1" "1" "square,edge2"]
#	Pad[7800 -300 7800 300 3400 3000 4000 "2" "2" "square,edge2"]
#	Pad[3900 -8500 3900 -7900 3400 3000 4000 "3" "3" "square"] 
#	ElementLine [10300 -11000 -2500 -11000 1000]
#	ElementLine [10300 2900 10300 -11000 1000]
#	ElementLine [-2500 2900 10300 2900 1000]
#	ElementLine [-2500 -11000 -2500 2900 1000]
#)

# Placed on the far side -> layer onsolder?
#Element["selected,onsolder" "SOT-23 package" "Q7" "" 66666 133334 3200 -5900 0 100 "selected,auto"]
#(
#        Pad[0 300 0 -300 3400 3000 4000 "1" "1" "selected,onsolder,square"]
#        Pad[7800 300 7800 -300 3400 3000 4000 "2" "2" "selected,onsolder,square"]
#        Pad[3900 8500 3900 7900 3400 3000 4000 "3" "3" "selected,onsolder,square,edge2"]
#        ElementLine [10300 11000 -2500 11000 1000]
#        ElementLine [10300 -2900 10300 11000 1000]
#        ElementLine [-2500 -2900 10300 -2900 1000]
#        ElementLine [-2500 11000 -2500 -2900 1000]
#
#        )


# VIAs
# Via[17000 182000 31000 3000 34000 2800 "" ""]
# Via[17000 17000 31000 3000 34000 2800 "" ""]
# Via[282000 17000 31000 3000 34000 2800 "" ""]
# Via[282000 182000 31000 3000 34000 2800 "" ""]
# Via[15500 382500 31000 3000 34000 2800 "" ""]
# Via[15500 217500 31000 3000 34000 2800 "" ""]
# Via[280500 217500 31000 3000 34000 2800 "" ""]


# Tracks are made of Line????
# Layer(1 "solder")
# (
#	Line[137500 107500 132500 102500 4000 3000 "clearline"]
#	Line[145000 107500 137500 107500 4000 3000 "clearline"]
#	Line[85000 112500 85000 107500 4000 3000 "clearline"]
#	Line[97500 90000 97500 147500 4000 3000 "clearline"]
#)

 
# Element [element_flags, description, pcb-name, value, mark_x, mark_y, text_x, text_y, text_direction, text_scale, text_flags]
	def gen0805_resitor(self,refid,x,y,v):
		CRLF = '\n'
		s = 'Element["" "0805 chip resitor" "' + str(refid) + '" "' + str(v) + '" ' +'%i'% x + ' ' + '%i'% y + ' 3200 5900 0 100 ""]' + CRLF
		s += '(' + CRLF
		s += '	Pad[0 -700 0 700 4500 3000 5100 "1" "1" "square"]' + CRLF
		s += '	Pad[8000 -700 8000 700 4500 3000 5100 "2" "2" "square"]' + CRLF
		s += '	ElementLine [11700 -4400 -3700 -4400 800]' + CRLF
		s += '	ElementLine [11700 4400 11700 -4400 800]' + CRLF
		s += '	ElementLine [-3700 4400 11700 4400 800]' + CRLF
		s += '	ElementLine [-3700 -4400 -3700 4400 800]' + CRLF
		s += ')'  + CRLF
		return s
		
	def gen0805_capacitor(self,refid,x,y,v):
		CRLF = '\n'
		s = 'Element["" "0805 chip cap" "' + str(refid) + '" "' + str(v) + '" ' +'%i'% x + ' ' + '%i'% y + ' 3200 5900 0 100 ""]' + CRLF
		s += '(' + CRLF
		s += '	Pad[0 -700 0 700 4500 3000 5100 "1" "1" "square"]' + CRLF
		s += '	Pad[8000 -700 8000 700 4500 3000 5100 "2" "2" "square"]' + CRLF
		s += '	ElementLine [11700 -4400 -3700 -4400 800]' + CRLF
		s += '	ElementLine [11700 4400 11700 -4400 800]' + CRLF
		s += '	ElementLine [-3700 4400 11700 4400 800]' + CRLF
		s += '	ElementLine [-3700 -4400 -3700 4400 800]'  + CRLF
		s += ')'  + CRLF
		return s

	def genSOT23(self, refid, x, y, v):
		CRLF = '\n'
		s = 'Element["" "SOT-23 package" "' + str(refid) + '" "' + str(v) + '" ' +'%i'% x + ' ' + '%i'% y + ' 3200 5900 0 100 ""]' + CRLF
		s += '(' + CRLF
		s += '	Pad[0 -300 0 300 3400 3000 4000 "1" "1" "square,edge2"]' + CRLF
		s += '	Pad[7800 -300 7800 300 3400 3000 4000 "2" "2" "square,edge2"]' + CRLF
		s += '	Pad[3900 -8500 3900 -7900 3400 3000 4000 "3" "3" "square"] ' + CRLF
		s += '	ElementLine [10300 -11000 -2500 -11000 1000]' + CRLF
		s += '	ElementLine [10300 2900 10300 -11000 1000]' + CRLF
		s += '	ElementLine [-2500 2900 10300 2900 1000]' + CRLF
		s += '	ElementLine [-2500 -11000 -2500 2900 1000]' + CRLF
		s += ')'  + CRLF
		return s
	

	
	def rotatePoint(self,pt,x0,y0,angle):
					
		dX = pt._x - x0
		dY = pt._y - y0
			
		rX = pt._x
		rY = pt._y
		
		if angle == 90:
			rX = x0 + dY
			rY = y0 - dX
			
		if angle == 180:
			rX = x0 - dX
			rY = y0 - dY
		
		if angle == 270:
			rX = x0 - dY
			rY = y0 + dX
			
		return rX,rY

	def genElementLine(self,line,dev):
		# order of processing is important
		X1=int(line.points[0]._x)
		Y1=int(line.points[0]._y)
		X2=int(line.points[1]._x)
		Y2=int(line.points[1]._y)
		
		if dev.bottom:
			Y1 = 0 - Y1
			Y2 = 0 - Y2
		
		X1,Y1 = self.rotatePoint(Point(X1,Y1),0,0,dev.rotation)
		X2,Y2 = self.rotatePoint(Point(X2,Y2),0,0,dev.rotation)
		
		# keep horizontal, vertical Point2 > Point1
		if (X1 == X2):
			if (Y1 > Y2):
				t = Y1
				Y1 = Y2
				Y2 = t
		else: 
			if (Y1 == Y2):
				if (X1 > X2):
					t = X1
					X1 = X2
					X2 = t
		ns = 'ElementLine [' + " %d "% X1 + " %d "% Y1 + " %d "% X2 + " %d "% Y2
		ns += " %d "% line.thickness
		ns += ']\n' 
		return ns
				
	# rotation is clockwise
	def genElementArc(self,arc,dev):
#		 Thickness, Clearance, Mask, Drill, Name, Number, SFlags
		rX = int(arc._x)
		rY = int(arc._y)
		
		# rY is 
		if dev.bottom:
			rY = 0 - rY
				
		if dev.rotation == 90:
			arc.sangle += 90 
		
		if dev.rotation == 180:
			arc.sangle += 180
		
		if dev.rotation == 270:
			arc.sangle += 270
		
		rX,rY = self.rotatePoint(arc,0,0,dev.rotation)
		arc.sangle = arc.sangle % 360
		ns  = 'ElementArc [' +  " %d "% rX + " %d "% rY
		ns += " %d "% arc.width
		ns += " %d "% arc.height
		ns += " %d "% arc.sangle 
		ns += " %d "% arc.dangle
		ns += " %d "% arc.thickness
		ns += ']\n' 
		return ns
	
	def genElementPin(self,pin,dev):
#		 Thickness, Clearance, Mask, Drill, Name, Number, SFlags
		rX=int(pin.pos._x)
		rY=int(pin.pos._y)
		
		# Why we do not have to do it for the pins?
		# rY is 
		#if dev.bottom:
		#	rY = 0 - rY
			
		# Package has not been rotated and must match device pins
		rX,rY = self.rotatePoint(Point(rX,rY),0,0,dev.rotation)
		ns  = 'Pin [' +  " %d "% rX + " %d "% rY
		ns += " %d "% pin.thickness
		ns += " %d "% pin.clearance
		ns += " %d "% pin.mask 
		ns += " %d "% pin.drill 
		ns += pin.name + ' ' 
		ns += '"' + "%d"% pin.num + '" '
		ns += pin.sflags 
		ns += ']\n' 
		return ns
	
	def genElementPad(self,pin,dev):
#		Thickness, Clearance, Mask, Name, Number, SFlags
		# if package was parsed then these are set, if not I need to generate correct ones
		rX1=int(pin.rX1)
		rY1=int(pin.rY1)
		rX2=int(pin.rX2)
		rY2=int(pin.rY2)
		
		# Why we do not have to do it for the pads?
		#if dev.bottom:
		#	rY1 = 0 - rY1
		#	rY2 = 0 - rY2
			
		rX1,rY1 = self.rotatePoint(Point(rX1,rY1),0,0,dev.rotation)
		rX2,rY2 = self.rotatePoint(Point(rX2,rY2),0,0,dev.rotation)
		
		try:
			sflags = pin.sflags 
		except:
			# no PCB sflags then generate one
			# square
			# edge2
			if pin.pad.type == "S":
				sflags ='"square"'
			else:
				sflags ='""'
			
		ns = 'Pad [' + " %d "% rX1 + " %d "% rY1 + " %d "% rX2 + " %d "% rY2
		ns += " %d "% pin.thickness
		ns += " %d "% pin.clearance
		ns += " %d "% pin.mask 
		ns += pin.name + ' ' 
		ns += '"' + "%d"% pin.num + '" '
		ns += sflags 
		ns += ']\n' 
		return ns
	
	def genElementBody(self,dev):
		# print'name ' + dev.name
		l = len(dev.pins)
		# print ' len ' + str(l)
		# print 'roation ' + str(dev.rotation)
		ns = '(\n'
		for num in range(1,l+1):
			# print 'pin ' + str(num)
			pin  = dev.pins[num]
			ppin = dev.package.pins[num]
			#if dev.package.smt:						# event smt packages can have pins aka mounting holes
			if ppin.smt:
				ns += self.genElementPad(ppin,dev)
			else:
				ns += self.genElementPin(ppin,dev)
				
		for geo in dev.package.geometry:
			if isinstance(geo, Line):
				ns += self.genElementLine(geo,dev)
				
			if isinstance(geo, Arc):
				ns += self.genElementArc(geo,dev)
				
			if isinstance(geo, Text):
				ns += self.genElementText(geo,dev)
					
		ns += ')\n'
		return ns

	# Device is  on the bottom, coordinates of the pad are for the bottom
	# Pcb defines package looking from top so mirror it in X back to top
	# and add the  flags
	# For details see the core.py
	def genBrdPlaceDevOnSolder(self,dev):
		for pad in dev.package.pins.values():
			pad.pos._y = 0 - pad.pos._y
			try:									# quick fix TBI
				pad.rY1 = 0 -  pad.rY1
			except:
				pad.rY1 = 0
			try:									# quick fix TBI
				pad.rY2 = 0 -  pad.rY2
			except:
				pad.rY2 = 0
			try:									# quick fix TBI
				newsflags = pad.sflags.strip('"')
			except:
				newsflags = 'square'	# default to square
			if newsflags != '':
				newsflags = ',' + newsflags
			newsflags = '"onsolder' + newsflags + '"'
			pad.sflags = newsflags
		for pad in dev.package.geometry:
			pass
			# print pad.sflags
	
	# gen brd place scr"
	def genBrdPlaceScr(self):
		ns = ''
		CRLF = '\n'
		devnum  = 0
		self.brd.outline.calcBBox()
		for dev in self.brd.devices.values():
			name = str(dev.refid) + CRLF
			if dev.bottom:
				self.genBrdPlaceDevOnSolder(dev)
				x = (int)
				#x = (self.brd.outline.bbox.ur._x - dev.position._x) # position is in mils
				x = dev.position._x # position is in mils
				y = (int)
				#y = (self.brd.outline.bbox.ur._y - dev.position._y) # position is in mils
				y = dev.position._y # position is in mils
				placement = '"onsolder"'
			else:
				x = (int)
				x = dev.position._x # position is in mils
				y = (int)
				y = dev.position._y  # position is in mils
				placement = '""'
			# place the device
			ns += 'Element[' + placement + ' "' + str(dev.package.description) + '" "' + str(dev.refid) + '" "' + str(dev.val) + '" ' +'%i'% x + ' ' + '%i'% y + ' 3200 5900 0 100 ""]' + CRLF
			ns += self.genElementBody(dev)
			
#			if name[0:1] == 'R':
#				ns += self.gen0805_resitor(dev.refid,x,y,dev.val)
#			if name[0:1] == 'C':
#				ns += self.gen0805_capacitor(dev.refid,x,y,dev.val)
#			if name[0:1] == 'Q':
#				ns += self.genSOT23(dev.refid,x,y,dev.val)
#			numpins = 0
#			for pin in dev.pins:
#				numpins += 1
#			for k in dev.pins.keys():
#				pin = dev.pins[k]

			# dev.rotation ?
		return ns
		
		
	def Cmd(self,cmds):
		gen = 0
		sch = 0
		brd = 0
		cmd = 0
		add = 0
		layers = 0
		net_connect = 0
		netlist = 0
		board = 0
		place = 0
		route = 0
		scr = 0
		lst = 0
		
		# 0
		if cmds[0:1] == ['gen']:
			gen = 1
		# 1
		if cmds[1:2] == ['sch']:
			sch = 1

		if cmds[1:2] == ['brd']:
			brd = 1

		# 2
		if cmds[2:3] == ['cmd']:
			cmd = 1
			
		if cmds[2:3] == ['add']:
			add = 1
			
		if cmds[2:3] == ['layers']:
			layers = 1
			
		if cmds[2:3] == ['netconnect']:
			net_connect = 1
			
		if cmds[2:3] == ['netlist']:
			netlist = 1
			
		if cmds[2:3] == ['board']:
			board = 1
		
		if cmds[2:3] == ['place']:
			place = 1
			
		if cmds[2:3] == ['route']:
			route = 1

		# 3	
		if cmds[3:4] == ['scr']:
			scr = 1
			
		if cmds[3:4] == ['lst']:
			lst = 1

		if gen:
			if sch:
				if add:
					if scr:
						s = self.genSchAddScr()
						return s
						
				if layers:
					if scr:
						s = self.genSchLayersScr()
						return s
					
				if net_connect:
					pass
					
				if netlist:
						s = self.genSchNetlistLst()
						return s
		
			if brd:
				if cmd:
					if scr:
						s = self.genBrdCmdScr()			# commands to make the board
						return s
					
				if board:
					if scr:
						s = self.genBrdBoardScr()
						return s
				if layers:
					if scr:
						s = self.genBrdLayersScr()
						return s
				if place:
					if scr:
						s = self.genBrdPlaceScr()
						return s
					
				if netlist:
					if scr:
						s = self.genBrdNetlistScr()
						return s
				if route:
					pass
		
					
		return ""
					
			
	def test(self):
		
		ic1 = CDev("U1","","IC1")
		ic1.add( CPin("GND",1) )
		ic1.add( CPin("VCC",2) )
		self.sch.addDev(ic1)
	
		net1 = CNet("GND")
		net1.add(CNode(ic1,"GND"))
		self.sch.addNet(net1)
	
		net2 = CNet("VCC")
		net2.add(CNode(ic1,"VCC"))
		self.sch.addNet(net2)
		
		print "gen sch add scr"
		s = self.genSchAddScr()
		print s
		print "gen sch net-connect scr"
		s = self.genSchNetConnectScr()
		print s
		print "gen sch netlist lst"
		s = self.genSchNetlistLst()
		print s
		print "gen sch netlist scr"
		s = self.genSchNetlistScr()
		print s
	
# Some tests
if __name__ == "__main__":
	import sys
	#import string
	import re
	schem = CSchematic()
	board = CBoard(schem)
	board.addFromSchematic()

	mucs = CPCB(schem,board)
	
	# open input file
	if sys.argv[1:] == ['test']:
		mucs.test()
    
