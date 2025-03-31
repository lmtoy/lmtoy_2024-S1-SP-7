#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-SP-7"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["LH124379"] = [ 127860, 127861, 127862, 127864, 127865, 127866, 127868, 127869, 
                   127870, 127873, 127874, 127875, 128452, 128453, 128454,
                   129112, 129113, 129114, 129288, 129289, 129290,
                   132007, 132008, 132009, 132011, 132012, 132013, 132015, 132016, 132017, 
                   132020, 132021, 132022, 132024, 132025, 132026, 132028, 132029, 132030,]


on["LH136545"] = [ 129294, 129295, 129296,]


on["LH85226"] = [ 112601, 112602, 112603, 112605, 112606,
                  112607, 112610, 112611, 112612, 112614,
                  112615, 112616,
                  114429, 114430, 114431, 114433, 114434,
                  114435, 114437, 114438, 114439,
                  116632, 116633, 116634,
                  126745, 126746, 126747,
                  ]

on["LH89907"] = [ 123982, 123983, 123984, 123986, 123987, 123988,     # nov 30
                  124255, 124256, 124257, 124259, 124260, 124261,     # dec 2
                  124590, 124591, 124592, 124594, 124595, 124596, 124598, 124599, 124600,    # dec 4
                  124960, 124961, 124962, 124964, 124965, 124966, 124968, 124969, 124970, 
                  124973, 124974, 124975, 124977, 124978, 124979, 124981, 124982, 124983, 
                  127359, 127360, 127361, 127363, 127364, 127365, 127367, 127368, 127369, 
                  127372, 127373, 127374, 127376, 127377, 127378,
                  127462, 127463, 127464, 127466, 127467, 127468, 127470, 127471, 127472,]


on["LH97576"] = [ 121981, 121982, 121983,
                  122412, 122413, 122414, 123714, 123715, 123716, 123718, 123719, 123720, 123722, 123723, 123724,   # nov 28
                  127537, 127538, 127539, 127541, 127542, 127543, 127545, 127546, 127547, 127550, 127551, 127552,
                  127554, 127555, 127556, 127558, 127559, 127560, 127563, 127564, 127565, 127567, 127568, 127569, 
                  127571, 127572, 127573,
                  127733, 127734, 127735, 127737, 127738, 127739, 127741, 127742, 127743, 127851, 127852, 127853, 
                  127855, 127856, 127857,
                  128824, 128825, 128826,
                  128919, 128920, 128921, 128923, 128924, 128925,]

 




#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["LH124379"] = ""
pars1["LH136545"] = ""
pars1["LH85226"] = ""
pars1["LH89907"] = ""
pars1["LH97576"] = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["LH124379"] = ""
pars2["LH136545"] = ""
pars2["LH85226"] = ""
pars2["LH89907"] = ""
pars2["LH97576"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
