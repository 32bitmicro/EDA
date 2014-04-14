import sys
from eda import *
from eda.xmlpickle import *
import stm32dip40_schematic

if __name__ == "__main__":
	name = sys.argv[1]
	ppath  = sys.argv[2]
    	sch = stm32dip40_schematic.make(name, name)
	pickle = CXMLPickle(sch, None)
	
	try:
		print "pickling into ", ppath+"/"+name+".componnent"
		f = open(ppath+"/"+name+".componnent",'w')
		#pickle.pickleSchematic(f)
		pickle.pickleDevices(f)
		pickle.pickleSymbols(f)
		#xml_pickle.XML_Pickler(sch.devices).dump(f)
	except:
		print "pickle file missing or pickler has failed"
    
