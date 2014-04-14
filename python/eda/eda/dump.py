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

CRLF = "\n"

class CDump:
    " Dump class "
    def __init__(self, sch=None,brd=None):
        self.name=""
        self.sch=sch
        self.brd=brd
      
    def dumpNet(self,net):
        ns = ''
            
        for node in net.nodes:
            ns += "        pin " + str(node.pin.num) + " - " + node.pin.name + " dev " + node.dev.refid +  CRLF
            
        return ns
                
    def dumpNets(self, design):
        ns = ''
        ns += "NETS:  "  + CRLF
        ns += ""  + CRLF
                
        for netname in design.nets:
            net = design.nets[netname]
            ns += "    "  + netname + CRLF
            ns += self.dumpNet(net)
            ns += ""  + CRLF
            
        return ns


    def dumpDevice(self, dev):
        ns = ''
            
        for pinnum in dev.pins:
            pin = dev.pins[pinnum]
            ns += "        pin " + str(pin.num) + " - " + pin.name + " net " + pin.netname +  CRLF
            
        return ns
    
    def dumpDevices(self, design):
        ns = ''
        ns += "Devices:  "  + CRLF
        ns += ""  + CRLF
                
        for devname in design.devices:
            dev = design.devices[devname]
            ns += "    "  + devname + CRLF
            ns += self.dumpDevice(dev)
            ns += ""  + CRLF
            
        return ns
