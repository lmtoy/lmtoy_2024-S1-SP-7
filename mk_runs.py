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
                  112615, 112616,]



#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["LH85226"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["LH85226"] = "bank=0"


#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}
pars3["LH85226"] = "bank=1"


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
