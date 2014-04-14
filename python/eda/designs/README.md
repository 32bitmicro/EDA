Gen EDA flow

## Steps
     name               dir        data            script
0 - gen Schematic      schematic  name.schematic  name_gen_schematic.py  script to schematic data
1 - gen Component      componnent name.componnent name_gen_componnent.py script to componnet data
2 - gen Netlist        netlist    name.netlist    name_gen_netlist.py    script to netlist
3 - gen Board          board      name.board      name_gen_board.py      script to board data
4 - gen Placement      placement  name.placement  name_gen_placement.py  script to placement data
5 - gen Route          route      name.route      name_gen_route.py      script to route data
6 - gen Fabricate      fabricate  name.fabricate  name_gen_fabricate.py  script to fabrication data


All data is in pickled form and can be exported or imported into CAD format

script can either generate data on the fly or import from pickle or CAD format 
script exports data in pickle and/or CAD format 

script: step n-1 pickle data -> internal data step n-1
script transform internal data step n-1 -> internal data step n
script: internal data step n -> pickle data step n


If script does not have the functionality then CAD tool is used
through a wrapper script with CAD data import/export capability

script: step n-1 pickle data -> internal data step n-1
script: internal data step n-1 -> cad data step n-1
tool:   cad data step n-1 -> cad internal data step n-1
tool transform cad internal data step n-1 -> cad internal data step n
tool:   cad internal data step n -> output cad data step n
script: output cad data step n -> internal data step n
script: internal data step -> pickle data step n



EAGLE flow 4.12 works, 5.2 does not!
1 - create library using script name_eaglelib.scr save as name_eagle.lbr
2 - new Board
3 - reference lib wit Use name_eagle.lbr
4 - use script name_eagle.scr
5 - save as name_eagle.brd

PCB flow
1 - start X server Xming
2 - start cygwin pcb 
3 - load layout name_pcb.pcb

