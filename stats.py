#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Statistics for fits files. 

import argparse
import math
import pyfits
import numpy as np
from astropy import units as u
import pylab
import glob
import sys
import casacore
from casacore.images import *
    
parser = argparse.ArgumentParser(description='Fits image stats', epilog="Output:", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("infile", type=argparse.FileType('rb'), help='input FITS image')

args = parser.parse_args()
parser.print_help()
    
hdulist = pyfits.open(args.infile)
hdu=hdulist[0]
data = hdulist[0].data
header = hdulist[0].header
hdulist.info()
hdulist.close()
max = np.max(data)
min = np.min(data)
rms= np.std(data)

#im=casacore.images.image(args.infile)
#casacore_stat=im.statistics()

print ("RMS =", rms, "Jy/beam")
print ("MAX =", max, "Jy/beam")    
print ("MIN =", min, "Jy/beam" )       
#print "casacore stats:", casacore_stat 
        

#if args != 1:
	#print 'Please specify a FITS file'
	#sys.exit(-1)
	
