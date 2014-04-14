import sys
from eda import *
from eda.xmlpickle import *

import stm32dip40_schematic
import stm32dip40_board

def import_schematic_pickle(ppath, name):
	pickle=CXMLPickle()
	f = open(ppath+"/"+name+".schematic",'r+')
	pickle.unpickleSchematic(f)
	return  pickle.sch

def export_eagle_data(ppath,name,sch,brd):
	
	print "export eagle data"
	
	eagle = CEagle(sch,brd)
	
	# Set names
	# why writing requires path?	
	# output path
	#outpath = ""
	outpath = ppath+"/"

	eaglename 			= name + "_placement_eagle.scr"
	eagleschematicname 		= name + "_placement_eagle_schm.scr"
	eagleschematicnetlistname 	= name + "_placement_eaglenet_schm.scr"
	eaglenetlistname 		= name + "_placement_eaglenet.scr"
	eaglelibname 			= name + "_placement_eaglelib.scr"
	
	# Export Eagle
	# Schematic
	s = eagle.genSchAddScr()		# All Devices
#	s += eagle.genSchLayersScr()	# Layers
	s += eagle.generateConnections()# Connections
	print "creating " + str(eagleschematicname)
	f = open(outpath+eagleschematicname,'w')
	f.write(s)
	
	# Export Eagle
	# Schematic Netlist
#	s = eagle.generateSchematicNetlist() # Schematic netlist good but need position
#	s = eagle.genSchNetlistLst()	# Netlist
	s = eagle.genSchNetConnectScr() # Net connect script
	print "creating " + str(eagleschematicnetlistname)
	f = open(outpath+eagleschematicnetlistname,'w')
	f.write(s)
	
	# Export Eagle
	# Library
	s = eagle.genSchLayersScr()		# Layers
	s += eagle.generatePackages()	# Packages
	s += eagle.generateDevices()	# Devices
	print "creating " + str(eaglelibname)
	f = open(outpath+eaglelibname,'w')
	f.write(s)
	
	# Export Eagle
	# Board
	s = eagle.genSchLayersScr()		# Layers
	s += eagle.genBrdBoardScr()		# Board
	s += eagle.generatePour()		# All copper geometry
	s += eagle.genBrdPlaceScr()		# Placement
	s += eagle.generateRoutes()		# Routes
	s += eagle.generateVias()		# VIAs
	print "creating " + str(eaglename)
	f = open(outpath+eaglename,'w')
	f.write(s)
	
	# Export Eagle
	# Netlist
	s = eagle.genSchNetlistScr()	# Netlist
	print "creating " + str(eaglenetlistname)
	f = open(outpath+eaglenetlistname,'w')
	f.write(s)

def export_pcb_data(ppath,name,sch,brd):
	
	print "export pcb data"
	
	pcb = CPCB(sch,brd)
	
	# Set names
	pcbname  =  name + "_placement_pcb.pcb"
	
	
	# output path
	#outpath = ""
	outpath = ppath+"/"

	# Export PCB
	pcb.addLayers()
	s = pcb.genBrdBoardScr()		# Board
#	s += pcb.generatePour()			# All copper geometry, can not be here must be done with Routes
	s += pcb.genBrdPlaceScr()		# Placement
	s += pcb.generateRoutes()		# Routes
	s += pcb.generateVias()			# VIAs
	s += pcb.genBrdNetlistScr()	 	# Netlist
	print "creating " + str(pcbname)
	f = open(outpath+pcbname,'w')
	f.write(s)

if __name__ == "__main__":
	name = sys.argv[1]
	ppath  = sys.argv[2]
	sch = import_schematic_pickle(ppath,name)
	#sch = stm32dip40_schematic.make(name, name)
    	brd = stm32dip40_board.make(sch, name, name)
	print "after make"
	print str(brd.outline)
	pickle = CXMLPickle(sch, brd)

	
	# for viewing placement
	export_eagle_data(ppath,name,sch,brd)
	export_pcb_data(ppath,name,sch,brd)
	
	try:
		print "pickling into ", ppath+"/"+name+".board"
		f = open(ppath+"/"+name+".board",'w')
		pickle.pickleBoard(f)
	except:
		print "pickle file missing or pickler has failed"
		exit(-1)
    
