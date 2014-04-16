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
from eda.components.component import *
from eda.components.LDO.ld1117 import *

# Handle LDOs as sub-circuit aka module
# Adds all passive elements and nets to the schematic

class ldo_ld1117:
    pass

    def add(self,sch,ldo,innet,outnet,gndnet,rstart,cstart):
        innet.add(CNode(ldo,'IN'))
        outnet.add(CNode(ldo,'OUT'))
        gndnet.add(CNode(ldo,'GND'))
        # Tantalum cap
        refid = "C" + "%d"% cstart
        c1 = CAPPOLYSMT(refid,"","cap poly 1 ldo ")
        sch.addDev(c1)
        outnet.add(CNode(c1,'+'))
        gndnet.add(CNode(c1,'-'))
        # Cap 2
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c2 = CAPSMT(refid,"","cap 2 ldo ")
        sch.addDev(c2)
        outnet.add(CNode(c2,'2'))
        gndnet.add(CNode(c2,'1'))
        # Cap 3
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c3 = CAPSMT(refid,"","cap 3 ldo ")
        sch.addDev(c3)
        outnet.add(CNode(c3,'2'))
        gndnet.add(CNode(c3,'1'))
        # connect
    
    def place_on_schematic(self,sch,ldo,rstart,cstart):
        # Tantalum cap
        refid = "C" + "%d"% cstart
        c1 = sch.getDev(refid)
        # Cap 2
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c2 = sch.getDev(refid)
        # Cap 3
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c3 = sch.getDev(refid)
        X = ldo.position._x
        Y = ldo.position._y
        # print 'ldo position ' + str(ldo.position)
        c1.setPos(X+1.000,Y+0)
        c1.setRotation(90)
        c1.setBottom(ldo.isBottom())
        c2.setPos(X+2.000,Y+0.200)
        c2.setRotation(0)
        c2.setBottom(ldo.isBottom())
        c3.setPos(X+2.000,Y+0.400)
        c3.setRotation(0)
        c3.setBottom(ldo.isBottom())
        
    def place_on_board(self,sch,ldo,rstart,cstart):
        # Tantalum cap
        refid = "C" + "%d"% cstart
        c1 = sch.getDev(refid)
        # Cap 2
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c2 = sch.getDev(refid)
        # Cap 3
        cstart = cstart + 1
        refid = "C" + "%d"% cstart
        c3 = sch.getDev(refid)
        X = ldo.position._x
        Y = ldo.position._y
        # print 'ldo position ' + str(ldo.position)
        c1.setPos(X+mil2pcb(400),Y+mil2pcb(120))
        c1.setRotation(90)
        c1.setBottom(ldo.isBottom())
        c2.setPos(X+mil2pcb(0),Y+mil2pcb(400))
        c2.setRotation(0)
        c2.setBottom(ldo.isBottom())
        c3.setPos(X+mil2pcb(300),Y+mil2pcb(400))
        c3.setRotation(0)
        c3.setBottom(ldo.isBottom())
