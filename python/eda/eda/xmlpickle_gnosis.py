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

import gnosis.xml.pickle as xml_pickle
import gnosis.xml.objectify as xml_objectify

from edautils import *
from eda import *


class CXMLPickle:
    "XML pickle class "
    def __init__(self, sch=None,brd=None):
        self.name=""
        self.sch=sch
        self.brd=brd
        
# Pickle 
    def pickleBoardToString(self):
        ns = xml_pickle.XML_Pickler(self.brd).dumps()             
        return ns
        
    def pickleSchematicToString(self):
        ns = xml_pickle.XML_Pickler(self.sch).dumps()             
        return ns
    
    def pickleAllToString(self):
        ns = self.pickleSchematic()
        ns += self.pickleBoard()
        return ns
    
    def pickleBoard(self, f):
        xml_pickle.XML_Pickler(self.brd).dump(f)

    def pickleBoardDevices(self,f):
        xml_pickle.XML_Pickler(self.brd.devices).dump(f)

    def pickleBoardGeometry(self,f):
        xml_pickle.XML_Pickler(self.brd.geometry).dump(f)
        
    def pickleSchematic(self,f):
        xml_pickle.XML_Pickler(self.sch).dump(f)             
   
    def pickleDevices(self,f):
        xml_pickle.XML_Pickler(self.sch.devices).dump(f)

    def pickleSymbols(self,f):
	xml_pickle.XML_Pickler(self.sch.symbols).dump(f)
	
    def pickleNets(self,f):
        xml_pickle.XML_Pickler(self.sch.nets).dump(f)
	
    def pickleAll(self, f_sch, f_brd):
        self.pickleSchematic(f_sch)
        self.pickleBoard(f_brd)
    
# Unpickle 
    def unpickleBoardFromsString(self, xml_string):
        self.brd = xml_pickle.XML_Pickler().loads(xml_string)
        
    def unpickleSchematicFromsString(self, xml_string):
        self.sch = xml_pickle.XML_Pickler().loads(xml_string)
       
    def unpickleAllFromsString(self, sch_xml_string, brd_xml_string):
        self.unpickleSchematic(sch_xml_string)
        self.unpickleBoard(brd_xml_string)
        
    def unpickleBoard(self, f):
	self.brd = xml_pickle.XML_Pickler().load(f)

    def pickleBoardDevices(self,f):
	self.brd.devices = xml_pickle.XML_Pickler().load(f)
        xml_pickle.XML_Pickler(self.brd.devices).dump(f)

    def unpickleBoardGeometry(self,f):
	self.brd.geometry = xml_pickle.XML_Pickler().load(f)

    def unpickleSchematic(self, f):
        self.sch = xml_pickle.XML_Pickler().load(f)
	
    def unpickleDevices(self,f):
        self.sch.devices = xml_pickle.XML_Pickler().load(f)

    def unpickleSymbols(self,f):
	self.sch.symbols = xml_pickle.XML_Pickler().load(f)
	
    def unpickleNets(self,f):
        self.sch.nets = xml_pickle.XML_Pickler().load(f)
       
    def unpickleAll(self, f_sch, f_brd):
        self.unpickleSchematic(f_sch)
        self.unpickleBoard(f_brd)
