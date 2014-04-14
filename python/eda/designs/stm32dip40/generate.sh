#/bin/sh

#Steps
##   name               dir        data            script
#0 - gen Schematic      schematic  name.schematic  name_gen_schematic.py  script to schematic data
#1 - gen Component      componnent name.componnent name_gen_componnent.py script to componnet data
#2 - gen Netlist        netlist    name.netlist    name_gen_netlist.py    script to netlist
#3 - gen Board          board      name.board      name_gen_board.py      script to board data
#4 - gen Placement      placement  name.placement  name_gen_placement.py  script to placement data
#5 - gen Route          route      name.route      name_gen_route.py      script to route data
#6 - gen Fabricate      fabricate  name.fabricate  name_gen_fabricate.py  script to fabrication data


mkdir work
python stm32dip40_gen_schematic.py   stm32dip40 work
python stm32dip40_gen_componnent.py  stm32dip40 work
python stm32dip40_gen_netlist.py     stm32dip40 work
python stm32dip40_gen_board.py       stm32dip40 work
python stm32dip40_gen_placement.py   stm32dip40 work
python stm32dip40_gen_route.py       stm32dip40 work
python stm32dip40_gen_fabricate.py   stm32dip40 work
