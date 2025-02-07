#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-SP-7"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
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
                  124590, 124591, 124592, 124594, 124595, 124596, 124598, 124599, 124600,]    # dec 4


on["LH97576"] = [ 121981, 121982, 121983,
                  122412, 122413, 122414, 123714, 123715, 123716, 123718, 123719, 123720, 123722, 123723, 123724,]   # nov 28



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["LH85226"] = ""
pars1["LH89907"] = ""
pars1["LH97576"] = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["LH85226"] = ""
pars2["LH89907"] = ""
pars2["LH97576"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
