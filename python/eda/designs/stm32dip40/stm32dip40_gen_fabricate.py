import sys
from eda import *
from eda.dump import *
from eda.xmlpickle import *
from eda.pcb import *
from eda.eagle import *
from eda.kicad import *

import stm32dip40_schematic
import stm32dip40_board


def import_schematic_pickle(ppath, name):
	pickle=CXMLPickle()
	f = open(ppath+"/"+name+".schematic",'r+')
	pickle.unpickleSchematic(f)
	return  pickle.sch

def import_board_pickle(ppath,name):
	pickle=CXMLPickle()
	f = open(ppath+"/"+name+".board",'r+')
	pickle.unpickleBoard(f)
	return pickle.brd




def export_eagle_data(ppath,name,sch,brd):
	
###	print "export eagle data"
	
	eagle = CEagle(sch,brd)
	
	# Set names
	# why writing requires path?	
	# output path
	#outpath = ""
	outpath = ppath+"/"

	eaglename 			= name + "_fab_eagle.scr"
	eagleschematicname 		= name + "_fab_eagle_schm.scr"
	eagleschematicnetlistname 	= name + "_fab_eaglenet_schm.scr"
	eaglenetlistname 		= name + "_fab_eaglenet.scr"
	eaglelibname 			= name + "_fab_eaglelib.scr"
	
	# Export Eagle
	# Schematic
	s = eagle.genSchAddScr()		# All Devices
#	s += eagle.genSchLayersScr()	# Layers
	s += eagle.generateConnections()# Connections
###	print "creating " + str(eagleschematicname)
	f = open(outpath+eagleschematicname,'w')
	f.write(s)
	
	# Export Eagle
	# Schematic Netlist
#	s = eagle.generateSchematicNetlist() # Schematic netlist good but need position
#	s = eagle.genSchNetlistLst()	# Netlist
	s = eagle.genSchNetConnectScr() # Net connect script
###	print "creating " + str(eagleschematicnetlistname)
	f = open(outpath+eagleschematicnetlistname,'w')
	f.write(s)
	
	# Export Eagle
	# Library
	s = eagle.genSchLayersScr()		# Layers
	s += eagle.generatePackages()	# Packages
	s += eagle.generateDevices()	# Devices
###	print "creating " + str(eaglelibname)
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
###	print "creating " + str(eaglename)
	f = open(outpath+eaglename,'w')
	f.write(s)
	
	# Export Eagle
	# Netlist
	s = eagle.genSchNetlistScr()	# Netlist
###	print "creating " + str(eaglenetlistname)
	f = open(outpath+eaglenetlistname,'w')
	f.write(s)
	
	

def export_pcb_data(ppath,name,sch,brd):
	
###	print "export pcb data"
	
	pcb = CPCB(sch,brd)
	
	# Set names
	# why writing requires path?
	pcbname  = name + "_fab_pcb.pcb"
	
	# output path
	outpath = ""
	outpath = ppath+"/"

	# Export PCB
	pcb.addLayers()
	s = pcb.genBrdBoardScr()		# Board
#	s += pcb.generatePour()			# All copper geometry, can not be here must be done with Routes
	s += pcb.genBrdPlaceScr()		# Placement
	s += pcb.generateRoutes()		# Routes
	s += pcb.generateVias()			# VIAs
	s += pcb.genBrdNetlistScr()	 	# Netlist
###	print "creating " + str(pcbname)
	f = open(outpath+pcbname,'w')
	f.write(s)

	
def export_kicad_data(ppath,name,sch,brd):
	
###	print "export kicad data"
	
	kicad = CKICAD(sch,brd)

	# Set names
	# why writing requires path?
	kicadname =  name + "_fab_kicad.brd"
	
	# output path
	outpath = ""
	outpath = ppath+"/"
	
	# Export Kicad
	s  = kicad.generateBegin()		# Start
	s += kicad.generateLayers()		# Layers
	s += kicad.generateBoard()		# Board
#	s += kicad.generatePour()		# All copper geometry
	s += kicad.generatePlacement()	# Placement
	s += kicad.generateRoutes()		# Routes
#	s += kicad.generateVias()		# VIAs

	s += kicad.generateFinish()		# Done
###	print "creating " + str(kicadname)
	f = open(outpath+kicadname,'w')
	f.write(s)


	
if __name__ == "__main__":
	name = sys.argv[1]
	ppath  = sys.argv[2]

	sch = import_schematic_pickle(ppath, name)
    	brd = import_board_pickle(ppath, name)

	# import(sch) import(brd) does not work
	# make(sch) import(brd) does not work
	# make(sch) make(brd) import(route) does work

	# import cad data with placement and routing
	#import_eagle_data(ppath, name,sch,brd)
	
	pickle = CXMLPickle(sch, brd)
	
	
	# export cad
	# Eagle	
	export_eagle_data(ppath,name,sch,brd)
	# PCB
	export_pcb_data(ppath,name,sch,brd)
	# KiCAd
	export_kicad_data(ppath,name,sch,brd)
	
	try:
		print "pickling into ", ppath
		f = open(ppath+"/"+name+".fabricate",'w')
		pickle.pickleBoard(f)
	except:
		print "pickle file missing or pickler has failed"
    
