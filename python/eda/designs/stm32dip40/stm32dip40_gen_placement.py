import sys
from eda import *
from eda.xmlpickle import *
import stm32dip40_schematic
import stm32dip40_board


if __name__ == "__main__":
	name = sys.argv[1]
	ppath  = sys.argv[2]

    	sch = stm32dip40_schematic.make(name, name)
    	brd = stm32dip40_board.make(sch, name, name)
	pickle = CXMLPickle(sch, brd)
	
	try:
		print "pickling into ", ppath+"/"+name+".placement"
		f = open(ppath+"/"+name+".placement",'w')
		pickle.pickleBoardDevices(f)
	except:
		print "pickle file missing or pickler has failed"
    
