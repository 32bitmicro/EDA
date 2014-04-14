import platform
import re
import sys
import os
import subprocess

from eda import *
from eda.dump import *
from eda.xmlpickle import *


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

# route using Eagle
# TBI
	
if __name__ == "__main__":
	name = sys.argv[1]
	ppath  = sys.argv[2]

	sch = import_schematic_pickle(ppath, name)
    	brd = import_board_pickle(ppath, name)
	print
	print "brd.outline after import ", str(brd.outline)
	print
	#sch = stm32dip40_schematic.make(name, name)
    	#brd = stm32dip40_board.make(sch, name, name)
	pickle = CXMLPickle(sch, brd)
	
	# export cad
#	export_eagle_data(ppath, name,sch,brd)
	# route
	# import cad
#	import_eagle_data(ppath, name,sch,brd)
		
	try:
		print "pickling into ", ppath+"/"+name+".route"
		f = open(ppath+"/"+name+".route",'w')
		pickle.pickleBoard(f)
	except:
		print "pickle file missing or pickler has failed"
    
