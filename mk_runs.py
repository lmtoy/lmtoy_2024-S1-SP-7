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
                  ]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["LH85226"] = ""


#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["LH85226"] = ""


if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
