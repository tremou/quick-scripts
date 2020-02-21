#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Beam info (radio image). 

import argparse
import math
import numpy as np
import glob
import sys
import casacore
from casacore.images import *
from radio_beam import Beam
from astropy.io import fits   

parser = argparse.ArgumentParser(description='Beam size', epilog="Output:", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("infile", type=argparse.FileType('rb'), help='input FITS image')

args = parser.parse_args()
parser.print_help()


header = fits.getheader(args.infile)
my_beam = Beam.from_fits_header(header)
print (my_beam)
